## Project Proposal ##

My project proposal is to use the Template Scripting Testing Language (TSTL) to
define a test harness for the `sqlparse` Python module. The module provides a
parser for SQL statements. The parser takes a string for one or more SQL
statements and returns a tuple of objects for the parse trees  of the SQL
statements. The module also provides classes and methods for analyzing the parse
trees of SQL statements.

The parser provided by the module will be tested for correctness. The parser is
considered correct if it returns the parse tree of the input SQL statements, for
any standard SQL statements. The XML example will be used to guide the initial
design.

**TODO:** describe subset of SQL to test

The module is compatible with Python 2.7 and 3 and is released under the terms
of the BSD 2-clause license. The project page for the module is located at
https://github.com/andialbrecht/sqlparse. The module can be installed in several
ways. One way to install the module is using pip from the command line
interface:

    $ pip install sqlparse

**TODO:** describe other ways to install module

## Instructions ##

To generate the test harness defined by `mysqlparse.py` run the following
commands (in this directory):

    $ rm sut.*
    
    $ tstl --nocover mysqlparse.tstl

This will generate the test harness named `sut.py`. To run the random tester on
the test harness, run a command similar to the following (in this directory):

    $ python ../../../tstl/generators/randomtester.py --nocover --maxtest=4 --depth=2

In general, you must run the following command:

    $ python <path to randomtester> --nocover --maxtest=<m> --depth=<n>

## SQL Syntax ##

**TODO:** introduction to section

The structured query language (SQL) consists of two sublanguages: the data
definition language (DDL) and the data manipulation language (DML). Concrete
syntax shared by the DDL and DML is given by the following grammar.

    <letter>  ::= a | b | ... | z
    <digit>   ::= 0 | 1 | ... | 9
    <space>   ::= _ | \t | \n | \r
    <letters> ::= <letter>
                | <letter> <letters>
    <digits>  ::= <digit>
                | <digit> <digits>
    <sep>     ::= ε
                | <space> <sep>
    <comma>   ::= <sep> , <sep>
    <left>    ::= ( <sep>
    <right>   ::= <sep> )
    <name>    ::= <letters>
                | <letters> <digits> <name>
    <names>   ::= <name>
                | <name> <comma> <names>
    
    <num>     ::= ... | -1 | 0 | 1 | ...
    <bool>    ::= true | false
    <char>    ::= <letter> | <digit> | <space>
    <nums>    ::= <num>
                | <num> <comma> <nums>
    <chars>   ::= ε
                | <char> <chars>
    <str>     ::= " <chars> "
    <place>   ::= ? | : <name>
    <val>     ::= <num> | <bool> | <str> | <name> | <place>
    <op1>     ::= - | NOT
    <op2>     ::= + | - | * | / | AND | OR | == | <> | < | >
    <expr>    ::= <val>
                | <left> <expr> <right>
                | <op1> <sep> <expr>
                | <expr> <sep> <op2> <sep> <expr>
    <exprs>   ::= <expr>
                | <expr> <comma> <exprs>

The concrete syntax for DDL statements is given by the following grammar:

**TODO:** write grammar for DDL

The concrete syntax for DML statements is given by the following grammar:

    <which>   ::= ε | ALL | DISTINCT
    <which'>  ::= <sep> <which> <sep>
    <cols>    ::= * | <nums> | <names>
    <cols'>   ::= <sep> <cols> <sep>
    
    <where>   ::= ε | WHERE <sep> <expr>
    <where'>  ::= <sep> <where> <sep>
    <having>  ::= ε | HAVING <sep> <expr>
    <having'> ::= <sep> <having> <sep>
    <group>   ::= ε | GROUP BY <sep> <exprs> <having'>
    <group'>  ::= <sep> <group> <sep>
    <order>   ::= ε | ORDER BY <sep> <cols>
    <order'>  ::= <sep> <order> <sep>
    <limit>   ::= ε | LIMIT <sep> <expr>
    <limit'>  ::= <sep> <limit> <sep>
    
    <as>      ::= ε | AS <sep> <name>
    <table>   ::= <left> <select> <right> | <name>
    <from>    ::= ε | FROM <sep> <table> <sep> <as>
    <from'>   ::= <sep> <from> <as'>
    
    <select>  ::= SELECT <which'> <cols'> <from'> <where'> <group'> <order'> <limit'>

**TODO:** finish syntax
