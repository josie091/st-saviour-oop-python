
class Hair:
    def __init__(self, color: str, length: float, curly: bool):
        self.color = color
        self.length = length
        self.curly = curly

    def style(self) -> str:
        if self.curly:
            return f'you style the curly {self.color} hair that is {self.length} inches long!'
        else:
            return f'you style the straight {self.color} hair that is {self.length} inches long!'

if __name__ == '__main__':
    laren = Hair('brown', 20, False)
    print(laren.style())
    #this is the first instance
    josie = Hair('brown', 21, False)
    print(laren.style())
    #this is the second instance 

    Peyton = Hair('Blonde', 15, False)
    print(Peyton.style())
    #this is the third instance