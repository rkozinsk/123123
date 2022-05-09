class Kalkulator:

    def __init__(self) -> object:
        self.operacje = []

    def wypisz_wymaluj(self):
        print(self.operacje)

    def add(self, num1, num2):
        result = num1 + num2
        self.operacje.append(f"added {num1} to {num2} got {result}")
        return result

    def minus(self, num1, num2):
        result = num1 - num2
        self.operacje.append(f"added {num1} to {num2} got {result}")
        return result

    def razy (self, num1, num2):
        result = num1 * num2
        self.operacje.append(f"added {num1} to {num2} got {result}")
        return result



k = Kalkulator()
w = k.add(5,18)
print("wynik dodawania", w)

k = Kalkulator()
w = k.minus(5,18)
print("wynik minus", w)

k = Kalkulator()
w = k.razy(5,18)
print("wynik razuy", w)