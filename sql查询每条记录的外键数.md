## 查询每条记录的外键数  
* 进行左关联查询，没有的那个表获取一个字段，如果该字段为空，把计数值改为0  
* 没有直接获取到指标为0计数，计数结果为1，通过代码处理判断目标name为空进行修正  
```  
def get_scene_list(request, version_id):
    result = []
    **sql = "select s.*, count(s.id) as target_count, tpc.target_name " \**
          "from " \
              "(select tps.id, tvp.id as version_id, tps.guard_field, tps.sceneid, tps.scene_name, tps.scene_desc, " \
              "tps.`guarder`, tps.scene_remark, tps.priority, tps.start_time, tps.end_time, tps.is_active, tps.display, " \
              "tps.create_time, tps.update_time, tps.update_user " \
              "from tbl_version_project as tvp " \
              "inner join " \
              "tbl_perf_scenes as tps " \
              "on tvp.id=tps.version and tps.version={}) as s " \
          **"left join tbl_perf_counter as tpc on s.id=tpc.scene_id " \**
          "where s.version_id={} " \
          **"GROUP BY s.id " \**
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
                "start_time": (data.start_time + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S') if data.start_time else "",
                "end_time": (data.end_time + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S') if data.end_time else "",
                "status": data.status,
                "display": data.display,
                "create_time": (data.create_time + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S') if data.create_time else "",
                "update_time": (data.update_time + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S') if data.update_time else "",
                "update_user": data.update_user,
                **"target_count": data.count if data.target_name else 0**
            })
    return JsonResponse({"data": result})

``` 



