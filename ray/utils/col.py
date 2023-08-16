import pprintpp

class col:
    '''Print colours. Use example: f'{bcolors.OKGREEN}coloured text' '''
    def __init__(self):
        self.HEADER = '\033[95m'
        self.BLUE = '\033[94m'
        self.CYAN = '\033[96m'
        self.GREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.GREENBG = '\033[42m\033[30m'

    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREENBG = '\033[42m\033[30m'

    def printh(self, str: str):
        print(f'{self.HEADER}{str}')
    
    def printb(self, str: str):
        print(f'{self.BLUE}{str}')
    
    def printc(self, str: str):
        print(f'{self.CYAN}{str}')
    
    def printg(self, str: str):
        print(f'{self.GREEN}{str}')
    
    def printw(self, str: str):
        print(f'{self.WARNING}{str}')
    
    def printf(self, str: str):
        print(f'{self.FAIL}{str}')
    
    def printn(self, str: str):
        print(f'{self.ENDC}{str}')
    
    def printbb(self, str: str):
        print(f'{self.BOLD}{str}')

    def printu(self, str: str):
        print(f'{self.UNDERLINE}{str}')
    
    def gv(self, str: str, val):
        self.printg(f'{str} {self.ENDC}{val}')

    # Pretty Printing Data
    def pprint(self, str: str):
        pprintpp.pprint(str)

p = col()