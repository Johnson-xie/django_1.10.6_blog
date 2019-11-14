
```  
class PerfProject(models.Model):  
    ~~id = models.AutoField(primary_key=True, db_column='id')~~  
    project_name = models.CharField(max_length=200, unique=True, db_column='name_project', default='')  
    version_alias = models.CharField(max_length=200, default='', db_column='version_alias', null=True)  
    version_num = models.CharField(max_length=200, default='', db_column='version_num', null=True)  
    version_desc = models.CharField(max_length=500, default='', db_column='version_desc', null=True)  
    priority = models.PositiveIntegerField(default=0, db_column='priority')  
    ftp_url = models.CharField(max_length=500, default='', db_column='ftp_url')  
    status = models.PositiveIntegerField(default=0, db_column='status')  
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time')  
    start_time = models.DateTimeField(default=None, db_column='start_time')  
    end_time = models.DateTimeField(default=None, db_column='end_time')  
    remark = models.CharField(max_length=500, default='', db_column='remark')  

    class Meta:  
        db_table = 'tbl_version_project'  

```  


* 以下会报类似错误，根本原因应该是没有使用django命令迁移数据库，表的字段和数据库关系没有对应上，表名没有对应上都会报类似错误  
* 刚开始没有使用命令迁移的情况下，没有写db_table和db_column属性  
```  
class PerfAdministrator(models.Model):  
    user_num = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_num')  
    user_id = models.CharField(max_length=100, default='', db_column='user_id')  
    version_id = models.ForeignKey(PerfProject, on_delete=models.CASCADE, db_column='version_id')  
    permission = models.IntegerField(default=0, db_column='permission')  

    class Meta:  
        db_table = 'tbl_perf_user'  
 
```  

