from tkinter import *
from tkinter.messagebox import *
import sys
import minesweeping

class selectMode():
    def __init__(self):
        self.MAP_WIDTH = 10
        self.BOMBS_NUM = 10
        self.frame = Tk()
        self.frame.wm_title("选择难度")
        self.frame.minsize(300, 200)
        self.modeNo = 1
        v = IntVar()
        v.set(1)
        selectLabelFrame = LabelFrame(self.frame, text="请选择难度：")
        selectLabelFrame.pack(expand=YES)
        easyRadio = Radiobutton(selectLabelFrame, text="简单难度（10x10,10个地雷）", variable=v, value=1, command=self.selectEasyMode)
        normalRadio = Radiobutton(selectLabelFrame, text="中等难度（15x15，60个地雷）", variable=v, value=2, command=self.selectNormalMode)
        hardRadio = Radiobutton(selectLabelFrame, text="困难难度（20x20,175个地雷）", variable=v, value=3, command=self.selectHardMode)
        determineButton = Button(selectLabelFrame, text="确认", command=self.determineMode)
        easyRadio.pack(anchor=W)
        normalRadio.pack(anchor=W)
        hardRadio.pack(anchor=W)
        determineButton.pack()
        self.textlabel = Label(self.frame, text="已选择：简单难度")
        self.textlabel.pack()
        self.frame.mainloop()

    def selectEasyMode(self):
        self.MAP_WIDTH = 10
        self.BOMBS_NUM = 10
        self.modeNo = 1
        self.textlabel['text'] = "已选择：简单难度"

    def selectNormalMode(self):
        self.MAP_WIDTH = 15
        self.BOMBS_NUM = 60
        self.modeNo = 1
        self.textlabel['text'] = "已选择：中等难度"

    def selectHardMode(self):
        self.MAP_WIDTH = 20
        self.BOMBS_NUM = 175
        self.modeNo = 1
        self.textlabel['text'] = "已选择：困难难度"

    def determineMode(self):
        if self.modeNo in range(1, 4):
            minesweeping.minsweeping(self.MAP_WIDTH, self.BOMBS_NUM)
        else:
            showerror(title="出错啦！", message="选择了错误的难度")
            sys.exit()

if __name__ == "__main__":
    selectMode()
