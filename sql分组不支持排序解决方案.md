# 分组后提取特征字段，最好是多个，使用新表和原表内联  
```  
group_sql = "select tb1.* " \
            "from tbl_perf_result as tb1 inner join " \
                    "(select date, max(commit_number) as max_commit " \
                    "from tbl_perf_result " \
                    "where target_id=%s and date in %s " \
                    "group by date) as tb2 " \
            "on tb1.date=tb2.date and tb1.commit_number=tb2.max_commit"
```  
