from graphviz import Digraph
import random
import gen_node_edge

G = Digraph(format= 'pdf')
# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G.attr('node', shape='circle')
# shape='<要素の形を指定>'
# ノード数(ここでは "点"のこと)
one_num   = 10
two_num   = 10
three_num = 10
four_num  = 10
five_num  = 10

total_num = one_num + two_num + three_num + four_num + five_num

to_char_short = 97  # 小文字
to_char_long = 65   # 大文字

# char_type = to_char_short
char_type = to_char_long

gen_node = gen_node_edge.combinatorial()
G = gen_node.gen_node(one_num, char_type)

gen_one_two = gen_node_edge.combinatorial()
G = gen_one_two.gen_one_two(one_num, two_num, char_type)

gen_two_three = gen_node_edge.combinatorial()
G = gen_two_three.gen_two_three(one_num, two_num, three_num, char_type)

gen_three_four = gen_node_edge.combinatorial()
G = gen_three_four.gen_three_four(one_num, two_num, three_num, four_num, char_type)

gen_four_five = gen_node_edge.combinatorial()
G = gen_four_five.gen_four_five(one_num, two_num, three_num, four_num, five_num, char_type)

# G.edge(str(99), str(100), label="qwerty")

print(G)
                    # print()するとdot形式で出力される
G.render('image2')
# binary_tree.<shape='   '>で保存
