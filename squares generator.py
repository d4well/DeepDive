class SquaresGen:
    def __init__(self, n):
        self.n = n
        self.index = 0

    def __iter__(self):
        return SquaresGen.squares(self.n)
    
    @staticmethod
    def squares(n):
        for i in range(n):
            yield i**2

sq1 = SquaresGen(10)
print(sq1)
print(list(sq1))