from graphviz import Digraph

G = Digraph(format="png")
# 画像の保存形式（拡張子）を指定する

G.attr("node", shape="square", style="filled")
# (?, 要素の形, 色の塗りつぶし)
# attr = attribute → 振る舞い？

G.edge("start","state1",label="0.8")
# G.edge("<スタート>", "<ゴール>", "<数値>")


G.edge("start","state2",label="0.2")
G.edge("state1","state1",label="0.5")
G.edge("state2","state2", label="0.8")
G.edge("state1","state2",label="0.5")
G.edge("state2","end",label="0.2")
G.edge("end","count",label="1.0")
G.edge("count","start",label="1.0")

G.node("start", shape="circle", color="pink")
# G.node("state1", shape="triangle", color="red")
# G.node("ノードの名前", shape="形", color="<色>")

G.render("sample")
