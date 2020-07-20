import os
import os.path
def code2exe():
    cmd1 = '/Users/tian/opt/anaconda3/bin/pyinstaller --windowed --onefile --icon= --clean --noconfirm gui.py' #生成配置文件
    cmd2 = '/Users/tian/opt/anaconda3/bin/pyinstaller --clean --noconfirm --windowed --onefile gui.spec'
#对配置文件进行打包
    os.system(cmd1)
    os.system(cmd2)
 
if __name__ == "__main__":
    code2exe()