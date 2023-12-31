from pathlib import Path

def CheckBag(Input):
    GivenPoint = int(Input[5:Input.find(':')])
    Input = Input[Input.find(':') + 2:]
    Point = True

    while (len(Input) > 0):

        MaxSize = len(Input)
        Red = -MaxSize
        Green = MaxSize
        Blue = MaxSize
        Low = MaxSize 
        RedCheck = False
        GreenCheck = False

        if (Input.find('red') > -1):
            Red = Input.find('red')
            
            if  Low > Red:
                Low = Red
                RedCheck = True
                GreenCheck = False
        
        if (Input.find('green') > -1):
            Green = Input.find('green')     

            if  Low > Green:
                Low = Green
                RedCheck = False
                GreenCheck = True

        if (Input.find('blue') > -1):
            Blue = Input.find('blue')  

            if  Low > Blue:
                Low = Blue   
                RedCheck = False
                GreenCheck = False

        if (RedCheck == True):
            if (int(Input[0:Low-1]) > 12):
                Point = False
                break
            Input = Input[Low+5:]


        elif (GreenCheck == True):
            if (int(Input[0:Low-1]) > 13):
                Point = False
                break
            Input = Input[Low+7:]
            
        else:
            if (int(Input[0:Low-1]) > 14):
                Point = False
                break      
            Input = Input[Low+6:]

    if (Point):
        return GivenPoint
    else:
        return 0
    
def CalculateScore(Input):
    Score = 0

    #Get input puzzle
    p = Path(__file__).with_name(Input)
    with p.open('r') as f:
        InputPuzzle = f.read()

    #Loops trough input list and adds score
    while (len(InputPuzzle) > 0):
        String = InputPuzzle[0:InputPuzzle.find("\n" )]
        InputPuzzle = InputPuzzle[InputPuzzle.find("\n" )+1:]    

        Score += CheckBag(String)

    return Score        

print(CalculateScore('day02input.txt'))
