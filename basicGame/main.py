class Cell():
    def __init__(self, xposition, yposition,status):
        self.xposition = xposition
        self.yposition = yposition
        self.status = status
        self.libertys = 0


class Board():
    def __init__(self, size):
        self.board = []
        self.size = size
    
    def createGame(self):
        for i in range(self.size):
            self.board.append([])
            for k in range(self.size):
                self.board[i].append(Cell(i,k,"empty"))
    
    def addCell(self):
        x = int(input("wo in X "))
        y = int(input("wo in Y "))
        status = input("Status ")
        while status != "black" and status != "empty" and status != "white":
            print("wrong status!")
            status = input("Status ")
        self.board[x][y].status = status
    
    def checkLibertys(self):
        for i in range(self.size):
            for k in range(self.size):
                if i < self.size  and i > 0 and k < self.size and k > 0:
                    if self.board[i+1][k].status == "empty":
                        self.board[i][k].libertys += 1
                

if __name__== "__main__":
    x = 9 #input("wie Groß?")
    x = int(x)
    game = Board(x)
    game.createGame()

    def showBoard():
        for i in range(x):
            for k in range(x):
                print(i,k,game.board[i][k].status)
    game.addCell()


    