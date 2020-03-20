# coding=utf-8
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(-5, 5, 0.02)
# y = np.sin(x)
#
# plt.axis([-np.pi, np.pi, -2, 2])
#
# plt.plot(x, y, color="r", linestyle="-", linewidth=1)
#
# plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1.2, 2.5, 4.5, 7.3]

# plot函数作图
plt.plot(x, y)

# show函数展示出这个图，如果没有这行代码，则程序完成绘图，但看不到
plt.show()

