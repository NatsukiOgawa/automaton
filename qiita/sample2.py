import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

h = np.array([[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])
              # 3*3の配列を作る
              
def update(U):
    '''
    Update rule:
    current_state＼N_neighbors | 0   1   2   3   4   5   6   7   8
    ---------------------------+----------------------------------
                             0 | 0   0   0   1   0   0   0   0   0
                             1 | 0   0   1   1   0   0   0   0   0
    '''
    N_neighbors = scipy.signal.convolve2d(U, h, boundary='wrap', mode='same')
    U_next = np.zeros_like(U)
    # 配列の初期化

    U_next[N_neighbors == 3] = 1
    U_next[np.logical_and(N_neighbors == 2, U == 1)] = 1
    return U_next

size = (256, 256)
# ウインドウのサイズを指定する

U = np.random.randint(2,size=size)

fig = plt.figure()
ax = fig.add_subplot(111)
img = ax.imshow(U, interpolation="nearest", cmap=plt.cm.gray)

i = 0
while True:
    # 無限ループ
    U = update(U)
    img.set_data(U)
    i += 1
    ax.set_title("t = {}".format(i))
    # 時期tを出力する

    plt.pause(0.01)
