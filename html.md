



### 点击事件  
```  
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>jQuery Example</title>
</head>
<script type="text/javascript" src="C:/Users/xwx620452/Desktop/qd_js/jquery-1.10.2.js"></script>
<script type="text/javascript" src="C:/Users/xwx620452/Desktop/qd_js/jquery-ui-1.10.4.custom.js"></script>

<script>

    $(document).ready(function() {
        <!-- jquery添加点击事件 -->
        $('#toggle_message').click(function() {
            var value = $(this).attr('value');
            <!-- alert(value); -->
            $('#message').toggle('fast');
            
            if (value == 'Hide') {
                $(this).attr('value', 'show');
            } else if (value='show') {
                $(this).attr('value', 'Hide')
            }
        })
    })
    
    <!-- 函数执行，标签中添加onclick属性 -->

</script>


<body>
    <input id="toggle_message" type="button" value="Hide" />
    <p id="message">You can see this paragraph</p>
</body>
</html>
```

## jquery 多值填充
[jquery](https://www.w3cschool.cn/jqueryui/example-autocomplete.html)












