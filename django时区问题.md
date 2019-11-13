## 时区问题  
```  
datetime.datetime.now()  产生本地时间  
django.utils.timezone.now()  产生标准时区时间  
* datetime类型都可以转为字符串  
time_obj..strftime('%Y-%m-%d %H:%M:%S')  
```  

## django配置  
```  

USE_TZ = True  为True时，时区不生效，django的timezone生成的时间为标准时区时间  
不影响datetime的生成时间，datetime独立，但是如数据库时，django的模型字段为时间类型，会自动转化为标准时区的时间  
TIME_ZONE = 'Asia/Shanghai'  
```  

## pytz  
```  
from pytz import timezone  
from django.conf import settings  

cst_tz = timezone(settings.TIME_ZONE)
time_obj.astimezone(cst_tz) 时间对象转化为对应时区时间  
```  

## datetime  
* timedelta直接做时间对象的加减操作  
```  
from datetime import timedelta  
t1 = datetime.now()   
td = timedelta(hours=8)  
t2 = t1 + td  
```  
