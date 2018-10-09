Texto1 = "Olá"
Texto2 = "Mundo"
Texto3 = Texto1.center(10)
Texto4 = Texto2.center(10)
print(Texto3 + '\n' + Texto4)
Texto3 = Texto1.center(10, '-')
Texto4 = Texto2.center(10, '-')
print(Texto3 + '\n' + Texto4)
Texto3 = Texto1.ljust(5)
print(f"*{Texto3}*\n*{Texto2}*")
Texto3 = Texto1.rjust(5)
print(f"*{Texto3}*\n*{Texto2}*")