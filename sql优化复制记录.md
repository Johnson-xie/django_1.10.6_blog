## 复制其他记录到新的记录，对每条记录相关值做定制处理  

```  
def migrate_scene(request, version_id):
    data = json.loads(request.body.decode('utf-8'))
    scene_ids = data.get('scene_ids', [])
    scene_ids.sort()  # 确保后续场景，按id顺序插入，方便插入对应指标
    if not version_id or not scene_ids:
        return JsonResponse({"code": 400, "msg": "未能复制场景"})

    query_sql = "select guard_field, sceneid, concat(scene_name, '[复制]'), scene_desc, scene_remark, guarder," \
                " 0 as display, priority, 0 as is_active , 'time_placeholder' as create_time, {} as version " \
                "from tbl_perf_scenes " \
                "where id in ({}) " \
                "order by priority".format(version_id, ', '.join(map(str, scene_ids)))
    with connection.cursor() as c:
        c.execute(query_sql)
        rows = c.fetchall()

        # 检查迁移的场景名是否已经存在该版本
        scenes = ",".join(["'" + row[3] + "'" for row in rows])
        check_sql = "select * from tbl_perf_scenes where version={} and scene_name in ({})".format(version_id, scenes)
        c.execute(check_sql)
        row = c.fetchone()
        if row:
            return JsonResponse({"code": 400, "msg": "场景名冲突，迁移失败"})
        # 场景迁移
        content = ",".join(map(str, rows)).replace('time_placeholder', timezone.now().strftime('%Y%m%d%H%M%S'))
        insert_sql = "insert into tbl_perf_scenes " \
                     "(guard_field, sceneid, scene_name, scene_desc, scene_remark, " \
                     "guarder, display, priority, is_active, create_time, version) " \
                     "values " + content

        c.execute(insert_sql)

        # 指标迁移

        # 获取新生成的场景id列表，倒叙
        new_id_desc_sql = "select id from tbl_perf_scenes order by id desc limit {}".format(len(scene_ids))
        c.execute(new_id_desc_sql)
        new_scene_ids = c.fetchall()

        # 获取源场景的所有指标
        source_info_sql = "select tpc.scene_id, concat(tpc.target_name, '[复制]'), tpc.upper_limit, tpc.name_related, 0 as display, " \
                          "tpc.daily_upper_limit, tpc.unit, tpc.`owner`, tpc.owner_pl, tpc.formula, " \
                          "tpc.formula_annotation, tpc.remark, tpc.priority, 0 as `status`, tpc.counter_id, " \
                          "'time_placeholder' as create_time " \
                          "from tbl_perf_scenes as tps " \
                          "inner JOIN " \
                          "tbl_perf_counter as tpc " \
                          "on tps.id=tpc.scene_id " \
                          "and tps.id in ({}) " \
                          "order by tpc.scene_id desc".format(','.join(map(str, scene_ids)))
        c.execute(source_info_sql)
        target_rows = c.fetchall()

        new_target_rows = []
        for _, contents in groupby(target_rows, key=lambda x: x[0]):
            for _id in new_scene_ids:
                # content
                for content in contents:
                    row = _id + content[1:]
                    new_target_rows.append(row)

        contents = ','.join(map(str, new_target_rows))
        # 形成如下格式
        # [
        # (id1, target_name, upper_limit, name_related, display, daily_upper_limit, unit, `owner`, owner_pl, formula,
        # formula_annotation, remark, create_time),
        # (id2, ...), (), ()
        # ]
        contents = contents.replace('time_placeholder', timezone.now().strftime('%Y%m%d%H%M%S'))
        if contents:  # 可能不存在指标
            insert_target_sql = "insert into tbl_perf_counter " \
                                "(scene_id, target_name, upper_limit, name_related, display, " \
                                "daily_upper_limit, unit, `owner`, owner_pl, formula, " \
                                "formula_annotation, remark, priority, `status`, counter_id, create_time) " \
                                "values " + contents
            c.execute(insert_target_sql)

    return JsonResponse({"code": 200, "msg": "迁移成功!"})

```  
