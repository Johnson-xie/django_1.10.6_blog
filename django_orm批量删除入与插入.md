```  
@login_required
def subscribe_email(request):
    user_id = request.session.get('user_id', '')
    if request.method == 'POST':
        version_ids = request.POST.get('version_ids')
        user = User.objects.get(user_id=user_id)
        FlowerReceiver.objects.filter(user=user).delete()

        if version_ids:
            queryset = [FlowerReceiver(user=user, version_id=version_id) for version_id in version_ids]
            FlowerReceiver.objects.bulk_create(queryset)

        return JsonResponse({"code": 200, "msg": "订阅操作成功"})
    else:
        versions = Project.objects.all().order_by('project_id').values('project_id', 'project_name')
        with connection.cursor() as c:
            sql = "select ts.version_id " \
                  "from tbl_user as tu inner join tbl_flower_dts_sms as ts on tu.id=ts.user_id " \
                  "and tu.user_id='{}'".format(user_id)

            c.execute(sql)
            rows = c.fetchall()
            subscribe = [i for i in chain(*rows)]
        return JsonResponse({"versions": list(versions), "subscribe": subscribe})
```  
