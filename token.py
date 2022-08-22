import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

os.system("title [ZRZ-TOKEN] crée par ZRZ#0001")

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Fore.RED +Fore.RED +'[*] demarrage & Telechargement des modules... '+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

banner = (Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n"+ 
Fore.WHITE +Fore.RED +'''\n  
  ███████╗██████╗ ███████╗  ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
  ╚══███╔╝██╔══██╗╚══███╔╝  ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
    ███╔╝ ██████╔╝  ███╔╝█████╗██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
   ███╔╝  ██╔══██╗ ███╔╝ ╚════╝██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
  ███████╗██║  ██║███████╗     ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
  ╚══════╝╚═╝  ╚═╝╚══════╝     ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝\n\n'''+ Fore.RESET + Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n")

os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
print(Fore.WHITE +Fore.RED +"                                         Bienvenue dans "+Fore.WHITE+" ZRZ-TOKEN "+Fore.WHITE+"- 2022 -")
print(Fore.WHITE +Fore.RED +"                                         [1] "+Fore.WHITE+"Token Generateur(Rapide!)")
print(Fore.WHITE +Fore.RED +"                                         [2] "+Fore.WHITE+"Token Verificateur(verifie tous les token generer)")
print(Fore.WHITE +Fore.RED +"                                         [3] "+Fore.WHITE+"Credits")
print(Fore.WHITE +Fore.RED +"                                         [4] "+Fore.WHITE+"quitter")
print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
opcion = input("\nChoix: ")
if opcion=='1':
	os.system("cls")
	print(banner)
	cantidad = input("\nNombre de token a generer: ")
	while int(count)<int(cantidad):
		Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
		f.write(Generated+"\n")
		print(Fore.GREEN +"Token: "+ Fore.RESET + Generated)
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Fore.CYAN +Fore.RED +"Tokens generé avec succes !")
			print(Fore.WHITE +Fore.RED +"Tokens enregistré dans Generated.txt")
			input(Fore.RED +Fore.RED +"\nappui sur entrer pour quitter")
			os.system("cls")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			print(Fore.RED +Fore.RED +"                                                   fermeture!")
			print(Fore.GREEN +Fore.RED +"                                               Bonne journé :D")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			time.sleep(2)
			sys.exit()
			pass
	pass
if opcion=='2':
	os.system("cls")
	print("\n" + banner + "\n")
	with open('Generated.txt', 'r') as f:
	    for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{token}'  
	        }
	        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

	        try:
	            if src.status_code == 200:
	                print(f'{Fore.LIGHTGREEN_EX}Valid token! >{Fore.RESET} ' + token)
	            else:
	                print(f'{Fore.RED}Invalid token >{Fore.RESET} ' + token)
	        except Exception:
	            print(f"{Fore.CYAN}Error, please contact with ZRZ#0001 {Fore.RESET}")
pass
if opcion=='3':
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"________________________________________________________________________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.WHITE +Fore.RED +"                                         ZRZ-TOKEN"+Fore.WHITE+" Made by "+Fore.RED+"ZRZ#0001")
	print(Fore.WHITE +Fore.RED +"                                         [Discord] "+Fore.RED+"ZRZ#0001")
	print(Fore.WHITE +Fore.RED +"                                         [Server] "+Fore.RED+"https://discord.gg/bjEgarGt")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"________________________________________________________________________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	input(Fore.RED +Fore.RED +"\nEnter to exit")
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"________________________________________________________________________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.RED +Fore.RED +"                                                   Closing!")
	print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"________________________________________________________________________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass
if opcion=='4':
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.RED +Fore.RED +"                                                   Closing!")
	print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"____________________________________________________________"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass