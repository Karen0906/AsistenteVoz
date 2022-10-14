import speech_recognition as sr
import subprocess
import sys
import time
import traceback
import os
# import signal

try:
    r = sr.Recognizer()
    filename = "stream.wav"
    p = subprocess.Popen([sys.executable, "VoiceRecorder.py"]) 
    time.sleep(4)
    stream = sr.AudioFile(filename)
    antText = ''
    finalText = ''

    while True:
        print('Procesando audio...',end='')
        with stream as source:
            # r.adjust_for_ambient_noise(source)
            audio = r.record(stream)
        try:
            text = r.recognize_google(audio,language='es-MX')
            if antText != text:
                print(' Siga hablando...')
                antText = text
            else:
                # finalText += " " + text
                # print(finalText)
                print('')
                print(text)
                antText = ''
                p.terminate()
                p.wait()
                # os.rename(filename,text+'.wav')
                os.remove(filename)
                p = subprocess.Popen([sys.executable, "VoiceRecorder.py"]) 
                time.sleep(4)
        except sr.UnknownValueError:
            print('')
            print('Esperando dictado...')
            p.terminate()
            p.wait()
            os.remove(filename)
            p = subprocess.Popen([sys.executable, "VoiceRecorder.py"]) 
            time.sleep(4)
        except sr.RequestError as e:
            print('')
            print('Problema de conexión...')
            p.terminate()
            p.wait()
            os.remove(filename)
            p = subprocess.Popen([sys.executable, "VoiceRecorder.py"]) 
            time.sleep(4)
except KeyboardInterrupt:
    p.terminate()
    print('Procesos terminados...')
except Exception as e:
    p.terminate()
    print(e)
    traceback.print_exc()
finally:
    dp = subprocess.Popen([sys.executable,'Delete_all.py'])