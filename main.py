from lark import Lark

parser = Lark.open('grammar.lark', parser="lalr")

text = open("test.ks").read()
tree = parser.parse(text)
print(tree.pretty())

