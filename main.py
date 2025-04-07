from lark import Lark

parser = Lark.open('grammar.lark', parser="lalr")

# text = open("test.k").read()
text = open("fibonacci.k").read()
tree = parser.parse(text)
print(tree.pretty())

