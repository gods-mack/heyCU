from tkinter import *
import batcheet
import voice
#import Tkinter

def receive(ques):
  answer = batcheet.get_answer(ques)
  msg_list.insert(END, answer)

def receiveVoice(ques):
  answer = batcheet.get_answer(ques)
  voice.speak(answer)
  msg_list.insert(END, answer)
  
  
def send():
 ques =  my_msg.get()
 #newques = "      "+ques
 #msg_list.insert(END,newques)
 my_msg.set("") 
 receive(ques)

def voice_mode():
  ques  = batcheet.text2Voice()
  my_msg.set(ques)
  my_msg.set("")
  receiveVoice(ques)
  



top =  Tk()
top.title("Donna__")
top.configure(bg="teal")
top.geometry("350x350")

messages_frame = Frame(top)
messages_frame.config(bg="teal")
my_msg = StringVar()  # For the messages to be sent.
my_msg.set("type")
scrollbar = Scrollbar(messages_frame)  # To navigate through past messages.

msg_list = Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set,background="#E0E2FF")
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

messages_frame.pack()

entry_field = Entry(top, textvariable=my_msg,bg="#8CA7C7")
entry_field.bind("<Return>",send)
entry_field.pack()
send_button = Button(top, text="Send",command=send)
send_button.pack()
#send_button.place(x=750,y=270)
voice_mode = Button(top,text="Voice",command=voice_mode)
voice_mode.pack()

top.protocol("WM_DELETE_WINDOW")

top.mainloop()
