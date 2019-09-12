```  
def add_bug(request):
    res = {
        'code': 200
    }
    data = request.POST
    if request.method == 'POST':
        bug_form = BugForm(request.POST)
        if bug_form.is_valid():
            from pprint import pprint
            data = bug_form.cleaned_data

            # bug = bug_form.using('db_bug_trace').save(commit=False)

            user_id = request.session.get('user_id')
            if not user_id:
                return HttpResponseRedirect(reverse('login'))
            poster = BugUser.objects.using('db_bug_trace').get(userid=user_id)
            if poster:
                data['poster'] = poster.id
            else:
                print('提交人不存在')
                data['poster'] = 0

            timestamp = int(time.time())
            data['post_time'] = timestamp
            data['update_time'] = timestamp
            data['cur_groupinittime'] = timestamp

            bug = Bug.objects.using('db_bug_trace').create(**data)

            file = receive_file(request.FILES.get('attach', 'false'), timestamp)

            BugTrace.objects.using('db_bug_trace').create(
                bugid=bug.id,
                doer=bug.doer,
                poster=bug.poster,
                post_time=bug.post_time,
                attached=file,
                content=bug.content,
                cur_groupid=bug.cur_groupid,
                sync_dts=bug.sync_dts,
                dts_doer=bug.dts_doer,
                detail_version_id=bug.detail_version_id,
                label=bug.label,
            )
        else:
            print(bug_form.errors)

    return HttpResponse(json.dumps({'data': res}))

```  

```  
def upload_file(filename, file_upload_obj):
    try:
        ftp_server = '10.62.59.53'
        username = 'xwx620452'
        password = 'xq19921005....'
        ftp = FTP()
        ftp.connect(ftp_server, 21)
        ftp.login(username, password)

        remotepath = filename
        bufsize = 1024
        # fp = open(localpath, 'rb')
        ftp.storbinary('STOR ' + remotepath, file_upload_obj, bufsize)
        # fp.close()
        ftp.quit()
    except Exception as MSG:
        print('上传失败:', MSG)
    # return localpath


def receive_file(file, timestamp):
    if file != 'false':
        file_name = str(timestamp) + '.file'
        # file_path = os.path.join(os.path.dirname(root_path), 'static', 'tmp', file_name)
        # with open(file_path, 'wb+') as destination:
        #     for chunk in file.chunks():
        #         destination.write(chunk)

        json_str = json.dumps([{"file": file_name, "title": file._name}])
        # Pool().apply_async(upload_file, (file_name, file))
        upload_file(file_name, file)
    return json_str
```
