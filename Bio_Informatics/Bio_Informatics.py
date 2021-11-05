#Programming Assignment (due Nov 18): 
#   Jonathan Dao
#   11/2/21
#    Write a program to calculate the edit distance between two words and output both the matrix of distance calculation and an alignment that demonstrates the result. 
#    Your program should ask for input of two words, calculate the edit distance, output the matrix of calculation and an alignment that verifies the edit distance. 
#    You may use any programming language that you are most familiar. 
#    In front of your submission you should include a paragraph of comments describing how I can compile and test your program, 
#    including the required tools/environment. 
#    MATLAB is not acceptable since I do not have MATLAB in my computer.

#Made in visual studios 2019
#Compiling Instructions
#


#No pass by reference for string so print reverse
def printRevString(string):
    x = len(string)-1
    while(x>=0):
        print(string[x], end = '')
        x=x-1
    print(end='\n')

def createTable(string1, string2):
    #Creating Table
    lenstr1 = len(string1)
    lenstr2 = len(string2)
    #Dynamically creating 2d Array
    tDA = [[0 for x in range(lenstr1 + 1)] for y in range(lenstr2 + 1)]

    #Filling Table
    x = 0
    y = 0
    #First row
    while(x<lenstr1 + 1):
        tDA[y][x] = x
        x = x+1
    x = 0
    #Filling First Column
    while(y<lenstr2 + 1):
        tDA[y][x] = y
        y = y+1

    #Filling Rest of Table
    y = 1
    x = 1
    while (y<lenstr2 + 1):
        while(x<lenstr1 + 1):
            #If same letter Check diagonal matching
            if(string1[x-1] == string2[y-1]):
                tDA[y][x] = tDA[y-1][x-1]
            elif((tDA[y-1][x-1] < tDA[y][x-1]) and (tDA[y-1][x-1] < tDA[y-1][x])):
                tDA[y][x] = tDA[y-1][x-1] + 1
            elif(tDA[y][x-1] < tDA[y-1][x]):
                tDA[y][x] = tDA[y][x-1] + 1
            else:
                tDA[y][x] = tDA[y-1][x] + 1
            x = x + 1
        x = 1
        y = y + 1

    return tDA

def traceTable(table, stringx, stringy):
    sizeY = len(table)
    sizeX = len(table[0])
    largest = 0
    moves = 0
    curVal = 0
    aligX = ""
    aligY = ""
    alignVal = 0
    nextVal = 0

    if sizeY > sizeX:
        largest = sizeY-1
    else:
        largest = sizeX-1

    #Start Point to back track
    x = sizeX-1
    y = sizeY-1
    while(moves < largest):
        #Check lowest number
        curVal = table[y][x]
        a = table[y-1][x]
        b = table[y-1][x-1]
        c = table[y][x-1]

        if(a<b and a<c):
            aligX = aligX + "_"
            aligY = aligY + stringy[y-1]
            y = y-1
            a = nextVal
        elif(b<a and b<c):
            aligX = aligX + stringx[x-1]
            aligY = aligY + stringy[y-1]
            y = y-1
            x = x-1
            b = nextVal
        elif(c<a and c<b):
            aligX = aligX + stringx[x-1]
            aligY = aligY + "_"
            x = x-1
            c = nextVal
        else:
            aligX = aligX + stringx[x-1]
            aligY = aligY + stringy[y-1]
            b = nextVal
            x = x-1
            y = y-1

        moves = moves + 1
        if curVal != nextVal:
            alignVal = alignVal + curVal

    printRevString(aligX)
    printRevString(aligY)
    print("Alignment Value: ", alignVal)
    #print(aligX)
    #print(aligY)


def printTable(table):
    for i in table:
        for j in i:
            print(j, end = " ")
        print()


string1 = ""
string2 = ""

#Requesting two words
print(" Enter the first word")
string1 = input(string1)
print(" Enter the second word")
string2 = input(string2)
fullTable = createTable(string1, string2)

printTable(fullTable)
traceTable(fullTable, string1, string2)