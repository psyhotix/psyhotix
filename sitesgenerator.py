import random
import webbrowser
import keyboard
import time
print("wcisnij spacje!") 
def funkcja(klawisz):
 
    if klawisz =="space":
        plik = open(r"C:\Users\Dawid\Desktop\projekty python\randomsitegenerator\sites.txt","r")
        webbrowser.open(random.choice(plik.readlines()))
        time.sleep(1)
        return funkcja(keyboard.read_key())
        plik.close()
    else:
        print("wcisnij spacje!")
        return funkcja(keyboard.read_key())

funkcja(keyboard.read_key())
 