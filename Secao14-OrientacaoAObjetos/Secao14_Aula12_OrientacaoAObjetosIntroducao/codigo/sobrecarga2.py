class MinhaString(str):
    def __sub__(self, other):
        print("self:", self)
        print("other:", other)
        subtracao = self.replace(other, '')
        return f"Resultado de '{self}' - '{other}': {subtracao}"

    def __add__(self, other):
        print("self:", self)
        print("other:", other)
        return f"{self} + {other}"


s1 = MinhaString("Curso Python para")
s2 = "Todos"

# Ao realizar a soma s1 + s2, será retornado o texto "s1 + s2" literalmente.
s3 = s1 + s2
print(s3)