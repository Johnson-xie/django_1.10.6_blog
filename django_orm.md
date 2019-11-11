* models.CASCADE 外键定义了级联删除，删除时就会级联删除，不用迁移数据库  
* PerfScene.objects.filter(id=scene_id).delete()  
* scene  --> target ---> record  

* query to ORM row  
* insert, update  
```  
with connection.cursor() as c:
    c.execute()
```
