#coding:UTF-8

"""test1.c样本
#include<stdio.h>
void test1(int x1, int x2){
    if(x1 > x2)
        if(x1 >= 10)
            if((2 * x1 + x2) == 40)
                if((x1 - x2) == 5)
                    printf("Solved!");
}
"""

from z3 import *
x1 = Int('x1')
x2 = Int('x2')
solve(x1 > x2, x1 >= 10, (2 * x1 + x2) == 40, (x1 - x2) == 5)  #===> (15, 10)

from cffi import *
ffi = FFI()
ffi.cdef("void test1(int x1, int x2);")
import os
file_dir = os.path.abspath(".")
lib = ffi.verify('#include <test1.c>', include_dirs=[file_dir], library_dirs=[file_dir])
lib.test1(15, 10)