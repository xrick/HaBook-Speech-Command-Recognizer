import speech_recognition as sr
import pyaudio
# obtain audio from the microphone
from CommandConverters import commandparser
r = sr.Recognizer()
r.energy_threshold = 450 #設定多大能量上才會持續收聽
#r.dynamic_energy_threshold = False
audio = None
with sr.Microphone() as source:
    print("current energy is {}".format(r.energy_threshold))
    #print("current threshold is {}".format(r.threshold))
    print("Say something!")
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source,timeout=2)
try:
    #print("Sphinx thinks you said " + str(r.recognize_sphinx(audio,language="zh-CN",grammar='speechcommand')))  # grammar='speechcommand.fsg'
    #raw_recog_str = str(r.recognize_sphinx(audio,language="zh-CN",grammar='speechcommand'))
    #print("raw recognized string:"+str(r.recognize_sphinx(audio,language="zh-CN",grammar='speechcommand')))
    commandparser.Sent2Command(str(r.recognize_sphinx(audio,language="zh-CN",grammar='speechcommand2')))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
