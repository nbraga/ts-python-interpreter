import marshal, struct,sys #, py_compile

# this script generates expected outputs for unit tests
# of MarshalParser.ts, in the format:
# data/[module]/[function_under_test]
# ex: data/marshal-parser/typeInt.pyc

PATH = "data/module_marshal-parser/"
#inputs
INT = 3
INT_64 = 9392468011745350111L
FLOAT = 0.125
B_FLOAT = 00111110000000000000000000000000 #0.125
COMPLEX = complex(3,5)
#B_COMPLEX = 3
LONG = type(sys.maxint + 1)
STRING = "racecar"
#STRING_REF = id(STRING)
UNICODE = STRING.decode(encoding='UTF-8')
TUPLE = tuple([STRING,INT])
LIST = [FLOAT,LONG]
DICT = dict(one=STRING,two=FLOAT,three=TUPLE)
FROZEN_SET = frozenset("a")
#CODE_OBJ = 3

inputs = [INT,INT_64,FLOAT,B_FLOAT,COMPLEX,B_COMPLEX,
	  LONG,STRING,STRING_REF,UNICODE,TUPLE,
    	  LIST,DICT,FROZEN_SET,CODE_OJ]

for i in inputs:
	fo = open(PATH+i+".pyc","wb")
	fo.write(marshal.dumps(i))
	fo.close()

#@TODO(Nick): for testing on more realistic pycs
#py_compile.compile('pyc_for_integration_tests');

