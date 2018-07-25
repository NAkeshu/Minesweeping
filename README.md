# 扫雷（python3+tkinter）
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)  
~~写着玩的~~

**只有`minesweeping.pn`和`selectMode.py`是有用的，`old_minesweeping.py`是留作纪念的（雾），`Timer.py`还不能用，随缘实现吧……**
# TO-DO：
+ [x] 生成12x12的网格作为游戏棋盘
+ [x] 随机位置生成12个炸弹
+ [x] 在棋盘上绘制出炸弹
+ [x] 开始游戏选择简单、中等、困难三个等级的难度
+ [x] 计算出炸弹周围的数字，并在相应位置绘制出来
+ [x] 修补完善难度选择功能
+ [x] 在棋盘的每个上覆盖遮挡
+ [x] 点击遮挡自动消失，并且返回点击的方格编号
+ [x] 右键点击遮挡可以标记（此时不能再用左键清除遮挡），再次点击取消标记
+ [x] 判断点击方格下的内容（空？数字？炸弹？）
+ [x] 点击遮挡后自动将附近没有炸弹的遮挡一起清除（搜索周围的炸弹）
+ [x] 判断游戏结束（胜利、失败），确认后关闭当前游戏窗口
+ [x] 点击第一个遮挡后才开始（初始化）游戏（防止第一个就点到炸弹）
+ [x] 优化代码

**以下功能随缘吧**
+ [ ] 计时/计步
+ [ ] 添加胜利后的庆祝动画（看心情）
# 截图
![selectMode](https://i.loli.net/2018/07/25/5b5873194b460.png)
![easy](https://i.loli.net/2018/07/25/5b5872e835060.png)
![normal](https://i.loli.net/2018/07/25/5b58736499ae3.png)
![win](https://i.loli.net/2018/07/25/5b58732dc6ab9.png)
![fail](https://i.loli.net/2018/07/25/5b587348ef813.png)
~~另外，真的超级想吐槽一下python的二维数组……非常不习惯~~