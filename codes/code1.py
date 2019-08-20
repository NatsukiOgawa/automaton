from graphviz import Digraph

G = Digraph(format="png")
# 画像の保存形式（拡張子）を指定する

G.attr("node", shape="square", style="filled")
# (?, 要素の形, 色の塗りつぶし)
# attr = attribute → 振る舞い？

G.edge("Q 0","Q 1",label="a(3,1)")
G.edge("Q 0","Q 2",label="b(2,3)")
G.edge("Q 0","Q 3",label="c(1,2)")
G.edge("Q 0","Q 4",label="d(0,-)")
# G.edge("<スタート>", "<ゴール>", "<数値>")

G.edge("Q 1","Q 11",label="a(3,1)")
G.edge("Q 1","Q 12",label="b(2,3)")
G.edge("Q 1","Q 13",label="c(1,2)")
G.edge("Q 1","Q 14",label="d(0,-)")

G.edge("Q 2","Q 21",label="a(3,1)")
G.edge("Q 2","Q 22",label="b(2,3)")
G.edge("Q 2","Q 23",label="c(1,2)")
G.edge("Q 2","Q 24",label="d(0,-)")

G.edge("Q 3","Q 31",label="a(3,1)")
G.edge("Q 3","Q 32",label="b(2,3)")
G.edge("Q 3","Q 33",label="c(1,2)")
G.edge("Q 3","Q 34",label="d(0,-)")

G.edge("Q 4","Q 41",label="a(3,1)")
G.edge("Q 4","Q 42",label="b(2,3)")
G.edge("Q 4","Q 43",label="c(1,2)")
G.edge("Q 4","Q 44",label="d(0,-)")

G.node("Q 0", shape="circle", color="pink")
G.node("Q 1", shape="circle", color="grey")
G.node("Q 2", shape="circle", color="grey")
G.node("Q 3", shape="circle", color="grey")
G.node("Q 4", shape="circle", color="grey")
# G.node("Q 1", shape="triangle", color="red")
# G.node("ノードの名前", shape="形", color="<色>")

G.render("code1")
