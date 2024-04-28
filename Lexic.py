from TokenClassf import TokenClassf

class Lexic:
    def __init__(self):
        self.inital_state = 0
        self.current_state = self.inital_state

        self.line_count = 1
        self.include = {8}
        self.classes = {13}
        self.parentesis = {14,15}
        self.braces = {16,17}
        self.identifier = {18}
        self.getset = {25}

        self.word_verified = "" #uptate when complete to verify a word
        self.output = []

        self.ignorables = {' ', '\n', '\r', '\t'}
        self.open_brackeys_count = 0 #used when has a comment inside comment

    def restart(self):
        self.current_state = self.inital_state
        self.word_verified = ""

    def transition(self, symbol):
        should_ignore = self.current_state == self.inital_state and symbol in self.ignorables

        if(not should_ignore):
            self.word_verified += symbol

        if self.current_state != self.inital_state and symbol in self.ignorables:
            self.crash(symbol)
        elif self.current_state == self.inital_state:
            if symbol in self.ignorables:
                self.current_state = self.inital_state
            elif symbol == '#':
                self.current_state = 1
            elif symbol == 'c':
                self.current_state = 9
            elif symbol == '(':
                self.current_state = 14
            elif symbol == ')':
                self.current_state = 15
            elif symbol == '{':
                self.current_state = 16
            elif symbol == '}':
                self.current_state = 17
            elif symbol == 'g':
                self.current_state = 20
            else:
                self.current_state = 18

        #include
        elif self.current_state in [1,2,3,4,5,6,7,8]:
            self.process_include(symbol)

        #class
        elif self.current_state in [9,10,11,12,13]:
            self.process_class(symbol)

        #getset
        elif self.current_state in [20,21,22,23,24,25]:
            self.process_getset(symbol)

        #(){}
        elif self.current_state in [14,15,16,17]:
            self.crash(symbol)

        #Any text
        elif self.current_state == 18:
            if symbol in self.ignorables or (symbol in ['(',')','{','}']):
                self.crash(symbol)

    #get token type based on current state
    def get_token_type(self):
        if self.current_state in self.classes:
            return TokenClassf.CLASS
        elif self.current_state in self.include:
            return TokenClassf.INCLUDE
        elif self.current_state in self.parentesis:
            return TokenClassf.PARENTESIS
        elif self.current_state in self.braces:
            return TokenClassf.BRACES
        elif self.current_state in self.getset:
            return TokenClassf.GETSET
        elif self.current_state in self.identifier:
            return TokenClassf.IDENTIFIER
        return TokenClassf.INVALID

    def crash(self, symbol):                
        token_type = self.get_token_type()
        return_symbol = True

        _word_displacement = -1 if return_symbol else 0
        self.word_verified = self.word_verified[:len(self.word_verified)+_word_displacement]
        self.output.append([self.word_verified, token_type, self.line_count])

        self.restart()
        if return_symbol == True:
            self.transition(symbol)

    def generate_output(self, word):
        self.restart()
        self.output = []

        #TOKEN - CLASSIFICATION - LINE
        for char in word:
            self.transition(char)
            
            if char == '\n':
                self.line_count += 1

        #make sure last processing logic is finished
        self.transition(' ')

        return self.output

    def process_include(self, symbol):
        if symbol in self.ignorables:
            self.crash(symbol)
        elif self.current_state == 1 and symbol == 'i':
            self.current_state = 2
        elif self.current_state == 2 and symbol == 'n':
            self.current_state = 3
        elif self.current_state == 3 and symbol == 'c':
            self.current_state = 4
        elif self.current_state == 4 and symbol == 'l':
            self.current_state = 5
        elif self.current_state == 5 and symbol == 'u':
            self.current_state = 6
        elif self.current_state == 6 and symbol == 'd':
            self.current_state = 7
        elif self.current_state == 7 and symbol == 'e':
            self.current_state = 8
        else:
            self.current_state = 18

    def process_class(self, symbol):
        if symbol in self.ignorables:
            self.crash(symbol)
        elif self.current_state == 9 and symbol == 'l':
            self.current_state = 10
        elif self.current_state == 10 and symbol == 'a':
            self.current_state = 11
        elif self.current_state == 11 and symbol == 's':
            self.current_state = 12
        elif self.current_state == 12 and symbol == 's':
            self.current_state = 13
        else:
            self.current_state = 18

    def process_getset(self, symbol):
        init = 20 #after g
        quote = 'etset'

        if symbol in self.ignorables:
            self.crash(symbol)
        elif quote[self.current_state-init] == symbol:
            self.current_state += 1
        else:
            self.current_state = 18