

def printLine(count:int, thickness:int | None=1, char:str | None="-"):
    for i in range(thickness):
        print(char*count)
    
    