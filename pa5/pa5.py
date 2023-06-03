"REPLACE THE BOTTOM WITH YOUR Matrix CLASS "


# change list comprhenstions
from Vec import Vec
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
        if len(self.colsp[j-1]) != len(u):
            raise ValueError("Incompatible column length.")
        self.colsp[j-1] = u
        for i in range(len(self.rowsp)):
            self.rowsp[i][j-1] = u[i]

    def set_row(self, i, v):
        if len(self.rowsp[i-1]) != len(v):
            raise ValueError("Incompatible column length.")
        self.rowsp[i-1] = v
        for j in range(len(v)):
            self.colsp[j][i-1] = v[j]

    def set_entry(self, i, j, x):
        self.rowsp[i-1][j-1] = x
        self.colsp[j-1][i-1] = x

    def get_col(self, j):
        return self.colsp[j-1]

    def get_row(self, i):
        return self.rowsp[i-1]

    def get_entry(self, i, j):
        return self.rowsp[i-1][j-1]

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
