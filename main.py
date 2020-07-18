# coding=utf-8
import os
import urllib.request
import time
import signal
import json
import aria2



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
                print(url, name)
                urllist.append((url, name))
        except:
            return
    return urllist

def downloadFile(i, downpath):  # i is file name
    print(i)
    print("Running")
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
                print(CreateDate)
                url = play['Playset'][0]['Url']
                print(url)
                storepath = "/Users/tian/Downloads/video/" + CourseName + CreateDate + ".mp4" # 检查默认视频路径下是否有视频
                #print(os.listdir("~/Downloads/video/"))
                name = CourseName + CreateDate + ".mp4" # 文件名
                print(storepath)
                
                if os.path.isfile(downpath +'/'+ name):
                    if int(play['Size']) == os.path.getsize(storepath):
                        print("ignore", name)
                        continue
                    else:
                        print("same file but different size, local :", os.path.getsize(storepath)\
                            , "remote :", int(play['Size']))
                else:
                    print("Not included!!")
                print(url, name)
                aria2.aria2_download(url, name, downpath)
        except:
            return


def get_filelist(filepath="empty"):
    if filepath == "empty":
        filepaths = os.getcwd()
        filelist = os.listdir(filepaths)
        return filelist
    else:
        # print(filepath)
        filelist = os.listdir(filepath)
        # print(filelist)
        return filelist


if __name__ == '__main__':
    filepaths = os.getcwd() + '/packages'
    filelist = os.listdir(filepaths)
    with open("log.txt", "w") as log:
        for i in filelist:
            downloadFile(i)