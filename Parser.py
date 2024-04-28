from TokenClassf import TokenClassf

class Parser:
    def __init__(self):
        pass

    #validate getset
    def validate(self, lexic_output):
        i = 0
        while i < len(lexic_output):
            if lexic_output[i][1] == TokenClassf.GETSET:
                if lexic_output[i+1][1] != TokenClassf.IDENTIFIER or lexic_output[i+2][1] != TokenClassf.IDENTIFIER:
                    exit(-1)
            i += 1
