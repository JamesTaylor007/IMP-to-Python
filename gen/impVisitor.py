# Generated from C:/Users/enter/PycharmProjects/grammars\imp.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .impParser import impParser
else:
    from .impParser import impParser

# This class defines a complete generic visitor for a parse tree produced by impParser.

class impVisitor(ParseTreeVisitor):

    #a place to store our variable names for assignments
    global variableNames;
    variableNames = set()

    '''
    starting with the arithemtic expressions aexp
    '''

    # Visit a parse tree produced by impParser#Atom.
    def visitAtom(self, ctx:impParser.AtomContext):
        return ctx.getText()

    # Visit a parse tree produced by impParser#Variable.
    def visitVariable(self, ctx:impParser.VariableContext):
        return 'p_' + ctx.getText()

    # Visit a parse tree produced by impParser#Brackets.
    def visitBrackets(self, ctx:impParser.BracketsContext):
        return '(' + self.visit(ctx.inner) + ')'

    # Visit a parse tree produced by impParser#Mult.
    def visitMult(self, ctx:impParser.MultContext):
        return self.visit(ctx.left) + '*' + self.visit(ctx.right)

    # Visit a parse tree produced by impParser#Sub.
    def visitSub(self, ctx:impParser.SubContext):
        return self.visit(ctx.left) + '-' + self.visit(ctx.right)

    # Visit a parse tree produced by impParser#Add.
    def visitAdd(self, ctx:impParser.AddContext):
        return self.visit(ctx.left) + '+' + self.visit(ctx.right)


    '''
    Now we can define the visitors for the boolean expressions
    '''

    # Visit a parse tree produced by impParser#True.
    def visitTrue(self, ctx:impParser.TrueContext):
        return 'True'


    # Visit a parse tree produced by impParser#False.
    def visitFalse(self, ctx:impParser.FalseContext):
        return 'False'


    # Visit a parse tree produced by impParser#Equal.
    def visitEqual(self, ctx:impParser.EqualContext):
        return '(' + self.visit(ctx.left) + '==' + self.visit(ctx.right) + ')'


    # Visit a parse tree produced by impParser#Smaller.
    def visitSmaller(self, ctx:impParser.SmallerContext):
        return '(' + self.visit(ctx.left) + '<' + self.visit(ctx.right) + ')'


    # Visit a parse tree produced by impParser#Greater.
    def visitGreater(self, ctx:impParser.GreaterContext):
        return '(' + self.visit(ctx.left) + '>' + self.visit(ctx.right) + ')'


    # Visit a parse tree produced by impParser#Inequality.
    def visitInequality(self, ctx:impParser.InequalityContext):
        return '(' + self.visit(ctx.left) + ' != ' + self.visit(ctx.right) + ')'


    # Visit a parse tree produced by impParser#Not.
    def visitNot(self, ctx:impParser.NotContext):
        return '(' + 'not ' + self.visit(ctx.inner) + ')'


    # Visit a parse tree produced by impParser#And.
    def visitAnd(self, ctx:impParser.AndContext):
        return '(' + self.visit(ctx.left) + ' and ' + self.visit(ctx.right) + ')'


    # Visit a parse tree produced by impParser#Or.
    def visitOr(self, ctx:impParser.OrContext):
        return '(' + self.visit(ctx.left) + ' or ' + self.visit(ctx.right) + ')'


    '''
    finally the commands
    '''

    # Visit a parse tree produced by impParser#Skip.
    def visitSkip(self, ctx:impParser.SkipContext):
        return '\n'
    
    

    # Visit a parse tree produced by impParser#Assignment.
    def visitAssignment(self, ctx:impParser.AssignmentContext):
        variableNames.add(ctx.variable.text)
        return 'p_' + ctx.variable.text + '=' + self.visit(ctx.expression) + '\n'

    # Visit a parse tree produced by impParser#Sequence.
    def visitSequence(self, ctx:impParser.SequenceContext):
        return self.visit(ctx.first) + self.visit(ctx.second)


    # Visit a parse tree produced by impParser#If.
    def visitIf(self, ctx:impParser.IfContext):
        return 'if (' + self.visit(ctx.condition) + '): \n@' + self.visit(ctx.truecase) + 'ENDelse: \n@' + self.visit(ctx.falsecase) + '\nEND'


    # Visit a parse tree produced by impParser#While.
    def visitWhile(self, ctx:impParser.WhileContext):
        return 'while (' + self.visit(ctx.condition) + '): \n@' + self.visit(ctx.body) +'END'


del impParser