


# 6 模型 模板 视图
***
## 6.1 创建数据驱动页面的流程
1. 在 views.py 文件中导入想使用的模型。  
2. 在视图函数中查询模型，获取想呈现的数据。  
3. 把从模型获取的数据传给模板上下文。  
4. 创建或修改模板，显示上下文中的数据。  
5. 把 URL 映射到视图上（如果还未做的话）。  

## 6.2 在首页显示分类
`主页显示 最受欢迎的5个分类`
* view中导入所需模型
```from rango.models import Category```
* 修改index视图  



