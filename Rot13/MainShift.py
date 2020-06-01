from libs.FileManager import *
from libs.ShiftCipher import *
import os

def menu():
	os.system('clear')
	print("**** SHIFT CIPHER ****")

	print("What are you trying to do?\n")
	print("1) Encrypt")
	print("2) Decrypt")
	print("3) Encrypt from file")
	print("4) Decrypt from file")
	print("0) Exit")
	print("")

def encrypt():
	m = input("Write what you want to encrypt.\n")
	n = int(input("Shift:\n"))
	cs = ShiftCipher(n)
	e = cs.encrypt_m(m)
	os.system('clear')
	print("Plain Text: {}".format(m))
	print("Encrypted:  {}".format(e))
	print("Shift: {}".format(cs.shift))

def decrypt():
	m = input("Write what you want to decrypt.\n")
	n = int(input("Shift:\n"))
	cs = ShiftCipher(n)
	e = cs.decrypt_m(m)
	os.system('clear')
	print("Cipher Text: {}".format(m))
	print("Decrypted:   {}".format(e))
	print("Shift: 3")

def encryptffile():
	s = input("Name of source file\n")
	t = input("Name of target file\n")
	file = FileManager(s,t)
	n = int(input("Shift:\n"))
	cs = ShiftCipher(n)
	e = cs.encrypt_m(file.getText())
	file.createFile(e)
	print("Please check \"{}\"".format(t))

def decryptffile():
	s = input("Name of source file\n")
	t = input("Name of target file\n")
	file = FileManager(s,t)
	n = int(input("Shift:\n"))
	cs = ShiftCipher(n)
	e = cs.decrypt_m(file.getText())
	file.createFile(e)
	print("Please check \"{}\"".format(t))

while True:
	menu()
 
	opt = input()
 
	if opt == "1":
		encrypt()
		input("\nPress key to continue")
	elif opt == "2":
		decrypt()
		input("\nPress key to continue")
	elif opt == "3":
		encryptffile()
		input("\nPress key to continue")
	elif opt == "4":
		decryptffile()
		input("\nPress key to continue")
	elif opt== "0":
		print ("Exiting ...")
		break
	else:
		print ("")
		input("Not a valid option, press key to continue")


