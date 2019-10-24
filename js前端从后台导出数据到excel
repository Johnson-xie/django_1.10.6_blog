# 后台返回excel响应字节流对象，前端直接获取下载excel文件
* 后台设置  
""" 
# 接收参数
version = request.POST.get('version', '')
scene_selected = request.POST.get('scene_selected', '')
datetime_start = request.POST.get('datetime_start', '')
datetime_end = request.POST.get('datetime_end', '')
date_direction = request.POST.get('date_direction', '')


# 新建excel文件
import openpyxl
filename = '文件名.xlsx'
response = HttpResponse(content_type='text/xlsx; charset=utf-8')
response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(filename))
workbook = openpyxl.Workbook()
workbook.save(response)
return response
"""  
## method 1
* get请求过长，使用post表单模拟，页面会进行实时刷新
"""  
var export_url = "/xxx/xxx/xxx/";
        var data = {
            "version": version,
            "scene_selected": scene_selected,
            "datetime_start": datetime_start,
            "datetime_end": datetime_end,
            "date_direction": date_direction
        };

        var form = document.createElement("form");
        form.style.display = 'none';
        form.action = export_url;
        form.method = "post";
        document.body.appendChild(form);

        for(var key in data){
          var input = document.createElement("input");
          input.type = "hidden";
          input.name = key;
          input.value = data[key];
          form.appendChild(input);
        }
        form.submit();
        form.remove();
    }
"""  

## mthod 2  
* 防止页面刷新 
注意，这里的submitData是使用jquery构建key:value的form参数对象。传入导出方法后被解析还原成form表单数据。
代码的思路就是，利用隐藏的iframe内嵌模块，在iframe内部post表单提交导出我们想要的数据，页面翻转也仅发生在iframe内部，
我们的主页面并不会发生翻转，从而达到仿异步post导出的效果。
"""  
_export = {
        canExport:false,
        post:function(data,exportUrl) {
            _export.canExport = true;
            if ($('#exportIframe').length > 0) {
                $('#exportIframe').remove();
            }
            $('body').append('<iframe id="exportIframe" width="0" height="0" src="#"></iframe>');
            $('#exportIframe').load(function() {
                if (_export.canExport) {
                    var formData = '<form method="post" action='+exportUrl+' >';
                    for (var name in data) {
                        formData = formData + '<input type="text" name="'+name+'" value="'+data[name]+'" />';
                    }
                    formData = formData + '<input type="submit" id="submitExportForm"/>';
                    formData = formData + '</form>';
                    $(this).contents().find('body').append(formData);
                    $(this).contents().find('#submitExportForm').click();
                    _export.canExport = false;
                }
            });
        }
}
_export.post(submitData,exportUrl);
"""  

## method 3  
* 还是写上get请求  
"""  
var exportUrl = '/xxx;';
window.open(exportUrl);
"""  
