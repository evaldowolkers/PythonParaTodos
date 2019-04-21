class MinhaString(str):
    def __add__(self, other):
        print("self:", self)
        print("other:", other)
        return f"{self} {other}"

s1 = MinhaString("Curso Python para")
s2 = "Todos"

s3 = s1 + s2
print(s3)