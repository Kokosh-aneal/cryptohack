
from sympy import *

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161





def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

# Determines if n is a quadratic residue of an 
# odd prime p by using Euler's criterion.
def is_quadratic_residue(n, p):
	if n % p == 0:
		return True
	return pow(n, (p - 1)//2, p) == 1
    
# Given an odd prime p and an integer n
# This is an algorithm to find a mod-p square root of n when possible
# Can delete all the print statements once its working.
def tonelli_shanks(p, n):
	# Case when p|n, so n=0(mod p). The square root of 0 is 0. 
	if n % p == 0:
		return 0

	# So we can assume n is coprime to p, i.e. p does not divide n.
	# Use Euler's criteria to see if a solution exists or not
	if not is_quadratic_residue(n, p):
		print("This value of n is not a quadratic residue.")
		return None
	else:
		print("This value of n is a quadratic residue.")

	# If p=3(mod 4) and we know n is a quadratic residue then 
	# we can solve x^2=n(mod p) directly
	if p % 4 == 3:
		return pow(n, (p + 1)//4, p)
	
	# So now p=1(mod 4), (although this is not needed in the algorithm).
	# Write p - 1 = (2^S)(Q) where Q is odd
	Q = p - 1
	S = 0
	while Q % 2 == 0:
		S += 1
		Q //= 2
	print("Q=", Q)
	print("S=", S)

	# Find a quadratic non-residue of p by brute force search
	z = 2
	while is_quadratic_residue(z, p):
		z += 1
	print("z=", z)

	# Initialize variables
	M = S
	c = pow(z, Q, p)
	t = pow(n, Q, p)
	R = pow(n, (Q + 1)//2, p)

	print("M=", M)
	print("c=", c)
	print("t=", t)
	print("R=", R)
	
	while t != 1:
		print("LOOP")

		# Calculate i
		i = 0
		temp = t 
		while temp != 1:
			i += 1
			temp = (temp * temp) % p
		print("i=", i)
		
		# Calculate b, M, c, t, R
		pow2 = 2 ** (M - i - 1)
		b = pow(c, pow2, p)
		M = i
		c = (b * b) % p
		t = (t * b * b) % p
		R = (R * b) % p
		print("b=", b)
		print("M=", M)
		print("c=", c)
		print("t=", t)
		print("R=", R)

	# We have found a square root
	return R

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r




print(tonelli(a,p))
print(tonelli_shanks(p,a))
# print(sqrt_mod(a, p))