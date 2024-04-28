import os
from FileHandler import FileHandler
from Generator import Generator
from Lexic import Lexic
from TokenClassf import TokenClassf

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def generate(generator, lexic, cppss_file_addr):
    program = file_handler.read(cppss_file_addr)
    lexic_output = lexic.generate_output(program)   
    generator.generate(lexic_output, program)
    file_handler.write(lexic_output, f'lexic-outputs/{generator.get_class_name(lexic_output)}.txt',sep='\n')

lexic = Lexic()
file_handler = FileHandler()
generator = Generator(file_handler)

generate(generator, lexic, 'Item.cppss')