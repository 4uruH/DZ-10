class Matrix:
    def __init__(self, lst_of_lsts):
        self.matrix = lst_of_lsts

    def __str__(self):
        return '\n'.join([' '.join([f'{i}' for i in row]) for row in self.matrix])

    def __add__(self, other):
        m_out = []
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for row in range(len(self.matrix)):
                mat_el = []
                for column in range(len(self.matrix[row])):
                    mat_el.append(self.matrix[row][column] + other.matrix[row][column])
                m_out.append(mat_el)
        else:
            raise ValueError('нельзя складывать матрицы разного размера')
        return Matrix(m_out)


a = Matrix([[31, 22], [37, 43], [51, 86]])
b = Matrix([[31, 22], [37, 43], [51, 86]])
print(f'{a} \n')
print(f'{b} \n')
print(a+b)
