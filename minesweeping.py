from tkinter import *
import random

def initGameFrame(title, width, height):
    """
    创建游戏窗口
    :param title: 标题
    :param width: 窗口宽度
    :param height: 窗口高度
    :return: 创建的窗口
    """
    frame = Tk()
    frame.wm_title(title)
    frame.minsize(width, height)
    frame.maxsize(width, height)
    return frame

def initMap(rootframe):
    """
    在游戏窗口上画出扫雷的棋盘
    :param rootframe: 游戏窗口
    :return: 棋盘画布
    """
    map = Canvas(rootframe, width=640, height=690, bg="white")
    map.create_rectangle(20, 70, 620, 670) # 扫雷的棋盘
    for i in range(0, 12):
        map.create_line(20, 70+i*50, 620, 70+i*50) # 横线
        map.create_line(20+i*50, 70, 20+i*50, 670) # 竖线
    map.pack(side=BOTTOM)
    return map

def setMessageText(canvas, text):
    """
    计步（点击次数）或者计时
    :param frame: 游戏窗口
    :param text: 标题（计步或者计时）
    :return:
    """
    canvas.create_text(510, 30, text=text)

def drawDigitsOnSide(canvas, n):
    """
    标出棋盘边上的数字
    :param canvas:
    :return:
    """
    for i in range(0, n):
        canvas.create_text(10, 95+i*50, text=str(i))
        canvas.create_text(45+i*50, 60, text=str(i))

def drawDigitsAroundBomb(map):
    """
    在扫雷的棋盘上标出地雷周围的数字
    :param map: 棋盘画布
    :return:
    """
    pass

def initBombs(n):
    """
    随机生成n个不同位置的编号，位置按照格子从左到右，从上到下的顺序，一共有12x12个
    :param n: 生成炸弹数
    :return: 炸弹所在的格子编号的列表
    """
    BombNum = random.sample(range(1, 12*12+1), n)
    return BombNum

def drawBombs(mapcanvas, BombNum):
    """
    在扫雷画布上绘制出炸弹
    :param mapcanvas: 棋盘画布
    :param BombNum: 炸弹的位置编号的列表
    :return:
    """
    global BombImg
    BombImg = PhotoImage(file="./img/BombMini.png")
    n = len(BombNum)
    for i in range(0, n):
        x = 20 + 50*(BombNum[i] % 12)
        y = 70 + 50*int(BombNum[i] / 12)
        print("(" + str(x) + ", " + str(y) + ")")
        mapcanvas.create_image(x, y, anchor='nw', image=BombImg)

def main():
    root = initGameFrame("扫雷雷", 640, 690)
    gameMap = initMap(root)
    drawDigitsOnSide(gameMap, 12)
    setMessageText(gameMap, "步数：")
    Bombs = initBombs(12)
    drawBombs(gameMap, Bombs)
    #drawDigitsAndBombs(gameMap)
    root.mainloop()

if __name__ == "__main__":
    main()