class CQueue:

    def __init__(self):
        self.A = []
        self.B = []


    def appendTail(self, value: int) -> None:
        self.A.append(value)


    def deleteHead(self) -> int:
        if not self.A and not self.B:
            return None
        if self.B:
            return self.B.pop()
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()