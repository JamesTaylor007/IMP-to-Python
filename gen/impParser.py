# Generated from C:/Users/enter/PycharmProjects/grammars\imp.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\5\2\20\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\33")
        buf.write("\n\2\f\2\16\2\36\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3@\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4U\n\4\3\4\3\4\3\4\7\4Z\n\4\f\4")
        buf.write("\16\4]\13\4\3\4\2\4\2\6\5\2\4\6\2\2\2l\2\17\3\2\2\2\4")
        buf.write("?\3\2\2\2\6T\3\2\2\2\b\t\b\2\1\2\t\20\7\34\2\2\n\20\7")
        buf.write("\33\2\2\13\f\7\3\2\2\f\r\5\2\2\2\r\16\7\4\2\2\16\20\3")
        buf.write("\2\2\2\17\b\3\2\2\2\17\n\3\2\2\2\17\13\3\2\2\2\20\34\3")
        buf.write("\2\2\2\21\22\f\5\2\2\22\23\7\5\2\2\23\33\5\2\2\6\24\25")
        buf.write("\f\4\2\2\25\26\7\6\2\2\26\33\5\2\2\5\27\30\f\3\2\2\30")
        buf.write("\31\7\7\2\2\31\33\5\2\2\4\32\21\3\2\2\2\32\24\3\2\2\2")
        buf.write("\32\27\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2")
        buf.write("\2\35\3\3\2\2\2\36\34\3\2\2\2\37@\7\b\2\2 @\7\t\2\2!\"")
        buf.write("\5\2\2\2\"#\7\n\2\2#$\5\2\2\2$@\3\2\2\2%&\5\2\2\2&\'\7")
        buf.write("\13\2\2\'(\5\2\2\2(@\3\2\2\2)*\5\2\2\2*+\7\f\2\2+,\5\2")
        buf.write("\2\2,@\3\2\2\2-.\5\2\2\2./\7\r\2\2/\60\5\2\2\2\60@\3\2")
        buf.write("\2\2\61\62\7\16\2\2\62@\5\4\3\2\63\64\7\3\2\2\64\65\5")
        buf.write("\4\3\2\65\66\7\17\2\2\66\67\5\4\3\2\678\7\4\2\28@\3\2")
        buf.write("\2\29:\7\3\2\2:;\5\4\3\2;<\7\20\2\2<=\5\4\3\2=>\7\4\2")
        buf.write("\2>@\3\2\2\2?\37\3\2\2\2? \3\2\2\2?!\3\2\2\2?%\3\2\2\2")
        buf.write("?)\3\2\2\2?-\3\2\2\2?\61\3\2\2\2?\63\3\2\2\2?9\3\2\2\2")
        buf.write("@\5\3\2\2\2AB\b\4\1\2BU\7\21\2\2CD\7\33\2\2DE\7\22\2\2")
        buf.write("EU\5\2\2\2FG\7\24\2\2GH\5\4\3\2HI\7\25\2\2IJ\5\6\4\2J")
        buf.write("K\7\26\2\2KL\5\6\4\2LM\7\27\2\2MU\3\2\2\2NO\7\30\2\2O")
        buf.write("P\5\4\3\2PQ\7\31\2\2QR\5\6\4\2RS\7\32\2\2SU\3\2\2\2TA")
        buf.write("\3\2\2\2TC\3\2\2\2TF\3\2\2\2TN\3\2\2\2U[\3\2\2\2VW\f\5")
        buf.write("\2\2WX\7\23\2\2XZ\5\6\4\6YV\3\2\2\2Z]\3\2\2\2[Y\3\2\2")
        buf.write("\2[\\\3\2\2\2\\\7\3\2\2\2][\3\2\2\2\b\17\32\34?T[")
        return buf.getvalue()


