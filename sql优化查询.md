## 场景连表查询  
### 第一版  
```  
    date_time = datetime.datetime.now()
    date_today = date_time.strftime('%Y-%m-%d')
    date_list = get_datelist('datetime_start', date_today, 5)
    date_tuple = tuple(date_list)

    with connection.cursor() as c:
        sql = "select c.*, r.date, r.`value`, r.version, r.commit_number, r.is_lower_limit, r.is_upper_limit, r.is_daily_upper_limit, r.today_trend, r.more from " \
                  "(select tpc.id as id, tpc.target_name, tpc.name_related, tpc.lower_limit, tpc.upper_limit, tpc.daily_upper_limit, tps.scene_name, tps.scene_desc, tps.guarder, tps.guard_field " \
                  "from tbl_perf_counter as tpc, tbl_perf_scenes as tps " \
                  "where tpc.scene_id=tps.id " \
                  "and tps.version={} " \
                  "and tps.display=TRUE " \
                  "and tpc.display=TRUE) as c " \
              "left join (select * from tbl_perf_result as tpr " \
                  "where date in {} " \
                  "order by target_id, date desc) as r " \
              "on c.id=r.target_id " \
              "order by c.scene_name, r.target_id, r.date desc, r.commit_number desc;".format(version_dict[version], date_tuple)

        c.execute(sql)
        rows = c.fetchall()

    data = []
    for _, group in groupby(rows, key=lambda x: x[0]):
        t = list(group)
        record = [PerfData(*list(group_sub)[0]) for _, group_sub in groupby(t, key=lambda x: x[10])]
        row = record[0]

```

### 第二版 利用字段排序，不重数据库取出数据  
```  
        sql = "select c.id, c.target_name, c.name_related, c.lower_limit, c.upper_limit, c.daily_upper_limit, c.scene_name, c.scene_desc, c.guarder, c.guard_field , r.date, r.`value`, r.version, r.commit_number, r.is_lower_limit, r.is_upper_limit, r.is_daily_upper_limit, r.today_trend, r.more " \
              "from " \
                  "(select tpc.id as id, tps.priority as p1, tpc.priority as p2, tpc.target_name, tpc.name_related, tpc.lower_limit, tpc.upper_limit, tpc.daily_upper_limit, tps.scene_name, tps.scene_desc, tps.guarder, tps.guard_field " \
                  "from tbl_perf_counter as tpc right join tbl_perf_scenes as tps on  tpc.scene_id=tps.id " \
                  "where tps.version={} " \
                  "and tps.is_active=1 " \
                  "and tps.display=TRUE " \
                  "and (tpc.display=TRUE or tpc.display is null)) as c " \
              "left join " \
                  "(select * " \
                  "from tbl_perf_result as tpr " \
                  "where date in {} " \
                  "order by target_id, date desc) as r " \
              "on c.id=r.target_id " \
              "order by c.p1, c.p2, r.date desc, r.commit_number desc;".format(version_dict[version], date_tuple)
```  
### 第三版  where在on的基础上在过滤  
* 场景与指标使用外联查询，已场景为主，场景下指标为displey为空或为1都显示  
```  

    with connection.cursor() as c:
        # 连表时on后面表示需要的，where在on查询的结果上再筛选
        sql = "select c.id, c.target_name, c.name_related, c.lower_limit, c.upper_limit, c.daily_upper_limit, c.scene_name, c.scene_desc, c.guarder, c.guard_field , r.date, r.`value`, r.version, r.commit_number, r.is_lower_limit, r.is_upper_limit, r.is_daily_upper_limit, r.today_trend, r.more " \
              "from " \
                  "(select tpc.id as id, tps.priority as p1, tpc.priority as p2, tpc.target_name, tpc.name_related, tpc.lower_limit, tpc.upper_limit, tpc.daily_upper_limit, tps.scene_name, tps.scene_desc, tps.guarder, tps.guard_field " \
                  "from tbl_perf_counter as tpc right join tbl_perf_scenes as tps on  tpc.scene_id=tps.id and (tpc.display=1 or tpc.display is null)" \
                  "where tps.version={} " \
                  "and tps.is_active=1 " \
                  "and tps.display=1 ) as c " \
              "left join " \
                  "(select * " \
                  "from tbl_perf_result as tpr " \
                  "where date in {} " \
                  "order by target_id, date desc) as r " \
              "on c.id=r.target_id " \
              "order by c.p1, c.p2, r.date desc, r.commit_number desc;".format(version_dict[version], date_tuple)
        c.execute(sql)
        rows = c.fetchall()
    data = []
    for _, group in groupby(rows, key=lambda x: str(x[0]) + x[6]):  # None + 场景名用来标记分组
        t = list(group)
        record = [PerfData(*list(group_sub)[0]) for _, group_sub in groupby(t, key=lambda x: x[11])]
        row = record[0]
```



## 获取一个版本下的所有场景，及版本名，并获取每个场景下的指标数  
```  
    result = []
    sql = "select s.*, count(s.id) as target_count " \
          "from " \
              "(select tps.id, tvp.id as version_id, tps.guard_field, tps.sceneid, tps.scene_name, tps.scene_desc, " \
              "tps.`guarder`, tps.scene_remark, tps.priority, tps.start_time, tps.end_time, tps.is_active, tps.display, " \
              "tps.create_time, tps.update_time, tps.update_user " \
              "from tbl_version_project as tvp " \
              "inner join " \
              "tbl_perf_scenes as tps " \
              "on tvp.id=tps.version and tps.version={}) as s " \
          "left join tbl_perf_counter as tpc on s.id=tpc.scene_id " \
          "where s.version_id={} " \
          "GROUP BY s.id " \
          "order by s.priority".format(version_id, version_id)

    with connection.cursor() as c:
        c.execute(sql)
        rows = c.fetchall()
        for row in rows:
            data = SceneList(*row)
            result.append({
                "id": data.id,
                "version": data.version_id,
                "field": data.field,
                "scene_id": data.sceneid,
                "name": data.name,
                "desc": data.desc,
                "owner": data.owner,
                "remark": data.remark,
                "priority": data.priority,
                "start_time": data.start_time.astimezone(shanghai_zone).strftime('%Y-%m-%d %H:%M:%S') if data.start_time else "",
                "end_time": data.end_time.astimezone(shanghai_zone).strftime('%Y-%m-%d %H:%M:%S') if data.end_time else "",
                "status": data.status,
                "display": data.display,
                "create_time": data.create_time.astimezone(shanghai_zone).strftime('%Y-%m-%d %H:%M:%S') if data.create_time else "",
                "update_time": data.update_time.astimezone(shanghai_zone).strftime('%Y-%m-%d %H:%M:%S') if data.update_time else "",
                "update_user": data.update_user,
                "target_count": data.count
            })
    return JsonResponse({"data": result})
SceneList = namedtuple(
    'SceneList',
    [
        'id',
        'version_id',
        'field',
        'sceneid',
        'name',
        'desc',
        'owner',
        'remark',
        'priority',
        'start_time',
        'end_time',
        'status',
        'display',
        'create_time',
        'update_time',
        'update_user',
        'count',

    ]
)    

```  


