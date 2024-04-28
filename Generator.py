from GetSetHandler import GetSetHandler
from TokenClassf import TokenClassf

class Generator:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.getset_handler = GetSetHandler()

    def generate(self, lexic_output, program):
        __cpp_code = self.generate_cpp(lexic_output)
        __hpp_code = self.generate_hpp(program)
        __class_name = self.get_class_name(lexic_output).strip()

        __res = self.getset_handler.handle(__cpp_code, __hpp_code, __class_name)
        __cpp_code, __hpp_code = __res[0], __res[1]

        self.file_handler.write(__cpp_code.strip(), f'{__class_name}.cpp')
        self.file_handler.write(__hpp_code.strip(), f'{__class_name}.hpp')

    #use lexic output
    def get_class_name(self, lexic_output):
        i = 0
        while i < len(lexic_output):
            if lexic_output[i][1] ==  TokenClassf.CLASS:
                return lexic_output[i+1][0]
            i += 1
        return 'default'

    #use lexic output
    def generate_cpp(self, output):
        class_name = ''
        cpp_code = ''

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
        return cpp_code

    #use program text
    def generate_hpp(self, program):
        hpp_code = '#pragma once\n'
        i = 0
        while i < len(program):
            #method
            if program[i] == '(':
                while program[i] != ')':
                    hpp_code += program[i]
                    i += 1
                i += 1
                hpp_code += ');'

                if program[i] != ';':
                    while program[i] != '{':
                        i += 1
                    while program[i] != '}':
                        i += 1
                    i += 1
            else:
                hpp_code += program[i]
                i += 1
        return hpp_code