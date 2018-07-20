from tkinter import *

def initGameFrame(title, width, height):
    frame = Tk()
    frame.wm_title(title)
    frame.minsize(width, height)
    return frame

def initMap(rootframe):
    map = Canvas(rootframe, width=620, height=720, bg="white")
    map.create_rectangle(10, 100, 610, 700)
    for i in range(0, 12):
        map.create_line(10, 100 + i * 50, 610, 100 + i * 50)
        map.create_line(10 + i * 50, 100, 10 + i * 50, 700)
    map.pack()
    return map

def initMessageArea(canvas):
    canvas.create_rectangle(260, )

def main():
    root = initGameFrame("扫雷雷", 620, 720)
    gameMap = initMap(root)
    root.mainloop()

if __name__ == "__main__":
    main()