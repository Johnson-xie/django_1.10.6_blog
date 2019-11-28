# 分组优化union  
* 需要获取字段不同的每组数据，每组数据的筛选只有一个字段不同，如果使用in，统计该数据有多少个，会导致只有一条数据  
```  
select ifnull(result, 'NA') as result, ifnull(url, '') as url, count(id)
from basic_quality_module_info "
where report_id={0} and team_id={1} and property_id=3 and module_id in (1, 2, 3, 5)"format(node_report, static_check_group[0], report_id)
会导致只有一条数据  
```  

* 使用union优化  
```  
select ifnull(result, 'NA') as result, ifnull(url, '') as url, count(id) from basic_quality_module_info  
where report_id={0} and team_id={1} and property_id=3 and module_id=2 union all  
select ifnull(result, 'NA') as result, ifnull(url, '') as url, count(id) from basic_quality_module_info 
where report_id={2} and team_id={1} and property_id=3 and module_id=1 union all 
select ifnull(result, 'NA') as result, ifnull(url, '') as url, count(id) from basic_quality_module_info 
where report_id={2} and team_id={1} and property_id=3 and module_id=3 union all 
select ifnull(result, 'NA') as result, ifnull(url, '') as url, count(id) from basic_quality_module_info 
where report_id={2} and team_id={1} and property_id=3 and module_id=4 ".format(node_report, static_check_group[0], report_id)
导致代码冗余
```  

* 使用group分组优化  
```  
select ifnull(result, 'NA') as result, ifnull(url, '') as url, count(id) from basic_quality_module_info 
where report_id={0} and team_id={1} and property_id=3 and module_id=2 union all 
select ifnull(result, 'NA') as result, ifnull(url, '') as url, count(id) from basic_quality_module_info 
where report_id={2} and team_id={1} and property_id=3 and module_id in (1, 3, 4) 
group by report_id, team_id, property_id, module_id".format(node_report, static_check_group[0], report_id)
```  


