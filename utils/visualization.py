import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import hypothesis


def plot_h():
    # 生成 x 和 y 值
    x = np.linspace(-50, 50, 100)
    y = np.linspace(-50, 50, 100)

    # 创建网格
    X, Y = np.meshgrid(x, y)

    # 计算 z 值
    Z = hypothesis.hypothesis(X, Y)

    # 绘制 3D 图像
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Plot of z = h(x,y)')
    plt.show()
