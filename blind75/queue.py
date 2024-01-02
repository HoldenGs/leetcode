class MyQueue:

    def __init__(self):
        self.inp = []
        self.out = []

    def push(self, x: int) -> None:
        self.inp.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out.pop()

    def peek(self) -> int:
        if len(self.out) == 0:
            while len(self.inp) > 0:
                self.out.append(self.inp.pop())
        return self.out[-1]

    def empty(self) -> bool:
        return self.inp == [] and self.out == []