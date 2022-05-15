import random
import webbrowser
import keyboard
import time
print("press space!") 
def func(key):
    site_txt_location=""
    if key =="space":
        file = open(site_txt_location,"r")
        webbrowser.open(random.choice(file.readlines()))
        time.sleep(1)
        return func(keyboard.read_key())
        file.close()
    else:
        print("wcisnij spacje!")
        return func(keyboard.read_key())

func(keyboard.read_key())
 
