import sys
from antlr4 import *
from gen.impLexer import impLexer
from gen.impParser import impParser
from gen.impVisitor import impVisitor


def main(argv):
    #take the input of the file
    Input = FileStream(argv[1])

    lexer = impLexer(Input)

    stream = CommonTokenStream(lexer)

    parser = impParser(stream)
    tree = parser.cmd()

    visitor = impVisitor()
    transVisitor = visitor.visit(tree)



    #Sorting out pythons indentation

    lines = transVisitor.split('\n')
    count = 0
    for i in range(0,len(lines)):
        count = count + lines[i].count('@') - lines[i].count('END')
        if 'END' in lines[i]:
            y = lines[i].replace('END', '')
            lines[i] = y

        if '@' in lines[i]:
            y = lines[i].replace('@', '')
            lines[i] = y

        lines[i] = '    '*count + lines[i]

    lines = '\n'.join(lines)
    print(lines)


if __name__ == '__main__':
    main(sys.argv)