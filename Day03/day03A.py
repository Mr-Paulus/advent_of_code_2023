from pathlib import Path

def Check(Poss, CheckPoss, RowSize, Max, CheckList, SearchList): 
    Poss = Poss + CheckPoss
    Down = Poss - RowSize
    Up = Poss + RowSize

    if Poss > Max or Poss < 0 or CheckList[Poss]  == '\n':
        return False
    
    else:
        #Check Next
        if CheckList[Poss] in SearchList:
            return True      

        #Check Down
        if  Down >= 0:
            if CheckList[Down] in SearchList:
                return True    

        #Check Up 
        if Up <= Max:
            if CheckList[Up] in SearchList:
                return True           

    return False

def CheckSymboUpDown(Poss, RowSize, Max, CheckList, SearchList):
    Down = Poss - RowSize 
    Up = Poss + RowSize

    #CheckDown
    if Down  >= 0:
        if CheckList[Down] in SearchList:
            return True

    #ChechUp
    if Up  <= Max:
        if CheckList[Up] in SearchList:
            return True        

    #No match
    return False

def CheckTotal(RowSize, Max, CheckList, SearchList, Start, End):    
    #Check left
    if Check(Start, -1, RowSize, Max, CheckList, SearchList):
        return True
    
    #Check middel
    for x in range(Start, End + 1):
        if CheckSymboUpDown(x, RowSize, Max, CheckList, SearchList):
            return True
    #Check Right
    if Check(End, 0, RowSize, Max, CheckList, SearchList):
        return True
    
    return False

#Gets score of list
def CalculateScore(Input):
    Score = 0
    Number = False
    Word = ''
    SymbolList = ['*', '-', '$', '@', '=', '#', '+', '/', '%', '&']
    First  = 0

    #Get input puzzle
    p = Path(__file__).with_name(Input)
    with p.open('r') as f:
        InputPuzzle = f.read()

    #Loop trough list to get numbers
    for x in range(0, len(InputPuzzle)):
        if InputPuzzle[x] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            Word += InputPuzzle[x]
            
            if Number == False:
                Number = True
                First = x
        else:
            if Word != '' and Number:
                if CheckTotal(141, len(InputPuzzle), InputPuzzle, SymbolList, First, x):
                    Score += int(Word)
            
            Word = ''
            Number = False

    #Check last edge number
    if Number:
        if CheckTotal(141, len(InputPuzzle), InputPuzzle, SymbolList, First, len(InputPuzzle)):
            Score += int(Word)

    
    return(Score)
        

print(CalculateScore('day03input.txt'))

