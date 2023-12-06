from pathlib import Path

#Gets first digit or word number and returns number as string
def GetDigitAsc(Sentence):
    Size = len(Sentence)

    for x in range(0, Size):
        #Check if its a digit
        if(Sentence[x].isnumeric()):
            return Sentence[x]
        #Checks 5 letter words
        if (x + 5 <= Size):
            if Sentence[x:x + 5] == 'eight':
                return '8'
            elif Sentence[x:x + 5] == 'seven':
                return '7'
            elif Sentence[x:x + 5] == 'three':
                return '3'
        #Checks 4 letter words            
        if (x + 4 <= Size):
            if Sentence[x:x + 4] == 'nine':
                return '9'
            elif Sentence[x:x + 4] == 'five':
                return '5'
            elif Sentence[x:x + 4] == 'four':
                return '4'
        #Checks 3 letter words                      
        if (x + 3 <= Size):
            if Sentence[x:x + 3] == 'six':
                return '6'
            elif Sentence[x:x + 3] == 'two':
                return '2'
            elif Sentence[x:x + 3] == 'one':
                return '1'                       

#Gets last digit or word number and returns number as string                        
def GetDigitDesc(Sentence):

    for x in range(len(Sentence)-1, -1, -1):
        #Check if its a digit        
        if(Sentence[x].isnumeric()):
            return Sentence[x]
        #Checks 5 letter words        
        if (x - 5 > -1):
            if Sentence[x - 4: x+1] == 'eight':
                return '8'
            elif Sentence[x - 4: x+1] == 'seven':
                return '7'
            elif Sentence[x - 4: x+1] == 'three':
                return '3'        
        #Checks 4 letter words            
        if (x - 4 > -1):
            if Sentence[x - 3: x+1] == 'nine':
                return '9'
            elif Sentence[x - 3: x+1] == 'five':
                return '5'
            elif Sentence[x - 3: x+1] == 'four':
                return '4'       
        #Checks 3 letter words                 
        if (x - 3 > -1):            
            if Sentence[x - 2: x+1] == 'six':
                return '6'
            elif Sentence[x - 2: x+1] == 'two':
                return '2'
            elif Sentence[x - 2: x+1] == 'one':
                return '1'   

def CalculateScore(Input):
    #Get input puzzle
    p = Path(__file__).with_name(Input)
    with p.open('r') as f:
        InputPuzzle = f.read()

    Score = 0

    #Loops trough input list and adds score
    while (len(InputPuzzle) > 0):
        string = InputPuzzle[0:InputPuzzle.find("\n" )]
        InputPuzzle = InputPuzzle[InputPuzzle.find("\n" )+1:]    

        FirstDigit = GetDigitAsc(string)
        LastDigit = GetDigitDesc(string)

        Score += int(FirstDigit + LastDigit)

    return Score


print(CalculateScore('day01input.txt'))