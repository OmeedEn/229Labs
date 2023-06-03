#Add a method norm(self, p) to your Vec class so that if u is a Vec object, then u.norm(p)
#returns the Lp norm of vector u

import math

class Vec:
    def __init__(self, contents=[]):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
        return

    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        x = 0
        for i in self.elements:
            x += (i ** 2)
        return math.sqrt(x)

    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        if len(self.elements) != len(other.elements):
            raise ValueError
        result = []
        for i in range(0, len(self.elements)):
            result.append(self.elements[i] + other.elements[i])
        return Vec(result)

    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        if len(self.elements) != len(other.elements):
            raise ValueError

        result = []
        for i in range(0, len(self.elements)):
            result.append(self.elements[i] - other.elements[i])
        return Vec(result)

    def __mul__(self, other):
        """Overloads the * operator to support
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)

        """
        result = []
        if type(other) == Vec:  # define dot product
            if len(self.elements) != len(other.elements):
                raise ValueError
            else:
                finalresult = 0
                for i in range(0, len(self.elements)):
                    result.append(self.elements[i] * other.elements[i])
                for i in result:
                    finalresult += i

                return finalresult

        elif type(other) == float or type(other) == int:  # scalar-vector multiplication
            for i in range(0, len(self.elements)):
                result.append(self.elements[i] * other)

            return Vec(result)

    def __rmul__(self, other):
        """Overloads the * operation to support
            - float * Vec
            - int * Vec
        """
        result = []

        for i in range(0, len(self.elements)):
            result.append(self.elements[i] * other)

        return Vec(result)

    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements)  # does NOT need further implementation


class Matrix:

    def __init__(self, rowsp):
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)

    def _construct_cols(self, rowsp):
        colsp = []
        col_num = len(rowsp[0])
        row_num = len(rowsp)
        for i in range(col_num):
            col = []
            for j in range(row_num):
                col.append(rowsp[j][i])
            colsp.append(col)
        return colsp

    def __add__(self, other):
        if type(other) == Matrix:
            if len(self.rowsp) == len(other.rowsp):
                if len(self.rowsp[0]) == len(other.rowsp[0]):
                    result = []
                    for i in range(0, len(self.rowsp)):
                        column = []
                        for j in range(0, len(self.rowsp[0])):
                            column.append(self.rowsp[i][j] + other.rowsp[i][j])
                        result.append(column)
                    return Matrix(result)
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

    def __sub__(self, other):
        if type(other) == Matrix:
            if len(self.rowsp) == len(other.rowsp):
                if len(self.rowsp[0]) == len(other.rowsp[0]):
                    result = []
                    for i in range(0, len(self.rowsp)):
                        column = []
                        for j in range(0, len(self.rowsp[0])):
                            column.append(self.rowsp[i][j] - other.rowsp[i][j])
                        result.append(column)
                    return Matrix(result)
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

    def __mul__(self, other):
        result = []
        if type(other) == float or type(other) == int:
            for i in range(len(self.rowsp)):
                row = []
                for j in range(len(self.rowsp[i])):
                    x = self.rowsp[i][j] * other
                    row.append(x)
                result.append(row)

            return Matrix(result)

        elif type(other) == Matrix:
            if len(self.colsp) != len(other.rowsp):
                raise ValueError

            for i in range(len(self.rowsp)):
                row = []
                for j in range(len(other.colsp)):
                    col = 0
                    for k in range(len(other.colsp[0])):
                        col += self.rowsp[i][k] * other.colsp[j][k]
                    row.append(col)
                result.append(row)
            return Matrix(result)

        elif type(other) == Vec:
            result = [0 for i in range(len(self.rowsp))]
            if len(self.rowsp[0]) == len(other.elements):
                for i in range(len(self.rowsp)):
                    for j in range(len(other.elements)):
                        result[i] += self.rowsp[i][j] * other.elements[j]
                return Vec(result)
            else:
                raise ValueError("ERROR: Dimension mismatch.")
        else:
            raise ValueError("ERROR: Unsupported Type.")
        return

    def __rmul__(self, other):
        if type(other) == float or type(other) == int:
            result = []
            for i in range(len(self.rowsp)):
                row = []
                for j in range(len(self.rowsp[i])):
                    row.append(self.rowsp[i][j] * other)
                result.append(row)
            return Matrix(result)
        else:
            raise ValueError("ERROR: Unsupported Type.")
        return

    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rowsp:
            mat_str += str(row) + "\n"
        return mat_str

    def __eq__(self, other):
        """overloads the == operator to return True if
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()

    def __req__(self, other):
        """overloads the == operator to return True if
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()

    def set_col(self, j, u):
        if len(self.colsp[j - 1]) != len(u):
            raise ValueError("Incompatible column length.")
        self.colsp[j - 1] = u
        for i in range(len(self.rowsp)):
            self.rowsp[i][j - 1] = u[i]

    def set_row(self, i, v):
        if len(self.rowsp[i - 1]) != len(v):
            raise ValueError("Incompatible column length.")
        self.rowsp[i - 1] = v
        for j in range(len(v)):
            self.colsp[j][i - 1] = v[j]

    def set_entry(self, i, j, x):
        self.rowsp[i - 1][j - 1] = x
        self.colsp[j - 1][i - 1] = x

    def get_col(self, j):
        return self.colsp[j - 1]

    def get_row(self, i):
        return self.rowsp[i - 1]

    def get_entry(self, i, j):
        return self.rowsp[i - 1][j - 1]

    def col_space(self):
        return self.colsp

    def row_space(self):
        return self.rowsp

    def get_diag(self, k):
        col = 0
        row = 0
        list = []
        if k < 0:
            k = abs(k)
            for i in range(k, len(self.rowsp)):
                list.append(self.rowsp[i][col])
                col += 1
            return list

        for i in range(k, len(self.colsp)):
            list.append(self.rowsp[row][i])
            row += 1
        return list

    def ref(self):
        new_rows = [row[:] for row in self.rowsp]
        num_rows, num_cols = len(new_rows), len(new_rows[0])
        for i in range(num_cols):
            pivot_row = i
            while pivot_row < num_rows and new_rows[pivot_row][i] == 0:
                pivot_row += 1
            if pivot_row == num_rows:
                continue
            if pivot_row != i:
                new_rows[i], new_rows[pivot_row] = new_rows[pivot_row], new_rows[i]
            for j in range(i + 1, num_rows):
                multiplier = new_rows[j][i] / new_rows[i][i]
                new_rows[j] = [new_rows[j][k] - multiplier * new_rows[i][k] for k in range(num_cols)]

        return Matrix(new_rows)

    def rank(self):
        ref_matrix = self.ref()
        num_pivots = 0
        for i in range(len(ref_matrix.rowsp)):
            row = ref_matrix.rowsp[i]
            if any(row):
                num_pivots += 1
        return num_pivots

