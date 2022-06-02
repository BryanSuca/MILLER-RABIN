
import random

# Exponenciación modular
# Devuelve (x^y) % z

def exponenciacionModular(x, y, z):
    r = 1
    while y > 0:
        if y % 2 != 0:
            r = (r * x) % z
        x = (x * x) % z
        y //= 2
    return r

# Ejecuta la prueba de primalidad miller-rabin t veces para n
def miillerRabin(n, t):
    
    # Encuentra los valores r y s tales que 2^s * r = n - 1
    r = (n - 1) / 2
    s = 1
    while r % 2 == 0:
        s += 1
        r /= 2

    #  Ejecuta el programa las veces que sea necesaria
    for i in range(t):
        a = random.randint(2, n - 1)
        y = exponenciacionModular(a, r, n)

        if y != 1 and y != n - 1:
            # Sigue elevando x al cuadrado 
            # comprobando que no hay j para el cual (a^r)^(2^j) = -1 (mod n)
            j = 0
            while j < s - 1 and y != n - 1:
                y = (y * y) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False

    return True

def randoms(d):
    #Genera un número aleatorio de max n bits
    a = random.getrandbits(d)
    if a % 2 == 0:
        a -= 1
    return a

if __name__ == '__main__':
    s = 10  # Número s de Miller-Rabin 
    bits1 = 16  # Numero de bits
    bits2 = 32
    bits3 = 64
    a1 = randoms(bits1); a2 = randoms(bits1); a3 = randoms(bits1); a4 = randoms(bits1); a5 = randoms(bits1)
    b1 = randoms(bits2); b2 = randoms(bits2); b3 = randoms(bits2); b4 = randoms(bits2); b5 = randoms(bits2)
    c1 = randoms(bits3); c2 = randoms(bits3); c3 = randoms(bits3); c4 = randoms(bits3); c5 = randoms(bits3)
    
    while not miillerRabin(a1, s):
        a1 = randoms(bits1)
    print(a1)
    while not miillerRabin(a2, s):
        a2 = randoms(bits1)
    print(a2)
    while not miillerRabin(a3, s):
        a3 = randoms(bits1)
    print(a3)
    while not miillerRabin(a4, s):
        a4 = randoms(bits1)
    print(a4)
    while not miillerRabin(a5, s):
        a5 = randoms(bits1)
    print(a5)

    while not miillerRabin(b1, s):
        b1 = randoms(bits2)
    print(b1)
    while not miillerRabin(b2, s):
        b2 = randoms(bits2)
    print(b2)
    while not miillerRabin(b3, s):
        b3 = randoms(bits2)
    print(b3)
    while not miillerRabin(b4, s):
        b4 = randoms(bits2)
    print(b4)
    while not miillerRabin(b5, s):
        b5 = randoms(bits2)
    print(b5)

    while not miillerRabin(c1, s):
        c1 = randoms(bits3)
    print(c1)
    while not miillerRabin(c2, s):
        c2 = randoms(bits3)
    print(c2)
    while not miillerRabin(c3, s):
        c3 = randoms(bits3)
    print(c3)
    while not miillerRabin(c4, s):
        c4 = randoms(bits3)
    print(c4)
    while not miillerRabin(c5, s):
        c5 = randoms(bits3)
    print(c5)
    
        
        
        
   
    
    
    
        
   

   