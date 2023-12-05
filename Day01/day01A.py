from pathlib import Path

def GetDigit(sentence):
    First = 0
    Last = 0

    for x in range(0, len(sentence)):
        if(sentence[x].isnumeric()):
            First = sentence[x]
            break

    for x in range(len(sentence)-1, -1, -1):
        if(sentence[x].isnumeric()):
            Last = sentence[x]
            break
    
    return int(First + Last)

#Get input puzzle
p = Path(__file__).with_name('day01input.txt')
with p.open('r') as f:
    InputPuzzle = f.read()

Score = 0

while (len(InputPuzzle) > 0):
    Score += GetDigit(InputPuzzle[0:InputPuzzle.find("\n" )])
    InputPuzzle = InputPuzzle[InputPuzzle.find("\n" )+1:]

print(Score)