import socket
import threading
import time
import json
import select
from tkinter import *

user_name = "JOHN"
win_count = 0
window_width = 470
window_height = 550

#GLOBAL VARIABLES
main_window = Tk()
questionLabelVar = StringVar()
wincountLabelVar = StringVar()


def listen_server(delay):
        while True:
                message = comms_socket.recv(4096).decode("UTF-8")
                print(message) 
                time.sleep(1)

def send_func(message):
        outbound_message = "{\"name\":\"" + user_name + "\",\"answer\": " + message + "}"
        print (outbound_message)
        comms_socket.send(bytes(outbound_message, "UTF-8"))

#def mainApp():
#        global win_count
#        global questionLabelVar
#        global wincountLabelVar

#        message = comms_socket.recv(4096).decode("UTF-8")
#        print(message) 
#        data = json.loads(message)
#
#        if (data["winner"] == user_name):
#                win_count += 1       
#
#        mystring = str(data["question"])
#        questionLabelVar.set(mystring)
#        wincountLabelVar.set("You have won " + str(win_count) + " times")
#        time.sleep(1)
#        main_window.after(1000, mainApp)

print("Running Application")
comms_socket = socket.socket()
host = '192.168.86.11'
port = 8081
comms_socket.connect((host, port))
comms_socket.setblocking(1)
#receive_thread = threading.Thread(target = listen_server, args=(1,))
#receive_thread.start()


main_window.title("Math Game")
#main_window.withdraw()
#main_window.deiconify()
main_window.resizable(width = False, height = False)
main_window.configure(width = window_width, height = window_height)

questionLabelVar.set("waiting for server...")
questionLabel = Label(main_window, text = questionLabelVar.get(), font = "100")
questionLabel.place(relwidth = 1, y = 20)

wincountLabelVar.set("You have won 0 times")
wincountLabel = Label(main_window, text = wincountLabelVar.get(), font = "100")
wincountLabel.place(relwidth = 1)



#BUTTON SETTINGS
numpadVerticalOffset = 100
numpadButtonHeight = 50
numpadButtonFont = "14"
numpadButtonWidth = window_width / 3

button1 = Button(main_window, font = numpadButtonFont, text = "1", command = lambda : send_func("1"))
button1.place(x = 0, y = numpadVerticalOffset, width = numpadButtonWidth, height = numpadButtonHeight)

button2 = Button(main_window, font = numpadButtonFont, text = "2", command = lambda : send_func("2"))
button2.place(x = numpadButtonWidth, y = numpadVerticalOffset, width = numpadButtonWidth, height = numpadButtonHeight)

button3 = Button(main_window, font = numpadButtonFont, text = "3", command = lambda : send_func("3"))
button3.place(x = (numpadButtonWidth*2), y = numpadVerticalOffset, width = numpadButtonWidth, height = numpadButtonHeight)

button4 = Button(main_window, font = numpadButtonFont, text = "4", command = lambda : send_func("4"))
button4.place(x = 0, y = numpadVerticalOffset + numpadButtonHeight, width = numpadButtonWidth, height = numpadButtonHeight)

button5 = Button(main_window, font = numpadButtonFont, text = "5", command = lambda : send_func("5"))
button5.place(x = numpadButtonWidth, y = numpadVerticalOffset + numpadButtonHeight, width = numpadButtonWidth, height = numpadButtonHeight)

button6 = Button(main_window, font = numpadButtonFont, text = "6", command = lambda : send_func("6"))
button6.place(x = (numpadButtonWidth*2), y = numpadVerticalOffset + numpadButtonHeight, width = numpadButtonWidth, height = numpadButtonHeight)

button7 = Button(main_window, font = numpadButtonFont, text = "7", command = lambda : send_func("7"))
button7.place(x = 0, y = numpadVerticalOffset + (numpadButtonHeight*2), width = numpadButtonWidth, height = numpadButtonHeight)

button8 = Button(main_window, font = numpadButtonFont, text = "8", command = lambda : send_func("8"))
button8.place(x = numpadButtonWidth, y = numpadVerticalOffset + (numpadButtonHeight*2), width = numpadButtonWidth, height = numpadButtonHeight)

button9 = Button(main_window, font = numpadButtonFont, text = "9", command = lambda : send_func("9"))
button9.place(x = (numpadButtonWidth*2), y = numpadVerticalOffset + (numpadButtonHeight*2), width = numpadButtonWidth, height = numpadButtonHeight)

button0 = Button(main_window, font = numpadButtonFont, text = "0", command = lambda : send_func("0"))
button0.place(x = numpadButtonWidth, y = numpadVerticalOffset + (numpadButtonHeight*3), width = numpadButtonWidth, height = numpadButtonHeight)

#main_window.after(1000, mainApp)
main_window.mainloop()
#while True:
#        main_window.mainloop()






