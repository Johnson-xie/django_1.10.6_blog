## 正常存标准时间，取的时候转化为本地时间,中国会统一加8个小时  
```  
from django.utils import timezone
"modify_time": timezone.localtime(data.modify_time).strftime(DATETIME_FORMAT) if data.modify_time else "",
```  
## 代码层面可以设置更新时间  
```  
create_time = models.DateTimeField(auto_now_add=True)
modify_time = models.DateTimeField(auto_now=True)  
```  

## 数据库层面自动生成新的和更新旧的  
```  
`create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
`modify_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
```  

## orm插入失败，某个时间字段为创建时间，自动生成失败，使用直接连接原生sql插入  
```  
orm变态啊，
数据库自动生成时间，orm执行失败
params = (params.get("old_version"), params.get("new_version"), params.get("project_path"),
          params.get("new_project_path"), params.get("target_branch"), params.get("new_target_branch"),
          params.get("merge_commit_time", ""), 0, 0, 999, f"{user.name_chs} {user.user_id}",
          f"{user.name_chs} {user.user_id}")
sql = "insert into tbl_mr_sync_config " \
      "(old_version, new_version, project_path, new_project_path, target_branch, new_target_branch, " \
      "merge_commit_time, status, sync_status, sort, create_user, modify_user) " \
      "values " \
      "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
with connection.cursor() as c:
    c.execute(sql, params)
数据库有一个字段为自动生成

```  
