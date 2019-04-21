class MinhaString(str):
    def __sub__(self, texto):
        print("self:", self)
        print("other:", texto)
        subtracao = self.replace(texto, '')
        return f"Resultado de '{self}' - '{texto}': {subtracao}"

    def __add__(self, other):
        print("self:", self)
        print("other:", other)
        return f"{self} + {other}"

s1 = MinhaString("Olá mundo cruel")
s2 = "cruel"

# Ao realizar a subtração s1 - s2, será removida a string s2 de dentro da string s1,
# utilizando o self.replace(s2, '')
s3 = s1 - s2
print(s3)