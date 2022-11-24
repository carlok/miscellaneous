from mlib import *

@mdec('warning')
def my_function(a):
    return a / 0

my_function(1)