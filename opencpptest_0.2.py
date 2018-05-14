#coding:UTF-8
"""
windows 64bit， python2.7 32bit
"""

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
inputs = []
s = Solver()
s.add(x1 > x2, x1 >= 10, (2 * x1 + x2) == 40, (x1 - x2) == 5)
s.check()
m = s.model()
inputs.append(m)


import sys,os
sys.path.append(os.path.join(os.getcwd(), 'clang'))
from clang import cindex #llvm3.7 32bit
cindex.Config.set_library_file(os.path.join(os.getcwd(), r'clang/libclang.dll'))
def dumpnode(node, indent):
    if node.kind == cindex.CursorKind.FUNCTION_DECL:
        #print ' '*indent, '{},{},{},{},{}'.format(str(node.kind), node.spelling, node.location, node.displayname, node.result_type.kind)
        typekind = {"TypeKind.VOID":"void"}
        return str(node.spelling), typekind[str(node.result_type.kind)]+" "+node.displayname

    for i in node.get_children():
        return dumpnode(i, indent+2)

index = cindex.Index.create()
path = os.path.join(os.getcwd(), r'test1.c')
tu = index.parse(path)

template_include = '#include "gtest/gtest.h"\n\n'
template_decls = ''
template_tests ="""TEST(%s, %s){
    %s(%s, %s);
}

"""
funname, template_decls = dumpnode(tu.cursor, 0)
def write_unittest():
    with open(os.path.join(os.path.join(os.getcwd(), 'unittest'), 'test_{}.c'.format('test')), 'w+') as f:
        f.write(template_include+template_decls+';\n')
        for num, para in enumerate(inputs):
            f.write(template_tests % (funname.upper(), str(num), funname, para[x1], para[x2]))

write_unittest()
