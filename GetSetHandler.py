class GetSetHandler:
    def __init__(self):
        pass

    #returns both strings handled
    def handle(self, cpp_code, hpp_code, class_name):
        __methods = self.__get_getset_usages(cpp_code, hpp_code)
        hpp_code = self.__remove_getset_usages(hpp_code)
        hpp_code = self.__add_methods_to_hpp(hpp_code, __methods)
        cpp_code = self.__add_methods_to_cpp(cpp_code, __methods, class_name)
        return [cpp_code, hpp_code]

    def __get_getset_usages(self, cpp_code, hpp_code):
        methods = []
        sequence = 'getset'
        sequence_index = 0
        i = 0

        while i < len(hpp_code):
            #detected sequence
            if sequence_index < len(sequence) and hpp_code[i] == sequence[sequence_index]:
                sequence_index += 1
            else:
                sequence_index = 0

            if sequence_index == len(sequence):
                i = i+1 #last char from getset
                i = i+1 #space

                __var_type = ''
                __var_name = ''

                while hpp_code[i] != ' ':
                    __var_type += hpp_code[i]
                    i += 1
                i += 1 #space

                while hpp_code[i] != ';':
                    __var_name += hpp_code[i]
                    i += 1
                i += 1 #;

                methods.append([__var_type.strip(), __var_name.strip()])
            i += 1
        return methods

    def __remove_getset_usages(self, hpp_code):
        return hpp_code.replace("getset ", '')

    def __add_methods_to_hpp(self, hpp_code, methods):
        __str = '\tpublic:'

        for method in methods:
            __str += f'\n\t\t{method[0]} get{method[1].capitalize()}();' 
            __str += f'\n\t\tvoid set{method[1].capitalize()}({method[0]} {method[1]});'

        __str += '\n};'
        return hpp_code.replace("};", __str)

    def __add_methods_to_cpp(self, cpp_code, methods, class_name):
        __str = ''

        for method in methods:
            #get
            __str += f'\n\n{method[0]} {class_name}::get{method[1].capitalize()}()'
            __str += '{ return this.' + f'{method[1]};'+' }' 

            #set
            __str += f'\n\nvoid {class_name}::set{method[1].capitalize()}({method[0]} {method[1]})'
            __str += '{ this.' + f'{method[1]} = {method[1]};'+' }' 

        return cpp_code.strip() + __str