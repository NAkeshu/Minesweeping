from tkinter import *
from tkinter.messagebox import *
import random

class blockCanvas():
    """
    继承的画布，记录改组件的位置(self.x, self.y)
    """
    def __init__(self, master, x, y):
        self.clickedNum = 0
        self.WarningImg = PhotoImage(file="./img/warning.png")
        self.x = x
        self.y = y
        self.canvas = Canvas(master, width=50, height=50, bg="gray")
        self.canvas.place(x=x, y=y, anchor=NW)

def initGameFrame(title, width, height):
    """
    创建游戏窗口
    :param title: 标题
    :param width: 窗口宽度
    :param height: 窗口高度
    :return: 创建的窗口
    """
    frame = Toplevel()
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
    frameWidth = MAP_WIDTH*50 + 40
    frameHeight = MAP_WIDTH*50 + 90

    map = Canvas(rootframe, width=frameWidth, height=frameHeight, bg="white")
    map.create_rectangle(20, 70, frameWidth-20, frameHeight-20) # 扫雷的棋盘
    for i in range(0, MAP_WIDTH):
        map.create_line(20, 70+i*50, frameWidth-20, 70+i*50) # 横线
        map.create_line(20+i*50, 70, 20+i*50, frameHeight-20) # 竖线
    map.pack(side=BOTTOM)
    return map

def setMessageText(canvas):
    """
    计步（点击次数）或者计时
    :param frame: 游戏窗口
    :param text: 标题（计步或者计时）
    :return:
    """
    frameWidth = MAP_WIDTH*50 + 40
    canvas.create_text(frameWidth-120, 30, text="步数：")

def drawDigitsOnSide(canvas):
    """
    标出棋盘边上的数字
    :param canvas:
    :return:
    """
    for i in range(0, MAP_WIDTH):
        canvas.create_text(10, 95+i*50, text=str(i))
        canvas.create_text(45+i*50, 60, text=str(i))

def initGameData(n):
    """
    将nxn的游戏棋盘中每个小方格一次按照0～nxn-1的编号排好，
    使得二维的棋盘数据可以通过一维的字典数据结构保存。
    字典的键为方格编号，值为该方格中的数据。
    其中，0代表空，>0代表炸弹数，-1代表有炸弹，-2代表遮挡被清除
    :param n:
    :return:
    """
    GameData = {}
    for i in range(0, n*n):
        GameData[str(i)] = 0
    return GameData

def initBombs():
    """
    随机生成n个不同位置的编号，在数据里
    :param n: 生成炸弹数
    :return: 炸弹所在的格子编号的列表
    """
    BombNum = random.sample(range(0, MAP_WIDTH*MAP_WIDTH), BOMBS_NUM)
    for i in BombNum:
        gameData[str(i)] = -1

def drawBombs(mapcanvas):
    """
    在扫雷画布上绘制出炸弹
    :param mapcanvas: 棋盘画布
    :param BombNum: 炸弹的位置编号的列表
    :return:
    """
    global BombImg
    BombImg = PhotoImage(file="./img/BombMini.png")
    n = len(gameData)
    for i in range(0, n):
        if gameData[str(i)] == -1:
            x = 20 + 50*(i % MAP_WIDTH)
            y = 70 + 50*int(i / MAP_WIDTH)
            print(str(i)+": (" + str(i%MAP_WIDTH) + ", " + str(int(i/MAP_WIDTH)) + ")")
            mapcanvas.create_image(x, y, anchor='nw', image=BombImg)

def drawDigitsAroundBomb(mapcanvas):
    """
    在扫雷的棋盘上标出地雷周围的数字
    :param map: 棋盘画布
    :return:
    """
    for i in range(0, BOX_NUM):
        if gameData[str(i)] > 0:
            x = 45 + 50*(i % MAP_WIDTH)
            y = 95 + 50*int(i / MAP_WIDTH)
            mapcanvas.create_text(x, y, text=str(gameData[str(i)]))

def countAllDigits():
    for i in range(0, BOX_NUM):
        if gameData[str(i)] == -1:
            countDigitAroundTheBomb(i)

