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
