# coding=utf-8
import os
import urllib.request
import time
import signal
import json

filepaths = os.getcwd() + '/packages'
filelist = os.listdir(filepaths)

# 自定义超时异常


class TimeoutError(Exception):
    def __init__(self, msg):
        super(TimeoutError, self).__init__()
        self.msg = msg


def time_out(interval, callback):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("run func timeout")

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)       # interval秒后向进程发送SIGALRM信号
                result = func(*args, **kwargs)
                signal.alarm(0)              # 函数在规定时间执行完后关闭alarm闹钟
                return result
            except TimeoutError:
                print('time out')
        return wrapper
    return decorator


def timeout_callback(e):
    print(e.msg)


@time_out(2, timeout_callback)
def getRemoteFileSize(url, proxy=None):
    """ 通过content-length头获取远程文件大小
        url - 目标文件URL
        proxy - 代理  """
    opener = urllib.request.build_opener()
    if proxy:
        if url.lower().startswith('https://'):
            opener.add_handler(urllib.request.ProxyHandler({'https': proxy}))
        else:
            opener.add_handler(urllib.request.ProxyHandler({'http': proxy}))
    try:
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        response = opener.open(request)
        response.read()
    except Exception:
        return 0
    else:
        fileSize = dict(response.headers).get('Content-Length', 0)
        return int(fileSize)


@time_out(100, timeout_callback)
def downloadFile(i):  # i is file name
    print(i)
    print("Running")
    if i[0:2] != "cl":
        return
    log.write(i+'\n')
    
    with open(filepaths + '/' + i, 'r') as f:
        templine = f.readline()
        #print("Reading")
        text = json.loads(templine)
        try:
            CourseName = text['data']['courseName']
            #print(CourseName)
            for play in text['data']['lessonData']['fileList']:
                CreateDate = play['CreateTime']
                url = play['Playset'][0]['Url']
                print(url)
                log.write(url + '\n')
                storepath = "video/" + CourseName + CreateDate + ".mp4"
                print(storepath)
                
                if os.path.isfile(storepath):
                    if int(play['Size']) == os.path.getsize(storepath):
                        print("ignore", storepath)
                        continue
                    else:
                        print("same file but different size, local :", os.path.getsize(storepath)\
                            , "remote :", int(play['Size']))
                else:
                    print("Not included!!")
                urllib.request.urlretrieve(url, storepath)
                log.write("Save as " + storepath + '\n')
        except:
            return

with open("log.txt", "w") as log:
    for i in filelist:
        downloadFile(i)