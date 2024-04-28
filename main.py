import os
from FileHandler import FileHandler
from Generator import Generator
from Lexic import Lexic
from Parser import Parser

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

lexic = Lexic()
parser = Parser()
file_handler = FileHandler()
generator = Generator(file_handler)
cppss_file_addr = 'Item.cppss'

program = file_handler.read(cppss_file_addr)
lexic_output = lexic.generate_output(program)   
parser.validate(lexic_output)
generator.generate(lexic_output, program)
file_handler.write(lexic_output, f'lexic-outputs/{generator.get_class_name(lexic_output)}.txt',sep='\n')