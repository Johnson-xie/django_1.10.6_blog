## 分组间的数据有关联，分组之后使用for处理，原位处理  
```  
    new_result = []
    for group_name, content in groupby(result, key=lambda x: x['group_name']):
        content = list(content)
        for i in range(1, len(content)):
            content[i]['percent'] = '{:.2%}'.format(content[i]['total_count']/content[0]['total_count'])
            for item in content[i]['detail']:
                item["percent"] = '{:.2%}'.format(item['total_count']/content[i]['total_count'])
        new_result.extend(content)
```  
