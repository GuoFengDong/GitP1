import matplotlib.pyplot as plt #导入pyplot模块,指定别名为plt

squares = [1, 4, 9, 16, 25] #创建一个列表，包含前五个整数的平方

fig, ax = plt.subplots() #创建一个图形和一组子图
ax.plot(squares) #在子图上绘制平方数的折线图

plt.show() #显示图形
