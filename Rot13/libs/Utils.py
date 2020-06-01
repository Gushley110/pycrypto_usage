import os

def get_coprime(a):
	c = int.from_bytes(os.urandom(4),byteorder='big')
	while(gcd(a,c) != 1):
		c = int.from_bytes(os.urandom(4),byteorder='big')
	return c % a

def gcd(a,b):
	if(b == 0):
		return a
	else:
		return gcd(b, a % b)

def p_mod(a,m):
	if(a < 0):
		return m + (a % m)
	return a % m

def inverse_m(a,m):
	m0 = m
	x1 = 1
	x0 = 0
	while(a > 1):
		q  = a // m
		t  = m
		m  = a % m
		a  = t
		t  = x0
		x0 = x1 - q * x0
		x1 = t
	if(x1 < 0):
		x1 += m0

	return x1

def inverse_a(a,m):
	return (m - a) % m


