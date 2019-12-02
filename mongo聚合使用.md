## 原生语句  
```  
db.getCollection('quality_report_check_item').aggregate([
{"$match": {"version": "5G RAN V100R003C10", "start_time": {"$lte":"2019-12-02 00:00:00"}}},
{"$sort": {"start_time": -1}},
{"$group": {_id: "$tool_name", newest_data:{"$first":"$$ROOT"}}}])
```  
