* 子表查询  
```  
select * from tbl_version_project where id in (select version_id from tbl_perf_user where user_id='xwx620452')
```  
* 按字段分组后，把每组中的字段链接起来  
```  
select version_id, group_concat(user_id) as user_ids 
from tbl_perf_user
GROUP BY version_id
```  

* 返回一张表中所有的用户
1. 连表获取中文名和英文名，两个字段链接起来  
2. 有多个row,再将多个row链接起来为一个字符串  
```  
select group_concat(DISTINCT(CONCAT(tu.name_chs,tu.user_id)))  
from tbl_user as tu inner join tbl_perf_user as tpu on tu.user_id=tpu.user_id  
where tpu.version_id=22  
```  

