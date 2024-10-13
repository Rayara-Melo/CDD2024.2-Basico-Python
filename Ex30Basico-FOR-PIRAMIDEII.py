#
numero = int(input(" digite um numero: "))
for i in range(0,11,numero+1):
    for x in range(i+1):
        print(x, end = " ")
    print()