# coding=utf-8
import os
import urllib.request
import time
import signal
import json
import aria2
import sys


def get_path(filename):
    path = os.path.join(os.path.dirname(sys.argv[0]), fileName)
    return path

# 自定义超时异常

def get_urllist(i):
    urllist = []
    with open(i, 'r') as f:
        templine = f.readline()
        #print("Reading")
        text = json.loads(templine)
        try:
            CourseName = text['data']['courseName']
            #print(CourseName)
            for play in text['data']['lessonData']['fileList']:
                CreateDate = str(play['CreateTime']).replace(":", "-")
                url = play['Playset'][0]['Url']
                name = CourseName + CreateDate + ".mp4" # 文件名
                urllist.append((url, name))
        except:
            return
    return urllist

def downloadFile(i, downpath):  # i is file name
    if (downpath == ""):
        downpath = os.environ['HOME']+'/Downloads/video'
    if (i[0] == '.'):
        return
    with open(i, 'r') as f:
        templine = f.readline()
        #print("Reading")
        text = json.loads(templine)
        try:
            CourseName = text['data']['courseName']
            #print(CourseName)
            for play in text['data']['lessonData']['fileList']:

                CreateDate = str(play['CreateTime']).replace(":", "-")
                url = play['Playset'][0]['Url']
                storepath = "/Users/tian/Downloads/video/" + CourseName + CreateDate + ".mp4" # 检查默认视频路径下是否有视频
                #print(os.listdir("~/Downloads/video/"))
                name = CourseName + CreateDate + ".mp4" # 文件名     
                print(downpath + '/' + name)
                if os.path.isfile(downpath +'/'+ name):
                    if int(play['Size']) == os.path.getsize(storepath):
                        print('\t' + "ignore", name)
                        continue
                    else:
                        print("\tSame file but different size, local :", os.path.getsize(storepath)\
                            , "remote :", int(play['Size']))
                else:
                    print("\tNot included!!")
                print('\t', url, name, downpath)
                aria2.aria2_download(url, name, downpath)
        except:
            return


def get_filelist(filepath="empty"):
    if filepath == "empty":
        filepaths = os.path.dirname(sys.argv[0])
        filelist = os.listdir(filepaths)
        return filelist
    else:
        # print(filepath)
        filelist = os.listdir(filepath)
        filelist = [(time.ctime(os.path.getmtime(os.path.join(filepath, i))), i) for i in filelist]
        # print(filelist)
        return filelist


if __name__ == '__main__':
    filepaths =  os.path.dirname(sys.argv[0]) + '/packages'
    filelist = os.listdir(filepaths)
    with open("log.txt", "w") as log:
        for i in filelist:
            downloadFile(i)