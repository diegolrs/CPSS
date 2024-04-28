str = "getset float value;".split()

if str[len(str)-1][-1] == ';':
    str[len(str)-1] = str[len(str)-1][:-1]

__var_type = str[1]
__var_name = str[2]

__class_name = 'CLASS'
__get_str_hpp = f'{__var_type} get{__var_name.capitalize()}();' 
__set_str_hpp = f'void set{__var_name.capitalize()}({__var_type} {__var_name});'
__get_str_cpp = f'{__var_type} {__class_name}::get{__var_name.capitalize()}()'+'{ return this.' + f'{__var_name};'+' }' 
__set_str_cpp = f'void {__class_name}::set{__var_name.capitalize()}({__var_type} {__var_name})'+'{ this.' + f'{__var_name} = {__var_name};'+' }' 

print(__get_str_hpp)
print(__set_str_hpp)
print(__get_str_cpp)
print(__set_str_cpp)