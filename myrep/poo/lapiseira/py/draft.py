class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def desgaste_por_folha(self):
        mapa = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return mapa[self.dureza]

    def __str__(self):
        return f"[{self.calibre}:{self.dureza}:{self.tamanho}]"


class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def insert(self, grafite: Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if not self.tambor:
            print("fail: nao existe grafite no tambor")
            return
        self.bico = self.tambor.pop(0)

    def remove(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None

    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return

        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = self.bico.desgaste_por_folha()

        if self.bico.tamanho - gasto < 10:
            self.bico.tamanho = 10
            print("fail: folha incompleta")
            return

        self.bico.tamanho -= gasto

    def __str__(self):
        bico = str(self.bico) if self.bico else "[]"
        tambor = "<" + "".join(str(g) for g in self.tambor) + ">"
        return f"calibre: {self.calibre}, bico: {bico}, tambor: {tambor}"


lap = None

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue

    args = line.split()
    cmd = args[0]

    print("$" + line)

    if cmd == "end":
        break

    if cmd == "init":
        lap = Lapiseira(float(args[1]))

    elif cmd == "show":
        print(lap)

    elif cmd == "insert":
        lap.insert(Grafite(float(args[1]), args[2], int(args[3])))

    elif cmd == "pull":
        lap.pull()

    elif cmd == "remove":
        lap.remove()

    elif cmd == "write":
        lap.write()
