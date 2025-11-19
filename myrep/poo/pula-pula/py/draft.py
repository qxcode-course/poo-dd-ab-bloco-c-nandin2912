class Kid:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f"{self.name}:{self.age}"


class Trampoline:
    def __init__(self):
        self.waiting = []
        self.playing = []

    def arrive(self, name, age):
        self.waiting.append(Kid(name, age)) 
    

    def enter(self):
        if self.waiting:
            self.playing.append(self.waiting.pop(0))

    def leave(self):
        if self.playing:
            self.waiting.append(self.playing.pop(0))

    def remove(self, name):
        for i, k in enumerate(self.waiting):
            if k.name == name:
                self.waiting.pop(i)
                return
        for i, k in enumerate(self.playing):
            if k.name == name:
                self.playing.pop(i)
                return
        print(f"fail: {name} nao esta no pula-pula")

    def show(self):
         w = "[" + ", ".join(str(k) for k in reversed(self.waiting)) + "]"
         p = "[" + ", ".join(str(k) for k in reversed(self.playing)) + "]"
         print(f"{w} => {p}")
    
        

import sys

tramp = Trampoline()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    print(f"${line}")
    args = line.split()

    if args[0] == "end":
        break
    elif args[0] == "show":
        tramp.show()
    elif args[0] == "arrive":
        tramp.arrive(args[1], args[2])
    elif args[0] == "enter":
        tramp.enter()
    elif args[0] == "leave":
        tramp.leave()
    elif args[0] == "remove":
        tramp.remove(args[1])
