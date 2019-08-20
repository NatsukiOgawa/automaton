# !/usr/bin/env python
# -*- coding: utf-8 -*-

from graphviz import Digraph
import random

G = Digraph(format= 'pdf')
# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)

G.attr('node', shape='square')
# shape='<要素の形を指定>'

N = 20
# ノード数(ここでは "点"のこと)
# インデックスなので、0から数える

# ノードの追加
for i in range(N):
    G.node(str(i), str(i))
    # G.node(str(ノードのインデックス), str(ノードの内容：label=" "))

# 辺の追加
for i in range(N):
    if (i - 1) // 2 >= 0:
        G.edge(str((i - 1) // 2), str(i))
        # G.edge(str((i - 1) // <進数>), str(<"頭"の数?>))
        # 切り捨て

        # [0]:-1//2 = -0.5 → -1 (先頭・てっぺん)
        # [1]:0 //2 = 0    → 0
        # [2]:1 //2 = 0.5  → 0
        # [3]:2 //2 = 1    → 1
        # [4]:3 //2 = 1.5  → 1
        # [5]:4 //2 = 2    → 2
        # [6]:5 //2 = 2.5  → 2

print(G)
# print()するとdot形式で出力される

G.render('binary_tree')
# binary_tree.<shape='   '>で保存
