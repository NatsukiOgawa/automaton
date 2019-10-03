# !/usr/bin/env python
# -*- coding: utf-8 -*-

from graphviz import Digraph
import random

G = Digraph(format= 'pdf')
# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)

G.attr('node', shape='circle')
# shape='<要素の形を指定>'

# ノード数(ここでは "点"のこと)
# インデックスなので、0から数える
one_num = 5
two_num = 5
three_num = 5
total_num = one_num + two_num + three_num
one_two = total_num - two_num - three_num
two_three = total_num - one_num - two_num

to_char_s = 92
# ノードの追加
for j in range(one_num):
    G.node(str(j), str(j))
    # G.node(str(ノードのインデックス), str(ノードの内容：label=" "))

for i in range(one_two):
    for c in range(one_two):
        G.edge(str(one_num-i), str(chr(two_num+to_char_s + c)))

for k in range(two_three):
    for c in range(two_three):
        G.edge(str(two_num-k), str(chr(three_num+to_char_s+c)))

# # 辺の追加
# for i in range(one_num):
# #     if (i - 1) // 2 >= 0:
#     G.edge(str(i), str(i+two_num+1))
#     G.edge(str(i), str(i+two_num+2))
#     G.edge(str(i), str(i+two_num+3))
#     G.edge(str(i), str(i+two_num+4))
#     G.edge(str(i), str(i+two_num+5))
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

G.render('image')
# binary_tree.<shape='   '>で保存
