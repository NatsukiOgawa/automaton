from graphviz import Digraph
import random
import gen_node_edge
import numpy as np

G = Digraph(format= 'pdf')
# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G.attr('node', shape='circle')
# shape='<要素の形を指定>'
# ノード数(ここでは "点"のこと)
one_num   = 2
two_num   = 2
three_num = 2
four_num  = 2
five_num  = 2

elements = [one_num, two_num, three_num, four_num, five_num]

path_list = [[0 for i in range(np.max(elements))] for j in range(len(elements))]
# print(path_list)

total_num = one_num + two_num + three_num + four_num + five_num

to_char_short = 97  # 小文字
to_char_long = 65   # 大文字

path_counter = 0

# char_type = to_char_short
char_type = to_char_long

gen_node = gen_node_edge.combinatorial()
G_con = gen_node.gen_node(one_num, char_type, path_list, path_counter)
G = G_con[0]
path_counter = G_con[1]
one_list = G_con[2]

gen_one_two = gen_node_edge.combinatorial()
G_con = gen_one_two.gen_one_two(one_num, two_num, char_type, path_list, path_counter)
G = G_con[0]
path_counter = G_con[1]
two_list = G_con[2]

gen_two_three = gen_node_edge.combinatorial()
G_con = gen_two_three.gen_two_three(one_num, two_num, three_num, char_type, path_list, path_counter)
G = G_con[0]
path_counter = G_con[1]
three_list = G_con[2]

gen_three_four = gen_node_edge.combinatorial()
G_con = gen_three_four.gen_three_four(one_num, two_num, three_num, four_num, char_type, path_list, path_counter)
G = G_con[0]
path_counter = G_con[1]
four_list = G_con[2]

gen_four_five = gen_node_edge.combinatorial()
G_con = gen_four_five.gen_four_five(one_num, two_num, three_num, four_num, five_num, char_type, path_list, path_counter)
G = G_con[0]
path_counter = G_con[1]
five_list = G_con[2]

# G.edge(str(99), str(100), label="qwerty")
total_reward_list = np.zeros(one_num * two_num * three_num * four_num * five_num)
reward_index_counter = 0

print(G)
# print()するとdot形式で出力される
for n in range(1):
    for m in range(0, one_num):
        for l in range(0, two_num):
            for k in range(0, three_num):
                for j in range(0, four_num):
                    for i in range(0, five_num):
                        print("=====")
                        print("=====")
                        print("====")
                        print("===")
                        print("==")
                        print("=")
                        print("{}{}{}{}{}".format(path_list[n][m], path_list[m][l],path_list[l][k], path_list[k][j], path_list[j][i]))
                        print("{}".format(one_list[m] * two_list[l] * three_list[k] * four_list[j] * five_list[i]))
                        total_reward_list[reward_index_counter] = one_list[m] * two_list[l] * three_list[k] * four_list[j] * five_list[i]
                        reward_index_counter += 1
# print(one_list)
# print(two_list)
# print(three_list)
# print(four_list)
# print(five_list)
print("=========================================================================================================================================")
print("報酬の添字(終了時：one_num * two_num + three_num * four_num * five_num)")
print(reward_index_counter)
# print(total_reward_list)
print()
print()
print("best_path(インデックス)")
best_path = np.argmax(total_reward_list)
print(best_path)
print()
print("best_pathの時の報酬（コスト）")
print(np.max(total_reward_list))
print()
print("平均")
print(np.mean(total_reward_list))


print("=========================================================================================================================================")
print("re-culculate")
total_reward_list = np.zeros(one_num * two_num * three_num * four_num * five_num)


best_i = 0
best_j = 0
best_k = 0
best_l = 0
best_m = 0

# print(G)
reward_index_counter_replay = 0
# print()するとdot形式で出力される
for n in range(1):
    for m in range(0, one_num):
        for l in range(0, two_num):
            for k in range(0, three_num):
                for j in range(0, four_num):
                    for i in range(0, five_num):
                        # print("{}{}{}{}{}".format(m, l, k, j, i))
                        if (reward_index_counter_replay == best_path):
                            best_i = i
                            best_j = j
                            best_k = k
                            best_l = l
                            best_m = m
                            res = gen_node_edge.combinatorial()
                            res.result(best_path, reward_index_counter_replay, best_i, best_j, best_k, best_l, best_m)
                            break
                        else:

                            # print("{}{}{}{}{}".format(path_list[n][m], path_list[m][l],path_list[l][k], path_list[k][j], path_list[j][i]))
                            # print("{}".format(one_list[m] * two_list[l] * three_list[k] * four_list[j] * five_list[i]))
                            # total_reward_list[reward_index_counter] = one_list[m] * two_list[l] * three_list[k] * four_list[j] * five_list[i]
                            reward_index_counter_replay += 1


# print()
# print(best_i)
# print(best_j)
# print(best_k)
# print(best_l)
# print(best_m)
print("=========================================================================================================================================")
print("報酬の添字(best_path と一致した時にforループを抜ける)")
print(reward_index_counter_replay)
# print(total_reward_list)
print()
print()


G.render('image2')
# binary_tree.<shape='   '>で保存
