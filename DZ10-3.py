class Cell:
    def __init__(self, number_of_cells):
        self.cells = int(number_of_cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            raise ValueError('Нельзя вычитать из меньшего большее')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_row):
        result = []
        if self.cells <= int(cells_row):
            return f'{"*" * self.cells}'
        elif self.cells > int(cells_row):
            for i in range(self.cells // cells_row):
                result.append('*' * int(cells_row))
            result.append('*' * (self.cells % cells_row))
            return '\n'.join(result)


a = Cell(15)
b = Cell(7)
new_cell = a + b
print((a+b).cells)
print((a*b).cells)
print((a//b).cells)
print(new_cell.make_order(5))