def countDigitAroundTheBomb(bombAddNum):
    if bombAddNum > (MAP_WIDTH - 1):
        if bombAddNum < MAP_WIDTH*(MAP_WIDTH - 1):
            countDigitOverBomb(bombAddNum)
            countDigitBesideBomb(bombAddNum)
            countDigitUnderBomb(bombAddNum)
        else:
            countDigitOverBomb(bombAddNum)
            countDigitBesideBomb(bombAddNum)
    else:
        countDigitBesideBomb(bombAddNum)
        countDigitUnderBomb(bombAddNum)

def countDigitOverBomb(bombAddNum):
    if bombAddNum % MAP_WIDTH > 0:
        if bombAddNum % MAP_WIDTH < (MAP_WIDTH - 1):
            for i in range(-1, 2):
                if gameData[str(bombAddNum - MAP_WIDTH + i)] >= 0:
                    gameData[str(bombAddNum - MAP_WIDTH + i)] += 1
        else:
            for i in range(-1, 1):
                if gameData[str(bombAddNum - MAP_WIDTH + i)] >= 0:
                    gameData[str(bombAddNum - MAP_WIDTH + i)] += 1
    else:
        for i in range(0, 2):
            if gameData[str(bombAddNum - MAP_WIDTH + i)] >= 0:
                gameData[str(bombAddNum - MAP_WIDTH + i)] += 1

def countDigitBesideBomb(bombAddNum):
    if bombAddNum % MAP_WIDTH > 0:
        if bombAddNum % MAP_WIDTH < (MAP_WIDTH - 1):
            for i in [-1, 1]:
                if gameData[str(bombAddNum + i)] >= 0:
                    gameData[str(bombAddNum + i)] += 1
        else:
            if gameData[str(bombAddNum - 1)] >= 0:
                gameData[str(bombAddNum - 1)] += 1
    else:
        if gameData[str(bombAddNum + 1)] >= 0:
            gameData[str(bombAddNum + 1)] += 1

def countDigitUnderBomb(bombAddNum):
    if bombAddNum % MAP_WIDTH > 0:
        if bombAddNum % MAP_WIDTH < (MAP_WIDTH - 1):
            for i in range(-1, 2):
                if gameData[str(bombAddNum + MAP_WIDTH + i)] >= 0:
                    gameData[str(bombAddNum + MAP_WIDTH + i)] += 1
        else:
            for i in range(-1, 1):
                if gameData[str(bombAddNum + MAP_WIDTH + i)] >= 0:
                    gameData[str(bombAddNum + MAP_WIDTH + i)] += 1
    else:
        for i in range(0, 2):
            if gameData[str(bombAddNum + MAP_WIDTH + i)] >= 0:
                gameData[str(bombAddNum + MAP_WIDTH + i)] += 1

def drawBlocks(mapcanvas):
    """
    在方格上放置按钮
    :param mapcanvas:
    :return:
    """
    global Blocks
    Blocks = {}
    for i in range (0, BOX_NUM):
        x = 20 + 50*(i % MAP_WIDTH)
        y = 70 + 50*int(i / MAP_WIDTH)
        theBlock = blockCanvas(mapcanvas, x, y)
        theBlock.canvas.bind("<Button-1>", clickBlock)
        theBlock.canvas.bind("<Button-3>", rightClickBlock)
        Blocks[str(i)] = theBlock

def clickBlock(event):
    blockBeClicked = event.widget
    for i in range(0, BOX_NUM):
        if Blocks[str(i)].canvas == blockBeClicked:
            px = Blocks[str(i)].x
            py = Blocks[str(i)].y
            x = int((px - 20)/50)
            y = int((py - 70)/50)
            BlockNo = x + y*MAP_WIDTH
            isGameFailed(BlockNo)
            searchEmptyBox(BlockNo)
            isGameWinned()
            # print(str(BlockNo)+": ("+str(x)+", "+str(y)+")")

def rightClickBlock(event):
    blockBeClicked = event.widget
    for i in range(0, BOX_NUM):
        if Blocks[str(i)].canvas == blockBeClicked:
            Blocks[str(i)].clickedNum += 1
            if Blocks[str(i)].clickedNum % 2 == 1:
                markBlock(event)
                Blocks[str(i)].canvas.unbind("<Button-1>")
            else:
                deleteMark(event)
                Blocks[str(i)].canvas.bind("<Button-1>", clickBlock)

