# !/usr/bin/env python
# -*- coding: utf-8 -*-
from graphviz import Digraph
import random

G = Digraph(format= 'pdf')
# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G.attr('node', shape='circle')

class combinatorial():
    def gen_node(self, total_num, char_type):
        self.char_type = char_type
        for i in range(0, total_num):
            G.node(str(i), str(chr(char_type+i)))
        return G

    def gen_one_two(self, one_num, two_num, char_type):
        self.char_type = char_type
        for i in range(0, one_num): # スタートのノードの数
            for k in range(0, two_num): # ゴールのノードの数
                G.node(str(k+one_num), str(chr(k+char_type)))
                G.edge(str(i+0), str(k+one_num))
                # G.edge(str(chr(i+0+to_char_s)), str(chr(k+one_num+to_char_s)))
        return G

    def gen_two_three(self, one_num, two_num, three_num, char_type):
        self.char_type = char_type
        for i in range(0, two_num): # スタートのノードの数
            for k in range(0, three_num): # ゴールのノードの数
                G.node(str(k+one_num+two_num), str(chr(k+char_type)))
                G.edge(str(i+0+one_num), str(k+one_num+two_num))
                # G.edge(str(<スタートのノードのインデックス>), str(<ゴールのノードのインデックス>))
        return G

    def gen_three_four(self, one_num, two_num, three_num, four_num, char_type):
        self.char_type = char_type
        for i in range(0, three_num): # スタートのノードの数
            for k in range(0, four_num): # ゴールのノードの数
                G.node(str(k+one_num+two_num+three_num), str(chr(k+char_type)))
                G.edge(str(i+0+one_num+two_num), str(k+one_num+two_num+three_num))
        return G

    def gen_four_five(self, one_num, two_num, three_num, four_num, five_num, char_type):
        self.char_type = char_type
        for i in range(0, four_num): # スタートのノードの数
            for k in range(0, five_num): # ゴールのノードの数
                # G.node(str(k+one_num+two_num+three_num+four_num), str(chr(k+one_num+two_num+three_num+four_num+to_char_s)))
                G.node(str(k+one_num+two_num+three_num+four_num), str(chr(k+char_type)))
                G.edge(str(i+0+one_num+two_num+three_num), str(k+one_num+two_num+three_num+four_num))
        return G
