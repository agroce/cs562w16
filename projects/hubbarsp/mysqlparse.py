# this is a temp file for learning sqlparse
import sqlparse
from sqlparse import tokens
from sqlparse import compat

def pretty(parsed):
  def helper(parsed, i = 0):
    result = '%s%s \'%s\'\n' % (' ' * (2 * i), parsed._get_repr_name(), parsed._get_repr_value())
    if parsed.is_group():
      for t in filter(lambda t: not t.is_whitespace(), parsed.tokens):
        result += helper(t, i + 1)
    return result
  return '\n' + helper(parsed)

def walk(parsed):
  return parsed

def forwards(stmt, i = 0):
  return sqlparse.parse(stmt)[i]

def backwards(parsed):
  return compat.u(parsed)

if __name__ == '__main__':
  parsed1 = forwards('select * from foo where bar = "baz";')
  parsed2 = forwards('select A.a, A.b from A;')
  parsed3 = forwards('select a, b from (select * from A where c < 1);')
  print pretty(parsed1)
  print pretty(parsed2)
  print pretty(parsed3)
  print backwards(parsed1)