def markBlock(event):
    theBlock = event.widget
    for i in range(0, BOX_NUM):
        if Blocks[str(i)].canvas == theBlock:
            img = Blocks[str(i)].WarningImg
            theBlock.create_image(0, 0, anchor='nw', image=img)

def deleteMark(event):
    theBlock = event.widget
    theBlock.delete(ALL)

def searchEmptyBox(firstBoxNo):
    """
    利用广度优先搜索，将周围空白方格上的遮挡清除，
    遇到数字方格或者棋盘边界停止
    :param firstBoxNo: 初始方格
    :return:
    """
    global searchList
    searchList = []
    searchList.append(firstBoxNo)
    while searchList:
        searchTheBox(searchList.pop(0))

def searchTheBox(No):
    if gameData[str(No)] == 0:
        if No >= MAP_WIDTH:
            searchUporUnderBoxs(No-MAP_WIDTH)
        searchBesideBoxs(No)
        if No < BOX_NUM-MAP_WIDTH-1:
            searchUporUnderBoxs(No+MAP_WIDTH)
    gameData[str(No)] = -2
    Blocks[str(No)].canvas.place_forget()

def searchUporUnderBoxs(UporDownNo):
    if UporDownNo % MAP_WIDTH >= 1:
        if UporDownNo % MAP_WIDTH < MAP_WIDTH - 1:
            searchList.append(UporDownNo-1)
            searchList.append(UporDownNo)
            searchList.append(UporDownNo+1)
        else:
            searchList.append(UporDownNo-1)
            searchList.append(UporDownNo)
    else:
        searchList.append(UporDownNo)
        searchList.append(UporDownNo+1)

def searchBesideBoxs(No):
    if No % MAP_WIDTH >= 1:
        if No % MAP_WIDTH < MAP_WIDTH - 1:
            searchList.append(No-1)
            searchList.append(No+1)
        else:
            searchList.append(No-1)
    else:
        searchList.append(No+1)

def isGameFailed(blockNo):
    """
    判断游戏是否失败：
    检测点击的方格下是否是炸弹，如果是，游戏失败；
    如果不是，游戏继续
    :param blockNo:
    :return:
    """
    for i in range (0, BOX_NUM):
        if gameData[str(i)] == -1 and blockNo == i:
            gameFailed(blockNo)
            root.destroy()

def isGameWinned():
    """
    判断游戏是否胜利：
    检测所有非炸弹方格上的遮挡是否被清空，如果是，游戏胜利；
    如果不是，游戏继续
    :return:
    """
    blockClickedNum = 0
    for i in range(0, BOX_NUM):
        if gameData[str(i)] == -2:
            blockClickedNum += 1
    if blockClickedNum == BOX_NUM - BOMBS_NUM:
        gameWinned()
        root.destroy()

def gameFailed(No):
    for i in range(0, BOX_NUM):
        if gameData[str(i)] == -1:
            if i == No:
                px = Blocks[str(i)].x
                py = Blocks[str(i)].y
                gameMap.create_rectangle(px, py, px+50, py+50, fill='red')
                gameMap.create_image(px, py, anchor='nw', image=BombImg)
            Blocks[str(i)].canvas.place_forget()
    showinfo(title="游戏结束！", message="完了，踩到地雷了QwQ")

def gameWinned():
    showinfo(title="游戏结束！", message="恭喜您把地雷都找到了！")

def startGame(map_width, bombs_num):
    global MAP_WIDTH
    global BOMBS_NUM
    global BOX_NUM
    MAP_WIDTH = map_width
    BOMBS_NUM = bombs_num
    BOX_NUM = MAP_WIDTH*MAP_WIDTH

    frameWidth = MAP_WIDTH*50 + 40
    frameHeight = MAP_WIDTH*50 + 90

    global root
    root = initGameFrame("扫雷雷", frameWidth, frameHeight)
    global gameMap
    gameMap = initMap(root)
    drawDigitsOnSide(gameMap)
    setMessageText(gameMap)
    global gameData
    gameData = initGameData(MAP_WIDTH)
    initBombs()
    drawBombs(gameMap)
    countAllDigits()
    drawDigitsAroundBomb(gameMap)
    drawBlocks(gameMap)
    root.mainloop()

if __name__ == "__main__":
    startGame(12, 24)
