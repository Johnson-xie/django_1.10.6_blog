## 数据库迁移  
* python manage.py makemigratons app_name  
`遇到关联错误，选择1，可以给空字符串填充或其他`  

* python manage.py migrate app_name  
`blank=True表单可以为空，数据库存的是字符串，如果是时间类型，null=True，blank=True，数据库才存的是null`  