def gram_schmidt(S):
    """ Takes a list of vectors and returns an orthonormal basis for the span of the vectors
    INPUT: list of vectors
    OUTPUT: orthonormal basis as list of vectors
    """
    #     for i in range(len(S)):
    #             for j in range(i+1, len(S)):
    #                 if abs(S[i]*S[j]) > 1e-10:
    #                     raise ValueError("The input vectors are not orthogonal.")
    #                 else:
    basis = []
    for v in S:
        u = v
        for b in basis:
            u = u - ((b * u) / (b * b)) * b
        if abs(u) > 0:
            basis.append(u)
    orthonormal_basis = []
    for b in basis:
        orthonormal_basis.append(b * (1 / abs(b)))
    return orthonormal_basis

print(gram_schmidt(S = [[12, 8, 4], [3, 2, 1], [-6, -9, 7]]))
#
# def gauss_solve(A, b):
#     n = len(A.rowsp)
#     for i in range(n):
#         max_coeff = abs(A.rowsp[i][i])
#         max_row = i
#         for j in range(i + 1, n):
#             if abs(A.rowsp[j][i]) > max_coeff:
#                 max_coeff = abs(A.rowsp[j][i])
#                 max_row = j
#
#         if max_coeff == 0:
#             return None
#
#         A.rowsp[i], A.rowsp[max_row] = A.rowsp[max_row], A.rowsp[i]
#         b.elements[i], b.elements[max_row] = b.elements[max_row], b.elements[i]
#
#         for j in range(i + 1, n):
#             c = -A.rowsp[j][i] / A.rowsp[i][i]
#             for k in range(i, n):
#                 print(i, j, k)
#                 A.rowsp[j][k] += c * A.rowsp[i][k]
#             b.elements[j] += c * b.elements[i]
#
#     x = [0] * n
#     for i in range(n - 1, -1, -1):
#         x[i] = b.elements[i] / A.rowsp[i][i]
#         for j in range(i - 1, -1, -1):
#             b.elements[j] -= A.rowsp[j][i] * x[i]
#
#     return Vec(x)
#
# print(gauss_solve([1, 11, 10, -2, -10, 7, -5, -15]
#                   [1, 11, 10, -2, -10, 7, -5, -15], [204, -175, -101, 96, -111, 267, 76, -48, 67, -134, -35]))
