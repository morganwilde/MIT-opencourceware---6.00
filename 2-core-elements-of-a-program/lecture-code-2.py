# scalar types

type(2)
#<type 'int'>
type(2.0)
#<type 'float'>
type(True)
#<type 'bool'>
type(None)
#<type 'NoneType'>

# non-scalar types

type('a')
#<type 'str'>

# expressions

3+2
#5
3/2
#1
3.0/2.0
#1.5
'a'+'b'
#'ab'

# static semantics error
'a' + 3
#TypeError: cannot concatenate 'str' and 'int' objects
'a' + '3'
'a' + str(3)
#'a3'
int('3')
#3
int(2.1)
int(2.9)
#2 (just trunctates the float)
