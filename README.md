Classin-VideoDownload
==========

事情的起因是`Classin`的视频播放页面非常令人恼火, 无法精确地调整播放速度, 播放窗口周围有其他元素干扰....

通过`Charles`, `Surge`, `Fiddler`等软件抓包口后, 将response文件存储即可自动提取出所有的视频下载链接, 并自动命名.

使用
---------
1. 使用`Charles`等软件抓包, 得到`json`的`response`
2. 打开该软件, 点击`Open Folder`进入json所在的列表, 点击需要的`json`文件, 即可生成对应`url`列表, 点击`Download Selected`可以调用`Aria2`下载, 前提是后台运行有`Aria2`.
3. 该软件对于批量下载(如期末复习时批量下载课程视频)有明显的效率提升, 如果仅仅下载单个视频, 直接抓包后下载对应`url`更快.