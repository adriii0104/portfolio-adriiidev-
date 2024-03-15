import random
import string


class GeneradorDeCodigos:
    def __init__(self) -> None:
        self.lenght = random.randint(4, 8)
        
        
    def stringcode(self) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=self.lenght))
    
    
    def intcode(self) -> int:
        return random.randint(1000, 9999)
    