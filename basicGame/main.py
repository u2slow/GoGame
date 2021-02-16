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
        self.BlackPoints = 0
        self.WhitePoints = 0
    
    def createGame(self):
        for i in range(self.size):
            self.board.append([])
            for k in range(self.size):
                self.board[i].append(Cell(i,k,"empty"))
    
    def addCell(self, inX, inY, instatus):
        x = inX
        y = inY
        status = instatus
        while status != "black" and status != "empty" and status != "white":
            print("wrong status!")
            status = input("Status ")
        self.board[x][y].status = status
    
    def checkLibertys(self):
        for i in range(self.size):
            for k in range(self.size):
                if i < self.size -1  and i > 0 and k < self.size -1 and k > 0:
                    if self.board[i+1][k].status == "empty" or self.board[i-1][k].status == "empty" or self.board[i][k+1].status == "empty" or self.board[i][k-1].status == "empty":
                        self.board[i][k].libertys += 1

        for i in range(self.size):
            for k in range(self.size):
                if self.board[i][k].libertys == 0:
                    if self.board[i][k].status == "black" or self.board[i][k].status == "white":
                        self.board[i][k].status = "empty"

if __name__== "__main__":
    x = 9 #input("wie Groß?")
    x = int(x)
    game = Board(x)
    game.createGame()

    def showBoard():
        for i in range(x):
            for k in range(x):
                print(i,k,game.board[i][k].status)
    game.addCell(1,2,"black")
    game.addCell(3,2,"black")
    game.addCell(2,1,"black")
    game.addCell(2,3,"black")
    game.addCell(2,2,"white")
    game.checkLibertys()
    showBoard()


    