## ORM获取的直接是属性对应的值，利用这一点，可以直接返回json数据  
```  
def perf_permission(request):
    data = []
    user_id = request.session.get('user_id', '')
    perf_permissions = PerfUser.objects.filter(user__user_id=user_id).values_list('permission', flat=True)
    project = PerfProject.objects.filter(status=1).order_by('-id').values('id', 'version_alias', 'version_num')
    data = list(project)
    # for project in PerfProject.objects.filter(status=1).order_by('-id'):
    #     data.append(
    #         {
    #             'id': project.id,
    #             'version_alias': project.version_alias,
    #             'version_num': project.version_num,
    #         }
    #     )
    return {'perf_versions': data, 'perf_admin': perf_permissions.count() != 0, 'perf_super': any(perf_permissions)}
```  

## 更新数据表用户权限，增加外键，利用chain展开fetchall()的结果，拼接插入语句  
```  
def manage_perf_user(request, version_id):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        user_ids = data.get('users', [])

        with connection.cursor() as c:
            delete_sql = "delete from tbl_perf_user where version_id={} and permission<>1;".format(version_id)
            c.execute(delete_sql)
            if user_ids:

                sql = "select id from tbl_user where user_id in ('{}')".format("','".join(user_ids))
                c.execute(sql)
                ids = c.fetchall()

                content = ",".join(str((user_id, version_id)) for user_id in chain(*ids))
                insert_sql = "insert into tbl_perf_user (user_id, version_id) values " + content
                c.execute(insert_sql)
            return JsonResponse({"data": "修改成功"})
    else:
        with connection.cursor() as c:
            sql = "select GROUP_CONCAT(DISTINCT(tu.user_id)) " \
                  "from tbl_user as tu inner join tbl_perf_user as tpu on tu.id=tpu.user_id " \
                  "where tpu.version_id={} and tpu.permission=0".format(version_id)
            c.execute(sql)
            rows = c.fetchone()
            data = rows[0] if rows[0] else []
        return JsonResponse({"data": data})
```  

