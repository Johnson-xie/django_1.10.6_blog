* 批量更新数据  
```  
@ajax_required
@login_required
def sort_scene(request):
    data = json.loads(request.body.decode('utf-8'))
    ids = tuple(data.get('ids', []))
    if len(ids) < 2:
        return JsonResponse({"code": 200, "msg": "排序成功!"})
    head = "update tbl_perf_scenes set priority = CASE id "
    body = " ".join(["WHEN " + str(_id) + " THEN " + str(priority) for priority, _id in enumerate(ids)])
    end = " END WHERE id in {}".format(ids)
    sql = head + body + end
    with connection.cursor() as c:
        c.execute(sql)
    return JsonResponse({"code": 200, "msg": "排序成功!"})
```  
