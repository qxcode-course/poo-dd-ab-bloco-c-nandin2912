class Person:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return self.name

class Market:
    def __init__(self, counter_size: int):
        self.counter = [None for _ in range(counter_size)]
        self.waiting = []
    def __str__(self):
        caixas = ", ".join("-----" if x is None else str(x) for x in self.counter)
        espera = ", ".join(str(x) for x in self.waiting)
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    def arrive(self, person):
        self.waiting.append(person)
    def call(self, index: int):
        if index < 0 or index >= len(self.counter):
            print("fail: caixa inexistente")
            return
        if not self.waiting:
            print("fail: sem clientes")
            return
        if self.counter[index] is not None:
            print("fail: caixa ocupado")
            return
        self.counter[index] = self.waiting.pop(0)
    def finish(self, index: int):
        if index < 0 or index >= len(self.counter):
            print("fail: caixa inexistente")
            return
        if self.counter[index] is None:
            print("fail: caixa vazio")
            return
        self.counter[index] = None

def main():
    market = None
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue
        print(f"${line}")
        args = line.split()
        cmd = args[0]
        if cmd == "init":
            market = Market(int(args[1]))
        elif cmd == "show":
            if market: print(market)
        elif cmd == "arrive":
            if market: market.arrive(Person(args[1]))
        elif cmd == "call":
            if market: market.call(int(args[1]))
        elif cmd == "finish":
            if market: market.finish(int(args[1]))
        elif cmd == "end":
            break

if __name__ == "__main__":
    main()
