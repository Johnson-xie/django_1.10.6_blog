```  
from django.db import transaction

with transactions.atomic():  # 开启事务  
    save_id = transaction.savepoint()  # 设置临时保存点  
    ...
    try:
        error
    except:
        transaction.savepoint_rollback(save_id)  # 回滚
        return HttpResponse(status=400, content="错误信息")  
```  
