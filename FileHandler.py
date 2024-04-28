class FileHandler:
    def __init__(self):
        pass

    def read(self, address):
        with open(address) as f:
            data = f.read()
        return data

    def write(self, output, addr,sep=''):
        with open(addr, 'w') as f:
            for item in output:
                f.write(str(item)+sep)