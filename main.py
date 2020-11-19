class MatrixProcessor:
    def menu(self):
        while True:
            print('1. Add matrices')
            print('2. Multiply matrix by constant')
            print('3. Multiply matrices')
            print('4. Transpose matrix')
            print('5. Calculate a determinant')
            print('0. Exit')
            choice = input()
            if choice == '1':
                self.addition()
            elif choice == '2':
                self.multiplication_by_num()
            elif choice == '3':
                self.multiply_matrices()
            elif choice == '4':
                self.transposition()
            elif choice == '5':
                self.determinant()
            elif choice == '6':
                self.inverse()
            else:
                print('Bye!')
                return 0

    def enter_matrix(self):
        row, col = map(int, input('Enter size: ').split())
        print('Enter matrix:')
        matrix = [[int(x) if x.isdigit() else float(x) for x in input().split()] for i in range(row)]
        return matrix

    def addition(self):
        matrix_a = self.enter_matrix()
        matrix_b = self.enter_matrix()
        if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
            matrix_c = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in
                        range(len(matrix_a))]
            self.print_matrix(matrix_c)
        else:
            print('ERROR')

    def determinant(self):
        matrix = self.enter_matrix()
        print(f'The result is:\n{self.rec_determinant(matrix)}')

    def rec_determinant(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2 and len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for i in range(len(matrix[0])):
                det += pow(-1, i) * matrix[0][i] *  \
                       self.rec_determinant([row[:i] + row[i + 1:] for row in (matrix[:0] + matrix[1:])])
            return det

    def inverse(self):
        matrix = self.enter_matrix()
        det = self.rec_determinant(matrix)
        if det != 0:
            if len(matrix) == 2:
                print([[matrix[1][1] / det, -1 * matrix[0][1] / det], [-1 * matrix[1][0] / det, matrix[0][0] / det]])
            else:
                cofactors = []
                for row in range(len(matrix)):
                    cofactor_row = []
                    for col in range(len(matrix)):
                        minor = [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]
                        cofactor_row.append(((-1) ** (row + col)) * self.rec_determinant(minor))
                    cofactors.append(cofactor_row)
                cofactors = list(map(list, zip(*cofactors)))
                for row in range(len(cofactors)):
                    for col in range(len(cofactors)):
                        cofactors[row][col] = cofactors[row][col] / det
                self.print_matrix(cofactors)
        else:
            print("This matrix doesn't have an inverse.")

    def multiplication_by_num(self):
        matrix_a = self.enter_matrix()
        num = input()
        if num.isdigit():
            num = int(num)
        else:
            num = float(num)
        matrix_a = [[matrix_a[i][j] * num for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
        self.print_matrix(matrix_a)

    def multiply_matrices(self):
        matrix_a = self.enter_matrix()
        matrix_b = self.enter_matrix()
        if len(matrix_a[0]) == len(matrix_b):
            matrix_tb = [[matrix_b[j][i] for j in range(len(matrix_b))] for i in range(len(matrix_b[0]))]
            matrix_c = []
            for i in range(len(matrix_a)):
                matrix_c.append([])
                for j in range(len(matrix_tb)):
                    matrix_c[i].append(sum([a_item * tb_item for a_item, tb_item in zip(matrix_a[i], matrix_tb[j])]))
            self.print_matrix(matrix_c)
        else:
            print('ERROR')

    def transposition(self):
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        choice = input()
        matrix = self.enter_matrix()
        if choice == '1':
            matrix_t = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            print('The result is:')
            self.print_matrix(matrix_t)
        elif choice == '2':
            matrix_t = [[matrix[j][i] for j in reversed(range(len(matrix)))] for i in reversed(range(len(matrix[0])))]
            print('The result is:')
            self.print_matrix(matrix_t)
        elif choice == '3':
            matrix_t = [[matrix[i][j] for j in reversed(range(len(matrix)))] for i in range(len(matrix[0]))]
            print('The result is:')
            self.print_matrix(matrix_t)
        elif choice == '4':
            matrix_t = [[matrix[i][j] for j in range(len(matrix))] for i in reversed(range(len(matrix[0])))]
            print('The result is:')
            self.print_matrix(matrix_t)
        else:
            print('Incorrect input')

    def print_matrix(self, matrix):
        for i in matrix:
            print(*i)


MatrixProcessor().menu()
