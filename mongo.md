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

## 原生分组查询  
```  
    aggs = [
        {"$match": {"version": {"$in": ["word", "hello"]}}},
        {"$sort": {"update_time": -1}},
        {"$group": {"_id": "$version", "data": {"$first": "$$ROOT"}}}
    ]
    collection = db.表名1
    datas = collection.aggregate(aggs)
```  

```  
       aggs = [
        {"$match": {"version": {"$in": versions}, "group": {"$in": ["L2", "L3"]}}},
        {"$sort": {"update_time": -1}},
        {"$group": {"_id": {"version": "$version", "group": "$group"}, "data": {"$first": "$$ROOT"}}}
    ]
    collection = db.表名2
    datas = collection.aggregate(aggs)
```  

* 使用pymongo的查询语句  
```  
    collection = db.version_result
    data = collection.find({"field_name": "val", "config_type": "daily"}).sort("start_time", -1).limit(1)
    data = list(data)
    if not data:
        return
    else:
        info = data[0]
```  

* 既有原生和pymongo的查询  
```  
    end = datetime.datetime.now()
    start = end + datetime.timedelta(days=-1)

    collection = db.version_result
    # data = collection.find(
        # {"config_type": "daily",
        #  # "project": {"$regex": r".*5G RAN.*"},
        #  "project": {"$in": versions},
        #  "start_time": {"$gte": str(start), "$lte": str(end)},
        #  }).sort("start_time", -1)


    aggs = [
        {"$match": {"project": {"$in": versions}, "config_type": "daily", "start_time": {"$gte": str(start), "$lte": str(end)}}},
        {"$sort": {"update_time": -1}},
        {"$group": {"_id": {"version": "$version"}, "data": {"$first": "$$ROOT"}}}
    ]
    collection = db.version_result
    datas = collection.aggregate(aggs)

```  



