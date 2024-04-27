import os
from Lexic import Lexic
from TokenClassf import TokenClassf

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def read_file(address):
    with open(address) as f:
        data = f.read()
    return data

def write_file(output, addr,sep=''):
    with open(addr, 'w') as f:
        for item in output:
            f.write(str(item)+sep)

lexic = Lexic()
program = read_file('code2.cppss')
output = lexic.generate_output(program)
write_file(output, 'lexic.txt',sep='\n')


class_name = ''
methods = []
cpp_code = ''

#---------------CPP---------------
#class name
i = 0
while i < len(output):
#for i in range(len(output)):
    if output[i][1] ==  TokenClassf.CLASS:
        class_name = output[i+1][0]
        cpp_code += f'#include "{class_name}.hpp"\n\n'
    
    #method
    elif output[i][0] ==  '(':
        __method_name = ''
        __method_return = ''
        __method_params = ''
        __method_code = ''

        #constructor
        __method_name = output[i-1][0]
        __method_return = '' if output[i-1][0] == class_name else output[i-2][0]

        #inside parentesis
        i += 1
        while output[i][0] != ')':
            __method_params += output[i][0] + " "
            i += 1

        i += 2 #consume ) and {
        while output[i][0] != '}':
            #break line
            if output[i][2] != output[i-1][2]:
                __method_code += "\n\t"

            __method_code += output[i][0] + " "
            i += 1
        
        __method_return = __method_return.rstrip()
        __method_name = __method_name.rstrip()
        __method_params = __method_params.rstrip()
        __method_code = __method_code.rstrip()

        if __method_return != '':
            __method_return += " "
        cpp_code += f"{__method_return}{class_name}::{__method_name}({__method_params})"+'\n{\t'+__method_code+'\n}\n\n'

    i += 1

write_file(cpp_code.strip(), 'code.cpp')

#----------------- HPP -------------------
hpp_code = '#pragma once\n'
i = 0
while i < len(program):
    #method
    if program[i] == '(':
        while program[i] != ')':
            hpp_code += program[i]
            i += 1
        hpp_code += program[i] + ';'
        i += 1

        while program[i] != '{':
            i += 1
        while program[i] != '}':
            i += 1
        i += 1    

        #formatting
        count = 0
        while program[i] in ['\n']:
            i += 1
            count += 1
        if count > 0:
            hpp_code += '\n'

    else:
        hpp_code += program[i]
        i += 1

write_file(hpp_code.strip(), 'code.hpp')