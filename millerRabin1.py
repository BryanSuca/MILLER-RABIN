import random
 
# exponenciación modular.
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
            # Sigue elevando y al cuadrado
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
 
if __name__ == '__main__':
    s = 10; # Número s de Miller-Rabin
    print("Primos de 3, 4 y 5 cifras ");
    for n in range(100,100000):
        if (miillerRabin(n, s)):
            print(n , end=" ");
