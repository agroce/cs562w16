## Project Proposal ##

My project proposal is to use the Template Scripting Testing Language (TSTL) to
define a test harness for the `sqlparse` Python module. The module provides a
parser for SQL statements. The parser takes a string for one or more SQL
statements and returns a tuple of objects for the abstract syntax trees (ASTs)
of the SQL statements. The module also provides classes and methods for
analyzing the ASTs of SQL statements.

The parser provided by the module will be tested for correctness. The parser is
considered correct if it returns the ASTs of the input SQL statements, for any
standard SQL statements. The XML example will be used to guide the initial
design.

**TODO:** describe subset of SQL to test

The module is compatible with Python 2.7 and 3 and is released under the terms
of the BSD 2-clause license. The project page for the module is located at
https://github.com/andialbrecht/sqlparse. The module can be installed in several
ways. One way to install the module is using pip from the command line
interface:

    $ pip install sqlparse

**TODO:** describe other ways to install module
