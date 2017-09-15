from random import randint
from fractions import gcd
from array import array

def selectPrime():
	primeNumbers = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
					173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
					251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
					337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
					421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
					503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
					601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677,
					683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
					787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
					881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
					983, 991, 997]
	length = len(primeNumbers)
	index = randint(0, length - 1)
	return primeNumbers[index]

def pick_e(n, phi):
	while (True):
		e = randint(3, phi - 1)
		if (gcd(e, n) == 1 and gcd(e, phi) == 1):
			return e

def compute_d(e, phi):
	L1, L2 = phi, e
	R1, R2 = phi, 1

	while(True):
		R3 = R1 - int(L1/L2) * R2
		if (R3 < 0):
			R3 = R3 % phi

		L3 = L1 % L2

		if (L3 == 1):
			return R3
		else:
			L1 = L2;
			L2 = L3;
			R1 = R2;
			R2 = R3;

def encrypt(m, e, n):
    cipher = []
    for i in range(len(m)):
        c = m[i]**e % n
        cipher.append(c)
    return cipher

def decrypt(encryptedNum, d, n):
    original = []
    for i in range(len(encryptedNum)):
        decryptedNum = encryptedNum[i]**d%n
        original.append(decryptedNum)
    return original

# Set-Up begins...
p = selectPrime()
q = selectPrime()
while(q == p):
	q = selectPrime()

n = p * q
totient = (p - 1) * (q - 1)
e = pick_e(n, totient)
d = compute_d(e, totient)
# Set-Up ends...

print("Your encryption key (e, n) is: (", e,",",n,")")

message = input("Enter your message below:\n\t")

coded_message = [] #This array store the number representation of each char
for i in range(len(message)):
	coded_message.append(ord(message[i]))

print("\nOriginal message:\n\t", message, "\n")
print("Original message in code:\n\t", *coded_message, "\n")

cipher_num = encrypt(coded_message, e, n)
print("Encrypted message in code:\n\t", *cipher_num, '\n')
#encryptedText = []
#for i in range(len(cipher_num)):
#    encryptedText.append(chr(cipher_num[i]))\

#print("Encrypted message:\n\t", *encryptedText, sep = '')

print("Your decryption key (d, n) is: (", d,",",n,")")
print("Please share your decryption key with your DESIRED RECEIVER ONLY!")

#	The following code is used to check decrypt function's funtionality

#origin_code = decrypt(cipher_num, d, n)
#print("Original coded message:\n", *origin_code, '\n')
#msg = []
#for i in range(len(origin_code)):
#	msg.append(chr(origin_code[i]))
        
#print("Message:")
#print(*msg, sep = '')
