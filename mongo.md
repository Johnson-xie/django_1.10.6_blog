# first  

```  
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

client = MongoClient('ip', 27017)
db = client.test  # 库名
collection = db.quality_report_dup  # 表名
row = collection.find_one({'version': '20B'})  # 获取筛选后的第一条
row = collection.find_one({'_id': ObjectId("5d511d1c91f2cd3a60471b53")})  # 根据id直接获取对象


cursor = collection.find({'version': '20B'}).sort('update_time')
print(cursor.count())
for item in cursor:
    pprint(item)
```

## like查询  
```  
db.getCollection('table_name').find({'field':'value', 'project':/hello world/}).sort({'start_time': -1})
```  
