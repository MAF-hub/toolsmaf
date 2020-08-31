#!/src/env/ python3
# -*- coding: utf-8 -*-
import sys, os, webbrowser, platform
from time import sleep
from sys import stdout, exit
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
##Def funciones
def limpiar():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def logo():
      print '''        
       {0}    ``      {2}T O O L S{0}      ``            
          -h-`                        -           
          dMMy     `::`     ```      :N-          
         `MMMm`.:+shMNy+-./ohNd+:.` /NM/          
         .MMMmdNMMMMMMMh/-yMMMMMMNdsyMM+          
         `NMM+yMMMMMMMm/+o:dMMMMMMMNoNM+          
          yMm`-dNMNNmNNMMMMdhmNMMMm/`dM+          
          +MN-``:++/oNMMMMMMh/+oo/-``hM/          
          `dMm/::hmNMMNMMMMMMNmho-../hm`          
         ` /MMMMNmMMMmdmmmmmNMMNNNmmMM: `         
    `-+ydmo.dMMMMMMmhy/---:ohdNMMMMMMm:hmhs/-     
./shmNMMMMMd+dMMMMMms-.-.-..:hmMMMMMddNMMMMMNdy+: 
:hNMMMMMMMMMNNMMNMMNo-.-----/dNMNNMMNMMMMMMMMMMNs 
 -sMMMMMmyys+dMMNmMNNhyo+oydNmhNmNNMsoyyyNMMMMN+` 
  :dNs::o.`:dNMMNNmNmhhyyhyyydmNNMMMNy.`:o:/hMo-  
   +do-.ym+NMMMMd.`:mNmmddmNNs.`/MMMMMhsN/`/hh.   
    -ddmMMNNMMMMM/ :hMMMMMMMNs. hMMMMMdMMNdds     
     ..yMMMMMMMMd+ -mMMMdNMMMs``yNMMMMMMMM-.      
       .mMMMdy/.   {2}MERETEC AND FLYEAD{1}{0}   `-ohNMMMs`       
       `+y+.           ```           `-sy:                             
       {3}SOLO MUESTRA LOS TOOLS MAS INTERESANTES 
  Este script esta hecho con fines eduacativos{2} '''.format(GREEN, END, CYAN, RED)

logo()
sleep(0.7)
limpiar()
sleep(0.3)
logo()
sleep(0.3)
limpiar()
sleep(0.3)
logo()
sleep(0.3)
limpiar()
sleep(0.3)
logo()
sleep(1.5)
for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{3}*{0}]{2}BANNER ERROR404 Preparando el Script... %d%%".format(GREEN, END, CYAN, RED, WHITE) % i)
        stdout.flush()
limpiar()

def menuc():
    print '''
{3}*{1}{0} Este Script esta hecho con la Colaboracion de MERETEC AND FLYEAD
                Esperamos que les sea util{1} {3}MAF{0}'''.format(GREEN, END, CYAN, RED, WHITE)

def menu():
    print '''
      {3}1.{1} {2} PENTESTING
      {3}2.{1} {2} GENERAR PAYLOAD								
      {3}3.{1} {2} BUSCADORES DE LA DEEP WEB										
      {3}4.{1} {2} PHISHING 											
      {3}5.{1} {2} FUERZA BRUTA												
      {3}6.{1} {2} IP GEOLOCALIZADOR								
      {3}7.{1} {2} Youtube MAF					
      {3}8.{1} {2} Salir						
				'''.format(GREEN, END, CYAN, RED)
limpiar()
menuc()
menu()
d = raw_input('\033[1;32m TOOLS MAF > \033[0m')

if d == "":
	print("Ha seleccionado un numero")
elif d == "1":
  os.system("git clone https://github.com/Hackplayers/evil-winrm")
elif d == "2":
	os.system("git clone https://github.com/nccgroup/Winpayloads")
elif d == "3":
      print """
    NOT EVIL:
      http://hss3uro2hsxfogfq.onion/
    AHMIA:
      http://msydqstlz2kzerdg.onion/
    TORCH:
      http://xmh57jrzrnw6insl.onion/
    HAYSTAK:
      http://haystakvxad7wbk5.onion/
    DUCKDUCKGO:
      https://3g2upl4pq6kufc4m.onion/
    SEARX:
      http://5plvrsgydwy2sgce.onion/      
  """
  
elif d == "4":
	os.system(" git clone https://github.com/htr-tech/zphisher")
elif d == "5":
	os.system("git clone https://github.com/Ha3MrX/InstaBrute")	
elif d == "6":
  os.system("git clone https://github.com/maxmind/GeoIP2-php")
elif d == "7":
	webbrowser.open('https://www.youtube.com/channel/UCplxfPaS6e5-ELl7zqjdPHg')  
elif d == "8":  
        limpiar()
	sys.exit()
else:
  print("No existe el comando en la base de datos")









