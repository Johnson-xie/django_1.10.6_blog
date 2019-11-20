# 需要上传下载文件到ftp服务器  

## 上传文件到指定ftp服务器  
* 前段使用input type="file"表单字段  `<input type="file" name="attach" style="width: 100%;"> `  
* django后台获取前端传递的文件  `file_obj = request.FILES.get(filename)`  
* 文件对象传入ftp模块  
```  
    from ftplib import FTP  
    try:  
        ftp = FTP()  
        ftp.connect(FTP_SERVER, 21)  
        ftp.login(USERNAME, PASSWORD)  

        remotepath = FTP_PATH[FTP_PATH.find('/', 6):] + filename  
        bufsize = 1024  
        ftp.storbinary('STOR ' + remotepath, file_obj, bufsize)  
        ftp.quit()  
    except Exception as MSG:  
        print('上传失败:', MSG)  
```  
* 下载文件(上传文件改变了名字，名称重新修改)  
```  
    from io import BytesIO
    try:
        ftp = FTP()
        ftp.connect(FTP_SERVER, 21)
        ftp.login(USERNAME, PASSWORD)

        remotepath = FTP_PATH[FTP_PATH.find('/', 6):] + filename

        fp = BytesIO()
        bufsize = 1024
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
        fp.seek(0)
        content = fp.read()
        fp.close()
        ftp.quit()
        return content
    except Exception as MSG:
        print('下载失败:', MSG)
```  

## 上传文件报错  
* 文件名含中文报错  
```  
UnicodeEncodeError: 'gbk' codec can't encode character '\xd0' in position 0: illegal multibyte sequence

或UnicodeEncodeError: 'latin-1' codec can't encode characters in position 5-7: ordinal not in range(256)
```  
* 设置编码  
```  
def upload_file(filename, file_upload_obj):
    try:
        ftp = FTP()
        ftp.encoding = 'UTF-8'
        ftp.connect(FTP_SERVER, 21)
        ftp.login(USERNAME, PASSWORD)

        remotepath = FTP_PATH[FTP_PATH.find('/', 6):] + filename
        bufsize = 1024
        ftp.storbinary('STOR ' + remotepath, file_upload_obj, bufsize)
        ftp.quit()
    except Exception as MSG:
        print('上传失败:', MSG)
```  

*  553 Could not create file  
* 多半是根路径不对或目标文件夹不存在  





