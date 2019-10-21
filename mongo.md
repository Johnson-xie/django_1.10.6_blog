# first  

```  
client = MongoClient('ip', 27017)
db = client.test  # 数据库名
collection = db.quality_report_dup  # 表名
row = collection.find_one({'version': '20B'})  # 过滤条件
```
