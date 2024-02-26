from pathlib import Path

def CheckCardScore(Card, Points):    
    ScorePick = 0

    for x in Card:
        ScorePick += Points.count(x)
        
    return ScorePick
    
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

    TotalCards = 0
    List = []
    CardMulti = 0
    ListSize = 0
    LineCheck = 0

    while InputPuzzle.find('\n') > -1:
        #Get cards and calculate score
        Row = InputPuzzle[0: InputPuzzle.find('\n')]
        CardList = GetNumber(Row, 10, 10)
        PointList = GetNumber(Row, 42, 25)
        Add = CheckCardScore(CardList, PointList)

        #Append list or ad extra card
        if LineCheck + 1 > ListSize:
            List.append(1)
            ListSize += 1
        else:
            List[LineCheck] += 1

        CardMulti = List[LineCheck]
        TotalCards += CardMulti
        
        #Add cards
        for x in range(1, Add + 1):
        
            if x + LineCheck >= ListSize:
                List.append(CardMulti)
                ListSize += 1
            else:
                List[x + LineCheck] += CardMulti
        
        #Get next card
        LineCheck += 1
        InputPuzzle = InputPuzzle[InputPuzzle.find('\n')+ 1:] 

    return TotalCards
     
print(GetScore('day04input.txt'))