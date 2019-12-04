## 字段包含于的联表批量修改  
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

## 字段相等时的联表批量修改，并添加外键约束，约束后被关联的主键表，不能直接删除  
```  
update tbl_perf_user as tpu
inner join tbl_user as tu
on tpu.user_id=tu.user_id
set tpu.user_id=tu.id;

alter table tbl_perf_user modify user_id INT;

Alter table tbl_perf_user add constraint fk_perf_user_idx foreign key(user_id) REFERENCES tbl_user(id)
```  

## 新增mysql table关联外键  
```  
CREATE TABLE `tbl_flower_dts_sms` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `version_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `flower_user_idx` (`user_id`),
  CONSTRAINT `flower_user_idx` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8
```  
