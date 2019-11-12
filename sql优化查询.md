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

* 利用字段排序，不重数据库取出数据  
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

