# !/usr/bin/env python
# -*- coding: utf-8 -*-
from graphviz import Digraph
import random
import numpy as np

G = Digraph(format= 'pdf')
# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G.attr('node', shape='circle')

class combinatorial():
    def gen_node(self, one_num, char_type, path_list, path_counter):
        self.char_type = char_type
        self.one_num = one_num
        self.path_list = path_list
        self.path_counter = path_counter
        one_list = np.zeros(one_num)
        for i in range(0, one_num):
            G.node(str(i), str(chr(char_type+i)))
            one_list[i] = random.random()
            path_list[path_counter][i] = chr(char_type+i)
        path_counter += 1
        return G, path_counter, one_list

    def gen_one_two(self, one_num, two_num, char_type, path_list, path_counter):
        self.char_type = char_type
        self.one_num = one_num
        self.path_list = path_list
        self.path_counter = path_counter
        two_list = np.zeros(two_num)
        for i in range(0, one_num): # スタートのノードの数
            for k in range(0, two_num): # ゴールのノードの数
                G.node(str(k+one_num), str(chr(k+char_type)))
                two_list[k] = random.random()
                path_list[path_counter][k] = chr(k+char_type)
                G.edge(str(i+0), str(k+one_num))
        path_counter += 1
        return G, path_counter, two_list

    def gen_two_three(self, one_num, two_num, three_num, char_type, path_list, path_counter):
        self.char_type = char_type
        self.one_num = one_num
        self.path_list = path_list
        self.path_counter = path_counter
        three_list = np.zeros(three_num)
        for i in range(0, two_num): # スタートのノードの数
            for k in range(0, three_num): # ゴールのノードの数
                G.node(str(k+one_num+two_num), str(chr(k+char_type)))
                three_list[k] = random.random()
                path_list[path_counter][k] = chr(k+char_type)
                G.edge(str(i+0+one_num), str(k+one_num+two_num))
        path_counter += 1
        return G, path_counter, three_list

    def gen_three_four(self, one_num, two_num, three_num, four_num, char_type, path_list, path_counter):
        self.char_type = char_type
        self.one_num = one_num
        self.path_list = path_list
        self.path_counter = path_counter
        four_list = np.zeros(four_num)
        for i in range(0, three_num): # スタートのノードの数
            for k in range(0, four_num): # ゴールのノードの数
                G.node(str(k+one_num+two_num+three_num), str(chr(k+char_type)))
                four_list[k] = random.random()
                path_list[path_counter][k] = chr(k+char_type)
                G.edge(str(i+0+one_num+two_num), str(k+one_num+two_num+three_num))
        path_counter += 1
        return G, path_counter, four_list

    def gen_four_five(self, one_num, two_num, three_num, four_num, five_num, char_type, path_list, path_counter):
        self.char_type = char_type
        self.one_num = one_num
        self.path_list = path_list
        self.path_counter = path_counter
        five_list = np.zeros(five_num)
        for i in range(0, four_num): # スタートのノードの数
            for k in range(0, five_num): # ゴールのノードの数
                G.node(str(k+one_num+two_num+three_num+four_num), str(chr(k+char_type)))
                five_list[k] = random.random()
                path_list[path_counter][k] = chr(k+char_type)
                G.edge(str(i+0+one_num+two_num+three_num), str(k+one_num+two_num+three_num+four_num))
        path_counter += 1
        return G, path_counter, five_list

    def result(self, best_path, reward_index_counter_replay, best_i, best_j, best_k, best_l, best_m):
        self.best_path = best_path
        self.reward_index_counter_replay = reward_index_counter_replay
        self.best_i = best_i
        self.best_j = best_j
        self.best_k = best_k
        self.best_l = best_l
        self.best_m = best_m
        # print(best_i)
        # print(best_j)
        # print(best_k)
        # print(best_l)
        # print(best_m)
        if (reward_index_counter_replay == best_path):
            total = best_i*1 + best_j*2 + best_k*4 + best_l*8 + best_m*16
            print("total")
            print(total)
            return
