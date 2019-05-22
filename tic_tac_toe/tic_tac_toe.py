class TicTacToe:

    n = 3

    cells = { 1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2) }

    def __init__(self):
        self.table = [["" for _ in range(TicTacToe.n)] for _ in range(TicTacToe.n)]

    @staticmethod
    def cell_content(mark, x, y):
        if mark == "":
            return str(x * TicTacToe.n + y + 1)

        return mark

    def show_table(self):
        print()
        print("Current table:")

        for i in range(self.n):
            for j in range(self.n):
                print(TicTacToe.cell_content(self.table[i][j], i, j), end=" ")

            print()

        print()

    @staticmethod
    def who_win(mark):
        return 1 if mark == "x" else 2

    def move(self, cell, mark):
        if self.table[self.cells[cell][0]][self.cells[cell][1]] == "":
            self.table[self.cells[cell][0]][self.cells[cell][1]] = mark

    def is_finished(self, cell, mark):
        # 0 - not finished, 1 - server(x) win, 2 - client(o) win, 3 - draw

        x, y = self.cells[cell]

        for i in range(self.n):
            if self.table[x][i] != mark:
                break

            if i == self.n - 1:
                return TicTacToe.who_win(mark)
            
        for i in range(self.n):
            if self.table[i][y] != mark:
                break
            
            if i == self.n - 1:
                return TicTacToe.who_win(mark)

        if x == y:
            for i in range(self.n):
                if self.table[i][i] != mark:
                    break
                
                if i == self.n - 1:
                    return TicTacToe.who_win(mark)

        if x + y == self.n - 1:
            for i in range(self.n):
                if self.table[i][(self.n - 1) - i] != mark:
                    break
                
                if i == self.n - 1:
                    return TicTacToe.who_win(mark)

        move_count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.table[i][j] != "":
                    move_count += 1
        
        if move_count == self.n ** 2:
            return 3

        return 0


    


