from __future__ import division

# Uncomment the line below for readline support on interactive terminal
# import readline  
import re
from pyparsing import Word, alphas, ParseException, Literal, CaselessLiteral \
, Combine, Optional, nums, Or, Forward, ZeroOrMore, StringEnd, alphanums
import math

# Debugging flag can be set to either "debug_flag=True" or "debug_flag=False"
debug_flag=False

class sample:

	exprStack = []
	varStack  = []
	variables = {}
	opn = {}

	def pushFirst( self, str, loc, toks ):
	    self.exprStack.append( toks[0] )

	def assignVar( self, str, loc, toks ):
	    self.varStack.append( toks[0] )

	# Recursive function that evaluates the stack
	def evaluateStack(self, s ):
	  op = s.pop()
	  if op in "+-*/^":
	    op2 = self.evaluateStack( s )
	    op1 = self.evaluateStack( s )
	    return self.opn[op]( op1, op2 )
	  elif op == "PI" or op == "pi":
	    return math.pi
	  elif op == "E":
	    return math.e
	  elif re.search('^[a-zA-Z][a-zA-Z0-9_]*$',op):
	    if self.variables.has_key(op):
	      return self.variables[op]
	    else:
	      return 0
	  elif re.search('^[-+]?[0-9]+$',op):
	    return long( op )
	  else:
	    return float( op )

	# define grammar
	def defineGrammar(self, input_strings):
		point = Literal('.')
		e = CaselessLiteral('E')
		plusorminus = Literal('+') | Literal('-')
		number = Word(nums)
		#print "Nums", number 
		integer = Combine( Optional(plusorminus) + number )
		floatnumber = Combine( integer +
				       Optional( point + Optional(number) ) +
				       Optional( e + integer )
				     )

		ident = Word(alphas,alphanums + '_') 
		#print "ident", ident 
		plus  = Literal( "+" )
		minus = Literal( "-" )
		mult  = Literal( "*" )
		div   = Literal( "/" )
		lpar  = Literal( "(" ).suppress()
		rpar  = Literal( ")" ).suppress()
		addop  = plus | minus
		multop = mult | div
		expop = Literal( "^" )
		assign = Literal( "=" )

		expr = Forward()
		#print "Expr" , expr
		atom = ( ( e | floatnumber | integer | ident ).setParseAction(self.pushFirst) | 
			 ( lpar + expr.suppress() + rpar )
		       )
		
		factor = Forward()
		factor << atom + ZeroOrMore( ( expop + factor ).setParseAction( self.pushFirst ) )
		
		term = factor + ZeroOrMore( ( multop + factor ).setParseAction( self.pushFirst ) )
		expr << term + ZeroOrMore( ( addop + term ).setParseAction( self.pushFirst ) )
		bnf = Optional((ident + assign).setParseAction(self.assignVar)) + expr

		pattern =  bnf + StringEnd()
		#print "pattern" , pattern
		
		# map operator symbols to corresponding arithmetic operations
		self.opn = { "+" : ( lambda a,b: a + b ),
			"-" : ( lambda a,b: a - b ),
			"*" : ( lambda a,b: a * b ),
			"/" : ( lambda a,b: a / b ),
			"^" : ( lambda a,b: a ** b ) }
		exprns = input_strings.split(",")
		for input_string in exprns:
								
			self.exprStack = []
	    		self.varStack  = []
			if input_string != '':
			      # try parsing the input string
			      try:
				L=pattern.parseString( input_string )
				#print "L", L
			      except ParseException,err:
				L=['Parse Failure',input_string]	
			if debug_flag: print input_string, "->", L
			if len(L)==0 or L[0] != 'Parse Failure':
			  if debug_flag: print "exprStack=", self.exprStack
			 
			# calculate result , store a copy in ans , display the result to user
			  result=self.evaluateStack(self.exprStack)
			  self.variables['ans']=result
			  print input_string , "=" , result
			  
			# Assign result to a variable if required
			  if debug_flag: print "var=",self.varStack
			  if len(self.varStack)==1:
			    self.variables[self.varStack.pop()]=result
			  if debug_flag: print "variables=",self.variables
			else:
			  print 'Parse Failure'
			  print err.line
			  print " "*(err.column-1) + "^"
			  print input_string , "-" , err

	
#calc = sample()
#calc.defineGrammar(["3+7*12-4/2","3+2","quit"])

