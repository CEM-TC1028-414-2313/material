a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

for n in range(a,b+1):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)