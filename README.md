# IMP-to-Python
The aim of this project was to be able to take a program which was written in IMP (the syntax of which can be found here: http://flint.cs.yale.edu/cs428/coq/sf/Imp.html) and convert it into python code. 

# Set up

To run this project you will need to have ANTLR installed. You can find the offcial set up guide here: https://github.com/antlr/antlr4/blob/master/doc/getting-started.md however I found this guide to be much easier to understand: https://tomassetti.me/antlr-mega-tutorial/#chapter11

There should be a Virtual Environment folder which will manage all the dependancies required for this project which my IDE (pycharm) generated for me. It SHOULD work with all IDE's however I have not tested this. 

# Running the script

We want to take a simple imp program like this one below. 

```
X := 1;
Y := 1;
Result := 0;
Count := 0;
while Count < 100 do
Result := X + Y;
X := Y;
Y := Result;
Count := Count + 1
od
```

All this does is take two numbers and add them together producing the sequence 1 1 2 3 5 8 13 ... So this program generates the first 100 numbers in the fibbonacci sequence. 

When we run imp_to_python.py it takes this imp program we have just written and converts it into python code:

```
p_X=1
p_Y=1
p_Result=0
p_Count=0
while ((p_Count<100)): 
    p_Result=p_X+p_Y
    p_X=p_Y
    p_Y=p_Result
    p_Count=p_Count+1
```

Something to note is that all variables will start with the prefix p_ . This is because in our imp program we can name our variables anything we like and we don't want our variable name to clash with a key word in python. So to avoid this we simple start every variable name with this prefix. 

# How have we achieved this?

We want to do things in the following order:

Create a Grammar -> Let ANTLR generate a parse tree -> visit each node of the parse tree

![119968788_3542798845786073_8170399756407281336_n](https://user-images.githubusercontent.com/62481908/127685151-26e070ed-7c6e-4e81-a051-fa9e1e00dde8.png)

Creating a Grammar:

We want to first of all create a lexer and then a parser and we do this by defining a rule set inside our grammar:


The first step is called tokenization or lexing. All this means is if I give you the string "a b c" I want you to break it up into parts (tokens) based on some set of rules. This rules are defined in our grammer. The Lexer rules are defined at the bottom of the grammar and are in upper case like so:

```
/*
* Parser rules
*/

Here would be our parser rules

/*
* Lexer rules
*/

LETTERS : [a-z]+ ;
```

But what are parser rules?

If we have a basic calculator that can only add up two single digit numbers then we need to beable to process statements such as: 
2 + 2 

So we need to take each individual token and tell the grammar what it is. In this case when it sees a plus sign inbetween two numbers then that is an operation. So the grammar for this basic calclator would look like so:

```
operation : NUMBER '+' NUMBER;

NUMBER : [0-9]+
WHITESPACE: ' ' -> skip;
```

This would generate a parse tree similar to the one in the diagram at the top of this section. 


Now that we have created these rules ANTLR will work its magic and generate a parser and a lexer for us. However we still need to visit each node of the tree and tell our program when you come across xyz expression written in IMP (ie when you visit this node) we want you to write down this expression in python. ie:

```
    # Visit a parse tree produced by impParser#Brackets.
    def visitBrackets(self, ctx:impParser.BracketsContext):
        return '(' + self.visit(ctx.inner) + ')
```
This is saying when you come across the node "Brackets" return two brackets and then go and visit the inner node to tell us what is inside. 

# Conclusion
Whilst this is a little "hand wavey" all we are doing with this transpiler is breaking up the input into our desired expressions. Recognising what each expresion is (ie a NUMBER + NUMBER is addition) and marking it on our tree a such. Then finally visiting each node of this tree and generating the desired python code depending on what each node is labeled as. 

If you have any questions please feel free to contact me via any contact information listed on my CV.