class impParser ( Parser ):

    grammarFileName = "imp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'-'", "'+'", "'true'", 
                     "'false'", "'='", "'<'", "'>'", "'<>'", "'not'", "'and'", 
                     "'or'", "'skip'", "':='", "';'", "'if'", "'then'", 
                     "'else'", "'fi'", "'while'", "'do'", "'od'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "INT", "WS" ]

    RULE_aexp = 0
    RULE_bexp = 1
    RULE_cmd = 2

    ruleNames =  [ "aexp", "bexp", "cmd" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    VAR=25
    INT=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return impParser.RULE_aexp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(AexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.AexpContext
            super().__init__(parser)
            self.left = None # AexpContext
            self.right = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.AexpContext)
            else:
                return self.getTypedRuleContext(impParser.AexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(AexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.AexpContext
            super().__init__(parser)
            self.left = None # AexpContext
            self.right = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.AexpContext)
            else:
                return self.getTypedRuleContext(impParser.AexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(AexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.AexpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(impParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class BracketsContext(AexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.AexpContext
            super().__init__(parser)
            self.inner = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self):
            return self.getTypedRuleContext(impParser.AexpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrackets" ):
                return visitor.visitBrackets(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(AexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.AexpContext
            super().__init__(parser)
            self.left = None # AexpContext
            self.right = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.AexpContext)
            else:
                return self.getTypedRuleContext(impParser.AexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(AexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.AexpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(impParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def aexp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = impParser.AexpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_aexp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [impParser.INT]:
                localctx = impParser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(impParser.INT)
                pass
            elif token in [impParser.VAR]:
                localctx = impParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(impParser.VAR)
                pass
            elif token in [impParser.T__0]:
                localctx = impParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(impParser.T__0)
                self.state = 10
                localctx.inner = self.aexp(0)
                self.state = 11
                self.match(impParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = impParser.MultContext(self, impParser.AexpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_aexp)
                        self.state = 15
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 16
                        self.match(impParser.T__2)
                        self.state = 17
                        localctx.right = self.aexp(4)
                        pass

                    elif la_ == 2:
                        localctx = impParser.SubContext(self, impParser.AexpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_aexp)
                        self.state = 18
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 19
                        self.match(impParser.T__3)
                        self.state = 20
                        localctx.right = self.aexp(3)
                        pass

                    elif la_ == 3:
                        localctx = impParser.AddContext(self, impParser.AexpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_aexp)
                        self.state = 21
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 22
                        self.match(impParser.T__4)
                        self.state = 23
                        localctx.right = self.aexp(2)
                        pass

             
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return impParser.RULE_bexp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NotContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.inner = None # BexpContext
            self.copyFrom(ctx)

        def bexp(self):
            return self.getTypedRuleContext(impParser.BexpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.left = None # BexpContext
            self.right = None # BexpContext
            self.copyFrom(ctx)

        def bexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.BexpContext)
            else:
                return self.getTypedRuleContext(impParser.BexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.left = None # AexpContext
            self.right = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.AexpContext)
            else:
                return self.getTypedRuleContext(impParser.AexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.left = None # BexpContext
            self.right = None # BexpContext
            self.copyFrom(ctx)

        def bexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.BexpContext)
            else:
                return self.getTypedRuleContext(impParser.BexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class GreaterContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.left = None # AexpContext
            self.right = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.AexpContext)
            else:
                return self.getTypedRuleContext(impParser.AexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater" ):
                return visitor.visitGreater(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class SmallerContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.left = None # AexpContext
            self.right = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.AexpContext)
            else:
                return self.getTypedRuleContext(impParser.AexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmaller" ):
                return visitor.visitSmaller(self)
            else:
                return visitor.visitChildren(self)


    class InequalityContext(BexpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.BexpContext
            super().__init__(parser)
            self.left = None # AexpContext
            self.right = None # AexpContext
            self.copyFrom(ctx)

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.AexpContext)
            else:
                return self.getTypedRuleContext(impParser.AexpContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInequality" ):
                return visitor.visitInequality(self)
            else:
                return visitor.visitChildren(self)



    def bexp(self):

        localctx = impParser.BexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bexp)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = impParser.TrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(impParser.T__5)
                pass

            elif la_ == 2:
                localctx = impParser.FalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(impParser.T__6)
                pass

            elif la_ == 3:
                localctx = impParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                localctx.left = self.aexp(0)
                self.state = 32
                self.match(impParser.T__7)
                self.state = 33
                localctx.right = self.aexp(0)
                pass

            elif la_ == 4:
                localctx = impParser.SmallerContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                localctx.left = self.aexp(0)
                self.state = 36
                self.match(impParser.T__8)
                self.state = 37
                localctx.right = self.aexp(0)
                pass

            elif la_ == 5:
                localctx = impParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                localctx.left = self.aexp(0)
                self.state = 40
                self.match(impParser.T__9)
                self.state = 41
                localctx.right = self.aexp(0)
                pass

            elif la_ == 6:
                localctx = impParser.InequalityContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                localctx.left = self.aexp(0)
                self.state = 44
                self.match(impParser.T__10)
                self.state = 45
                localctx.right = self.aexp(0)
                pass

            elif la_ == 7:
                localctx = impParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.match(impParser.T__11)
                self.state = 48
                localctx.inner = self.bexp()
                pass

            elif la_ == 8:
                localctx = impParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 49
                self.match(impParser.T__0)
                self.state = 50
                localctx.left = self.bexp()
                self.state = 51
                self.match(impParser.T__12)
                self.state = 52
                localctx.right = self.bexp()
                self.state = 53
                self.match(impParser.T__1)
                pass

            elif la_ == 9:
                localctx = impParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 55
                self.match(impParser.T__0)
                self.state = 56
                localctx.left = self.bexp()
                self.state = 57
                self.match(impParser.T__13)
                self.state = 58
                localctx.right = self.bexp()
                self.state = 59
                self.match(impParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return impParser.RULE_cmd

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AssignmentContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.CmdContext
            super().__init__(parser)
            self.variable = None # Token
            self.expression = None # AexpContext
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(impParser.VAR, 0)
        def aexp(self):
            return self.getTypedRuleContext(impParser.AexpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class SkipContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkip" ):
                return visitor.visitSkip(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.CmdContext
            super().__init__(parser)
            self.condition = None # BexpContext
            self.body = None # CmdContext
            self.copyFrom(ctx)

        def bexp(self):
            return self.getTypedRuleContext(impParser.BexpContext,0)

        def cmd(self):
            return self.getTypedRuleContext(impParser.CmdContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class SequenceContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.CmdContext
            super().__init__(parser)
            self.first = None # CmdContext
            self.second = None # CmdContext
            self.copyFrom(ctx)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.CmdContext)
            else:
                return self.getTypedRuleContext(impParser.CmdContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a impParser.CmdContext
            super().__init__(parser)
            self.condition = None # BexpContext
            self.truecase = None # CmdContext
            self.falsecase = None # CmdContext
            self.copyFrom(ctx)

        def bexp(self):
            return self.getTypedRuleContext(impParser.BexpContext,0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(impParser.CmdContext)
            else:
                return self.getTypedRuleContext(impParser.CmdContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def cmd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = impParser.CmdContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_cmd, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [impParser.T__14]:
                localctx = impParser.SkipContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.match(impParser.T__14)
                pass
            elif token in [impParser.VAR]:
                localctx = impParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                localctx.variable = self.match(impParser.VAR)
                self.state = 66
                self.match(impParser.T__15)
                self.state = 67
                localctx.expression = self.aexp(0)
                pass
            elif token in [impParser.T__17]:
                localctx = impParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(impParser.T__17)
                self.state = 69
                localctx.condition = self.bexp()
                self.state = 70
                self.match(impParser.T__18)
                self.state = 71
                localctx.truecase = self.cmd(0)
                self.state = 72
                self.match(impParser.T__19)
                self.state = 73
                localctx.falsecase = self.cmd(0)
                self.state = 74
                self.match(impParser.T__20)
                pass
            elif token in [impParser.T__21]:
                localctx = impParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(impParser.T__21)
                self.state = 77
                localctx.condition = self.bexp()
                self.state = 78
                self.match(impParser.T__22)
                self.state = 79
                localctx.body = self.cmd(0)
                self.state = 80
                self.match(impParser.T__23)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = impParser.SequenceContext(self, impParser.CmdContext(self, _parentctx, _parentState))
                    localctx.first = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cmd)
                    self.state = 84
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 85
                    self.match(impParser.T__16)
                    self.state = 86
                    localctx.second = self.cmd(4) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.aexp_sempred
        self._predicates[2] = self.cmd_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def aexp_sempred(self, localctx:AexpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def cmd_sempred(self, localctx:CmdContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




