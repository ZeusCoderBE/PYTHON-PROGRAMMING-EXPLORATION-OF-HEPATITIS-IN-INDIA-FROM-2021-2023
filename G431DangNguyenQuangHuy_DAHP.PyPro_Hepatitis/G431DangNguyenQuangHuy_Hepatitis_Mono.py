import pyttsx3 as DNQuangHuy31_py 
import speech_recognition as DNQuangHuy31_sr   
import G431DangNguyenQuangHuy_Hepatitis_UI_SimpleDialog as huy31_simpledialog
from tkinter import *
Mono = DNQuangHuy31_py.init()
def Mono_Speak(audio):
    voice = Mono.getProperty('voices')
    Mono.setProperty('voice', voice[1].id)
    Mono.say(audio)
    Mono.runAndWait()
    return "M.O.N.O: " + audio + "\n"
def Command():
    DNQuangHuy31_c = DNQuangHuy31_sr.Recognizer()
    with DNQuangHuy31_sr.Microphone() as DNQuangHuy31_source:
        str=Mono_Speak("Xin Chào Ngài Tôi là Trợ Lí Ảo. Tên Tôi Là Mono")
        str += Mono_Speak("Ngài có cần gì ạ?")
        str += Mono_Speak("Hãy nói đi ạ, Tôi đang lắng nghe")
        DNQuangHuy31_audio = DNQuangHuy31_c.record(DNQuangHuy31_source, duration=4)
    try:
        DNQuangHuy31_query = DNQuangHuy31_c.recognize_google(DNQuangHuy31_audio, language='vi')
        str = str + "\n" + "Boss Huy: " + DNQuangHuy31_query
    except:
        Mono_Speak("Xin lỗi Ngài, Tôi không nghe rõ được. Vui lòng nói lại hoặc gõ lệnh.")
        root = Tk()
        app = huy31_simpledialog.SimpleDialog(root)
        str =str + "\n" + "Boss Huy: "+ app.set_command() # Lấy giá trị lệnh nhập vào
    return str
