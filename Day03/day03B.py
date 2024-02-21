from pathlib import Path

def FindNumberUpDown(CheckList ,CheckPoss, RowSize, Max, DontCheck, SearchList):
    Down = CheckPoss - RowSize 
    Up = CheckPoss + RowSize
    Right = CheckPoss + 1
    Left = CheckPoss - 1
    LeftDown = CheckPoss - RowSize - 1
    RightDown = CheckPoss - RowSize + 1
    LeftUp = CheckPoss + RowSize -1
    RightUp = CheckPoss + RowSize + 1

    #CheckDown
    if Down  >= 0:
        if CheckList[Down] in SearchList and Down not in DontCheck:
            return Down
        
        #CheckRightDown
        if CheckList[RightDown] in SearchList and RightDown not in DontCheck:
            return RightDown
                
    #ChechUp
    if Up  <= Max:
        if CheckList[Up] in SearchList and Up not in DontCheck:
            return Up   
        
        #ChecLeftUp
        if CheckList[LeftUp] in SearchList and LeftUp not in DontCheck:
            return LeftUp            

    #CheckRight
    if Right <= Max:
        if CheckList[Right] in SearchList and Right not in DontCheck:
            return Right
    #CheckLeft
    if Left >= 0:
        if CheckList[Left] in SearchList and Left not in DontCheck:
            return Left

    #CheckRightUp
    if CheckList[RightUp] in SearchList and RightUp not in DontCheck and RightUp <= RightUp:
        return RightUp      

    #CheckLeftDown 
    if CheckList[LeftDown] in SearchList and LeftDown not in DontCheck and LeftDown >= 0:
        return LeftDown
    
    return -1

def GetNumber(CheckPoss, Check, SearchList, Max):
    ReturnWord = ''
    ReturnDontCheck = []

    #CheckLeft
    if CheckPoss > -1:
        for x in range(CheckPoss, -1, -1):
            if Check[x] in SearchList:
                ReturnWord = Check[x] + ReturnWord
                ReturnDontCheck.append(x)

            else:
                break

    #CheckRight
    if CheckPoss + 1 <= Max:
        for x in range(CheckPoss + 1, Max + 1):
            if Check[x] in SearchList:
                ReturnWord = ReturnWord + Check[x]
                ReturnDontCheck.append(x)

            else:
                break

    return [int(ReturnWord), ReturnDontCheck]

def CalculateScore(Input):
    Search = ['0', '1', '2', '3', '4' ,'5' ,'6', '7', '8', '9']
    Score = 0

    #Get input puzzle
    p = Path(__file__).with_name(Input)
    with p.open('r') as f:
        InputPuzzle = f.read()

    Rowsize = InputPuzzle.find('\n') + 1
    MaxSize = len(InputPuzzle)

    #Find all gears
    for x in range(0, len(InputPuzzle)):
        if InputPuzzle[x] == '*':
            Pos1 = FindNumberUpDown(InputPuzzle ,x, Rowsize, MaxSize, [], Search)

            if (Pos1 != -1):
                Number1 = GetNumber(Pos1, InputPuzzle, Search, MaxSize)
                Pos2 = FindNumberUpDown(InputPuzzle ,x, Rowsize, MaxSize, Number1[1], Search)

                if Pos2 > -1:
                    Number2 = GetNumber(Pos2, InputPuzzle, Search, MaxSize)
                    Score += Number1[0] * Number2[0]

    return Score                     
                

print(CalculateScore('day03input.txt'))