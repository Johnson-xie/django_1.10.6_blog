```  
select (case state when 0 then '未解决' when 1 then '已解决' end) as 状态
from bug
```  
