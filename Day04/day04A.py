from pathlib import Path

def CheckCardScore(Card, Points):    
    ScorePick = -1
    ScoreMatch = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 
                  65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]

    for x in Card:
        ScorePick += Points.count(x)
        
    if ScorePick >= 0:
        return ScoreMatch[ScorePick]
    else:
        return 0
    
def GetNumber(Input, Startpoint, Numbers):
    ReturnList = []

    for x in range(0, Numbers):
        Start = x * 3
        End = Start + 2

        Numb = Input[Startpoint + Start:Startpoint + End]

        if Numb[0] == ' ':
            ReturnList.append(int(Numb[1]))
        else:
            ReturnList.append(int(Numb))

    return ReturnList

def GetScore(Input):
    #Get input puzzle
    p = Path(__file__).with_name(Input)
    with p.open('r') as f:
        InputPuzzle = f.read()

    FinalScore = 0

    while InputPuzzle.find('\n') > -1:

        Row = InputPuzzle[0: InputPuzzle.find('\n')]

        CardList = GetNumber(Row, 10, 10)
        PointList = GetNumber(Row, 42, 25)
        FinalScore += CheckCardScore(CardList, PointList)

        InputPuzzle = InputPuzzle[InputPuzzle.find('\n')+ 1:]

    
    return(FinalScore)


print(GetScore('day04input.txt'))