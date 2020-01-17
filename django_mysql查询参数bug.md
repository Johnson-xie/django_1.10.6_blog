
# 字符串的参数使用and不要和in元组的靠一起
```  
    sql_target = """
            ...
            where 
                tpt.display=1 and tpt.reference=%s and tpg.version=%s and tpt.version=%s and tps.scene_name in %s 
            order by 
                tps.id asc,tpt.id asc;
            """
    data = []
    PerfTarget.objects.raw(sql_target, (reference, version, version_dict[version], scene_tuple)):
```  

# 查询字符串入参in 不受语法限制(一个元素的情况)  
```  
select 
    * 
from 
    tbl
where
    date in %s
    
c.execute(sql, (date_tuple,))
```  

