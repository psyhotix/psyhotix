import random
import webbrowser
import keyboard
import time
print("wcisnij spacje!") 
def funkcja(klawisz):
    site_txt_location=""
    if klawisz =="space":
        plik = open(site_txt_location,"r")
        webbrowser.open(random.choice(plik.readlines()))
        time.sleep(1)
        return funkcja(keyboard.read_key())
        plik.close()
    else:
        print("wcisnij spacje!")
        return funkcja(keyboard.read_key())

funkcja(keyboard.read_key())
 
