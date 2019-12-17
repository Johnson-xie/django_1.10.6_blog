```  
select (case state when 0 then '未解决' when 1 then '已解决' end) as 状态
from bug
```  

##  单纯循环使用yield  
```  
def func(iterator):
    for i in iterator:
        yield {field_one: i[0], field_two: i[1]}  
```  

## python 时间字符串和datetime相互转化  
```  
datetime.strptime('2019-10-12 10:22:45', "%Y-%m-%d %H:%M:%S")
datetime.strftime("%Y-%m-%d %H:%M:%S") if datetime else ""
```  

## 数据库层面直接转化为时间字符串  
```  
select ifnull(date_format(tb1.time_field, '%%Y-%%m-%%d %%H:%%i:%%S'), '') as str_time
from table as tb1
```  

## timestamp时间戳好像是正确的  


