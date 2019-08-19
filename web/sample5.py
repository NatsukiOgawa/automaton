# nfa.py
from syntax_tree import Node, SyntaxTree
import sys

EMPTY = -1
NFA_STATE_MAX = 128
NFA_VECTOR_SIZE = int(NFA_STATE_MAX / 8)
DFA_STATE_MAX = 100

class NfaList:
    def __init__(self, next=None, to=None, c=None):
        self.char = c
        self.to = to
        self.next = next

class Nfa:
    def __init__(self, regex, debug=False):
        self.nfa = [None for _ in range(NFA_STATE_MAX)]
        self.state = 0
        self.exit = None
        self.entry = None
        self.regex = regex
        self.debug = debug

    def gen_node(self):
        if self.state > NFA_STATE_MAX:
            printf("Too many NFA state.")
            sys.exit(1)
        state = self.state
        self.state += 1
        return state

    def add_transition(self, src, dst, c):
        p = NfaList(self.nfa[src], dst, c)
        self.nfa[src] = p

    def gen_nfa(self, tree, entry, way_out):
        op = tree.op
        if op == 'char':
            self.add_transition(entry, way_out, tree.char)
        elif op == 'empty':
            self.add_transition(entry, way_out, EMPTY)
        elif op == 'union':
            self.gen_nfa(tree.left, entry, way_out)
            self.gen_nfa(tree.right, entry, way_out)
        elif op == 'closure':
            a1 = self.gen_node()
            a2 = self.gen_node()
            self.add_transition(entry, a1, EMPTY)
            self.gen_nfa(tree.left, a1, a2)
            self.add_transition(a2, a1, EMPTY)
            self.add_transition(a1, way_out, EMPTY)
        elif op == 'concat':
            a1 = self.gen_node()
            self.gen_nfa(tree.left, entry, a1)
            self.gen_nfa(tree.right, a1, way_out)
        else:
            print("This cannot happen in ")
            sys.exit(1)
    def init_tree(self):
        tree = SyntaxTree(self.regex, self.debug)
        return tree.make_tree()
    def build_nfa(self):
        tree = self.init_tree()
        self.entry = self.gen_node()
        self.exit = self.gen_node()
        self.gen_nfa(tree, self.entry, self.exit)
        if self.debug:
            print("------ NFA ------")
            self.dump_nfa()
        return self.nfa
    def dump_nfa(self):
        for i in range(self.state):
            if self.nfa[i]:
                print("state {:3}:".format(i),end="")
                p = self.nfa[i]
                while p:
                    c = '?' if p.char == EMPTY else p.char
                    print("({} . {}) ".format(c, p.to), end="")
                    p = p.next
                print()
nfa = Nfa("a(a|b)*a", debug=True)
nfa.build_nfa()
