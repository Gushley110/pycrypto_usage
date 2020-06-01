from libs.Utils import *

class ShiftCipher:

	alphabet = [chr(i) for i in range(97,123)]
	#alphabet = [chr(i) for i in range(127)]

	def __init__(self,shift):
		self.shift = shift % len(self.alphabet)
		self.mod   = len(self.alphabet)

	def encrypt(self,a):
		if a == ' ':	## Comment this if statement if you are using complete ascii
			return ' '
		a = a.lower()
		p = self.alphabet.index(a)
		c = p_mod(p + self.shift,self.mod)
		return self.alphabet[c].upper()

	def decrypt(self,c):
		if c == ' ':	## Comment this if statement if you are using complete ascii
			return ' '
		c = c.lower()
		p = self.alphabet.index(c)
		i = inverse_a(self.shift,self.mod)
		a = p_mod(p + i,self.mod)
		return self.alphabet[a].lower()

	def encrypt_m(self,message):
		m = list(message)
		c = list()
		for a in m:
			c.append(self.encrypt(a))
		return "".join(c)

	def decrypt_m(self,message):
		m = list(message)
		c = list()
		for a in m:
			c.append(self.decrypt(a))
		return "".join(c)





