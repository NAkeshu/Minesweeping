from tkinter import *
import minesweeping

def selectEasyMode():
    global MAP_WIDTH
    global BOMBS_NUM
    MAP_WIDTH = 6
    BOMBS_NUM = 3

    textlabel['text'] = "6x6的地图大小，3个地雷"

def selectNormalMode():
    global MAP_WIDTH
    global BOMBS_NUM
    MAP_WIDTH = 12
    BOMBS_NUM = 24

    textlabel['text'] = "12x12的地图大小，24个地雷"

def selectHardMode():
    global MAP_WIDTH
    global BOMBS_NUM
    MAP_WIDTH = 15
    BOMBS_NUM = 75

    textlabel['text'] = "15x15的地图大小，75个雷"

def determineMode():
    textlabel['text'] = "确认！MAP_WIDTH="+str(MAP_WIDTH)+", BOMBS_NUM="+str(BOMBS_NUM)
    minesweeping.startGame(MAP_WIDTH, BOMBS_NUM)


def showModes():
    global textlabel
    frame = Tk()
    frame.wm_title("选择难度")
    frame.minsize(300, 200)
    selectLabelFrame = LabelFrame(frame, text="请选择难度：")
    selectLabelFrame.pack(expand=YES)
    easyRadio = Radiobutton(selectLabelFrame, text="简单难度（6x6,3个地雷）", command=selectEasyMode)
    normalRadio = Radiobutton(selectLabelFrame, text="中等难度（12x12，24个地雷）", command=selectNormalMode)
    hardRadio = Radiobutton(selectLabelFrame, text="困难难度（15x15,75个地雷）", command=selectHardMode)
    determineButton = Button(selectLabelFrame, text="确认", command=determineMode)
    easyRadio.pack(anchor=W)
    normalRadio.pack(anchor=W)
    hardRadio.pack(anchor=W)
    determineButton.pack()
    textlabel = Label(frame, text="")
    textlabel.pack()
    frame.mainloop()

if __name__ == "__main__":
    showModes()