import time
import os

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("[green]Starting", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        time.sleep(0.0002)
        
        
        
with Progress() as progress:

    task1 = progress.add_task("[green]Cheking versions..", total=1000)

    while not progress.finished:
        progress.update(task1, advance=7)
        time.sleep(0.002)
os.system('clr || clear')
import os
try:
 import cryptocode
except:
    os.system('pip install cryptocode')
    os.system('clr || clear')
    import cryptocode
import os
#decoded - декодированный encoded - закодированный
from random import *
try:
 from rich import print
except:
    os.system('pip install rich')
    os.system('clr || clear')
from secrets import *


invalid = []
key = ''
def gen(lkey):
    key = token_hex(lkey)
    print('Your key:', key)
    
    
    
    
def genb(lkey):
   text = input('>')
   while 1:
    key = token_hex(lkey)
    if key not in invalid:
        decoded = cryptocode.decrypt(text, key)
        if decoded != False:
            print('Finded\nText:', decoded, "\nkey:\n",key)
            print('all using keys:', invalid, 'keys were used',len(invalid))
            quit()
        else:
            invalid.append(key)
            print(key)
            continue
        
    





def brute():
 class MyThread():
  print('''selct mode:
      [1] easy mod for easy keys
      [2] good mod for hard keys''')
  mode = int(input('[mode]-->  '))
  if mode == 1:
      length = int(input('max lenght key:'))
      text = input('encoded text:')
      print('Enter standart to use standard characters, or enter your own characters')
      chars = input('-->')
      if chars == 'standard':
       chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"*:;()/?!$~[]'
      else:
         pass
      key = ''
      invalid = []
      while 1:
       for i in range(length):
        key += choice(chars)
       if key not in invalid:
        decoded = cryptocode.decrypt(text, key)
        if decoded != False:
                    print('Finded\nText:', decoded, "\nkey:\n",key)
                    print('all using keys:', invalid, 'keys were used',len(invalid))
                    quit()
        else:
                    print(key)
                    invalid.append(key)
                    key = ''
                    
                    
                    
                    
                    
  elif mode == 2:
        length = int(input('[Length key in bytes]-->  '))
        key = ''
        invalid = []
        while 1:
            genb(length)
            quit()
        
 thread1 = myThread("Thread", 1)
 thread2 = myThread("Thread", 2)
 thread1 = myThread("Thread", 3)
 thread2 = myThread("Thread", 4)

 thread1.start()
 thread2.start()
 thread3.start()








def encoding():
        key = input('Input your key for encoding and decoding\nfor generate random key input r\n>>')
        if key == 'r':
            lkey = int(input('[Length key in bytes]-->  '))
        else:
                pass
        print('Input text for encode:')
        text = input('>>')
        encoded = cryptocode.encrypt(text, key)
        print('encoded:\n', encoded)
        decoded = cryptocode.decrypt(encoded, key)
        print('decoded:\n', decoded)
        
        
        
        
        
def decoding():
        key = input('Input your key for decoding:\n>>')
        text = input('Input encoded text:\n>>')
        decoded = cryptocode.decrypt(text, key)
        if decoded == False:
            print('Invalid encoded text or key')
        else:
            print('Your text:', decoded)







mods = """
version 0.5
by C404
Inst: The361_

•-----------------------------------------•
|Mods:                                    |
|   [1] – encoding                        |
|   [2] – decoding                        |
|   [3] - brute key                       |
|                                         |
|                                         |
•-----------------------------------------•
"""
logo = """

░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░░░██╗
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝╚██╗░██╔╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░░╚████╔╝
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░░░╚██╔╝░░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░░░░██║░░░
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░
"""
print(logo)
print(mods)
mode = input('[$]-->  ')
if mode == '1':
    encoding()
elif mode == '2':
    decoding()
elif mode == '3':
    brute()