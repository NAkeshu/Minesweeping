from tkinter import *

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
    map = Canvas(rootframe, width=620, height=620, bg="white")
    map.create_rectangle(10, 10, 610, 610) # 扫雷的棋盘
    for i in range(0, 12):
        map.create_line(10, 10+i*50, 610, 10+i*50) # 横线
        map.create_line(10+i*50, 10, 10+i*50, 610) # 竖线
    map.pack(side=BOTTOM)
    return map

def setMessageText(frame, text):
    """
    计步（点击次数）或者计时
    :param frame: 游戏窗口
    :param text: 标题（计步或者计时）
    :return:
    """
    stepMessage = Label(frame, text=text)
    stepMessage.pack(side=TOP)

def initDigitsAndBombs(map):
    """
    在扫雷的棋盘上标出地雷以及周围的地雷数
    :param map: 棋盘画布
    :return:
    """
    for i in range(0, 12):
        map.create_text(35+50*i, 35+50*i, text=str(i))

def main():
    root = initGameFrame("扫雷雷", 620, 670)
    gameMap = initMap(root)
    setMessageText(root, "步数：")
    initDigitsAndBombs(gameMap)
    root.mainloop()

if __name__ == "__main__":
    main()