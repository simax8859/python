# 定义棋盘的大小
BOARD_SIZE = 15
# 定义一个二维列表来充当棋盘
board = []


def initBoard():
    # 为每个元素赋值“+”，用于在控制台画出棋盘
    for i in range(BOARD_SIZE):
        row = ["➕"] * BOARD_SIZE
        board.append(row)


# 在控制台输出棋盘的方法
def printBoard():
    # 打印灭个列表元素
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # 打印列表元素后不换行
            print("%1s" % board[i][j], end="")
        # 换行
        print()


initBoard()
printBoard()
input_str = input("请输入您下棋的坐标: \n")
while input_str is not None:
    # 将用户输入的字符串以逗号（,）作为分隔符，分隔成两个字符串
    x_str, y_str = input_str.split(sep=",")
    # 为对应的列表元素赋值“◉”
    board[int(y_str) - 1][int(x_str) - 1] = "⚪"
    printBoard()
    input_str = input("请输入您下棋的坐标，应以x,y的格式：\n")
