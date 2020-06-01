from libs.Utils import *

class AffineCipher:

	alphabet = [chr(i) for i in range(97,123)]
	#alphabet = [chr(i) for i in range(127)]

	def __init__(self,a,b):
		self.a   = a % len(self.alphabet)
		self.b   = b % len(self.alphabet)
		self.mod = len(self.alphabet)
		if(gcd(a,len(self.alphabet)) != 1):
			raise Exception

	def encrypt(self,a):
		if a == ' ':	## Comment this if statement if you are using complete ascii
			return ' '
		a = a.lower()
		p = self.alphabet.index(a)
		c = ((self.a * p) + self.b) % self.mod
		return self.alphabet[c].upper()

	def decrypt(self,c):
		if c == ' ':	## Comment this if statement if you are using complete ascii
			return ' '
		c = c.lower()
		p = self.alphabet.index(c)
		i = inverse_a(self.b,self.mod)
		q = inverse_m(self.a,self.mod)
		a = (q * (p + i)) % self.mod
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
		