```  
select tu.id, tu.user_id, tpg.id, tpg.user_id 
from tbl_perf_guarder as tpg inner join tbl_user as tu 
on tu.user_id<>'' and tpg.user_id like CONCAT('%',tu.user_id)
order by tpg.id;

update tbl_perf_guarder set user_id=NULL where user_id='';


update tbl_perf_guarder as tpg
inner join tbl_user as tu
on tu.user_id is not null and tu.user_id<>'' and tpg.user_id like concat('%', tu.user_id)
set tpg.user_id=tu.id;

alter table tbl_perf_guarder modify user_id INT;

```  
