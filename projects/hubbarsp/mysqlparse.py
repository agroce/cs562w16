# This module contains helper functions used by testing harness for sqlparse.
import sqlparse
from sqlparse import tokens
from sqlparse import compat

# Builds a pretty print string for the given parse tree.
def pretty(parsed):
  def helper(parsed, i = 0):
    result = '%s%s \'%s\'\n' % (' ' * (2 * i), parsed._get_repr_name(), parsed._get_repr_value())
    if parsed.is_group():
      for t in filter(lambda t: not t.is_whitespace(), parsed.tokens):
        result += helper(t, i + 1)
    return result
  return '\n' + helper(parsed)

if __name__ == '__main__':
  stmt1 = 'select * from foo where bar = "baz";'
  stmt2 = 'select A.a, A.b from A;'
  stmt3 = 'select a, b from (select * from A where c < 1);'
  parsed1 = sqlparse.parse(stmt1)[0]
  parsed2 = sqlparse.parse(stmt2)[0]
  parsed3 = sqlparse.parse(stmt3)[0]
  print pretty(parsed1)
  print pretty(parsed2)
  print pretty(parsed3)
  print compat.u(parsed1) == stmt1
  print parsed1.get_type() == 'SELECT'
