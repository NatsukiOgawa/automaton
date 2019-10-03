from graphviz import Digraph
import random
import os

class super_visory_model_class():
    def super_visory_model(self, m):
        x = 0

        G = Digraph(format="png")
        # 画像の保存形式（拡張子）を指定する

        G.attr("node", shape="square", style="filled")
        # (?, 要素の形, 色の塗りつぶし)
        # attr = attribute → 振る舞い？
        # events = ["1,2", "2,3", "3,4", "4,5", "5,6", "6,7", "7,8", "8,9", "9,10", "10,11", "11,12", "12,13", "13,14", "15,16", "16,17", "17,18", "18,19", "19,20", "20,21", "21,22"]

        events = [[0 for j in range(2)] for i in range(m*(m-1))]
        banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "-"]
        # occured = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "-"]
        occured = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "-"]

        for i in range(m*(m-1)):
            # events[i][0] = int(random.random() * 10 + 1)    # 禁止事象
            # events[i][1] = int(random.random() * 10 + 1)    # 生起事象
            events[i][0] = banned[random.randrange(len(banned))]    # 禁止事象
            events[i][1] = occured[random.randrange(len(occured))]    # 生起事象

        for k in range(m):
            G.node("m[{}]".format(k), shape="circle", color="pink")
            for i in range(m):
                if i!=k:
                    # G.edge("m[{}]".format(i),"m[{}]".format(k),label="a(3,1)")
                    G.edge("m[{}]".format(k),"m[{}]".format(i),label="{}".format(events[x]))
                    x += 1
        # print(events)
        G.render("super_visory_model")

        print()
        print(events)
        root = ["" for i in range(2**m)]
        x = 0
        for k in range(len(root)):
            for i in range(len(events)):
                # print(events[i][0])
                root[k] += str(events[i][x])
                root[k] += " >> "
                # x += 1
                # x %= 2
            print(root[k])
        return

if __name__ == '__main__':
    m = 5

    a = super_visory_model_class()
    a.super_visory_model(m)
