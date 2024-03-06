from pathlib import Path
import time

start = time.time()

def Converter(List, Target):

    ReturnVal = Target

    for x in List:
        if x[1] <= Target and x[1] + (x[2] - 1) >= Target:
            
            ReturnVal = (x[0] + Target - x[1])            
            break
        
    return ReturnVal

def GetMap(List ,Start):
    ReturnList = []

    for x in range (0, Start):
        List = List[List.find('\n')+1: ]
    
    while List[0:1] in ['0', '1', '2', '3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']:
        AddToList = []

        NewList = List[0: List.find('\n')]

        for x in range(0, 2):

            AddToList.append(int(NewList[0: NewList.find(' ')]))
            NewList = NewList[NewList.find(' ')+1:]

        AddToList.append(int(NewList))
        ReturnList.append(AddToList)

        List = List[List.find('\n')+1:]

    return ReturnList
    
def GetScore(Input):
    #Get input puzzle
    p = Path(__file__).with_name(Input)
    with p.open('r') as f:
        InputPuzzle = f.read()

    LocationOut = []

    #Create list for seeds
    Seeds = InputPuzzle[InputPuzzle.find(' ')+1:  InputPuzzle.find('\n')]
    SeedList = []
    
    while Seeds.find(' ') > 0:
        SeedList.append(int(Seeds[0: Seeds.find(' ')]))
        Seeds = Seeds[Seeds.find(' ')+1:]

    SeedList.append(int(Seeds))

    #Get Almanac input
    Soil = GetMap(InputPuzzle, 3)
    Fertilizer = GetMap(InputPuzzle, 15)
    Water = GetMap(InputPuzzle, 33)
    Light = GetMap(InputPuzzle, 50)
    Temperature = GetMap(InputPuzzle, 97)
    Humidity = GetMap(InputPuzzle, 114)
    Location = GetMap(InputPuzzle, 139)

    #Convert seeds to location
    for x in SeedList:
        y = Converter(Soil, x)
        y = Converter(Fertilizer, y)
        y = Converter(Water, y)
        y = Converter(Light, y)
        y = Converter(Temperature, y)
        y = Converter(Humidity, y)
        y = Converter(Location, y)

        if LocationOut == []:
            LocationOut.append(y)
        elif LocationOut[0] > y:
            LocationOut[0] = y

    #Get lowest location and return
    return LocationOut[0]

print(GetScore('day05input.txt'))

end = time.time()

print(end - start)