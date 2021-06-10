import pandas as pd

def writeToCsv():
    df.to_csv("deneme.csv", index=False)
# updating the column value/data
def update(index, title):
    if int(title) == 1:
        df.loc[int(index), "audienceRating"] = input("audienceRating : ")
    elif int(title) == 2:
        df.loc[int(index), "Genre"] = input("Genre : ")
    elif int(title) == 3:
        df.loc[int(index), "criticRating"] = input("criticRating : ")
    elif int(title) == 4:
        df.loc[int(index), "timeMin"] = input("timeMin : ")
    elif int(title) == 5:
        df.loc[int(index), "grossMillions"] = input("grossMillions : ")
    elif int(title) == 6:
        df.loc[int(index), "Movie"] = input("Movie : ")
    elif int(title) == 7:
        df.loc[int(index), "Vote"] = input("Vote : ")
    elif int(title) == 8:
        df.loc[int(index), "Year"] = input("Year : ")
    else:
        print("Wrong choice, try again.")
    
# write a new row
def addNewRow():
    rowCounter = len(df)
    row = int(rowCounter)
    
    df.loc[row , ["audienceRating"]] = input("audienceRating : ")
    df.loc[row , ["Genre"]] = input("Genre : ")
    df.loc[row , ["criticRating"]] = input("criticRating : ")
    df.loc[row , ["timeMin"]] = input("timeMin : ")
    df.loc[row , ["grossMillions"]] = input("qrossMillions : ")
    df.loc[row , ["Movie"]] = input("Movie : ")
    df.loc[row , ["Vote"]]  = input("Vote : ")
    df.loc[row , ["Year"]] = input("Year : ")
    
#delete a row
def deleteRow(column):
    df.drop(int(column), axis = 0, inplace=True)

df = pd.read_csv ('deneme.csv', encoding='utf-8')
rowCounter = len(df)

questionAgain = "null"

while True:
    if not questionAgain == "y":
        goal = input(
              "What do you want to do?\n"
              "1 - Just show the file\n"
              "2 - Update the csv file\n"
              "3 - Add new row\n"
              "4 - Delete a row\n"
              "5 - Exit\n"
              )
     
    if int(goal) == 1:
        print(df)
        print("Do you want to do something else?")
        
    elif int(goal) == 2:
        
        while True:    
            index = input("Which index you want to change?\n")
            
            if 0 < int(index) and int(index) < (int(rowCounter)):
                break
            else:
                print("Wrong index number, try again.")
        
        title = input("Which title you want to change?\n"
                      "1 - audienceRating\n"
                      "2 - Genre\n"
                      "3 - criticRating\n"
                      "4 - timeMin\n"
                      "5 - grossMillions\n"
                      "6 - Movie\n"
                      "7 - Vote\n"
                      "8 - Year\n")
        
        update(index, title)
        writeToCsv()
        
        questionAgain = input("Success, do you want to change more title?(y/n)\n\n")
        
        if questionAgain == "y" or "Y":
            goal = 2
            
    elif int(goal) == 3:
        
        addNewRow()
        writeToCsv()
        print("Success. Do you want to do something else?\n")
    
    elif int(goal) == 4:
        
        column = input("Which index you want to delete?\n")
        deleteRow(column)
        writeToCsv()
        print("Success. Do you want to do something else?\n")
    
    elif int(goal) == 5:
        writeToCsv()
        break
    
    else: 
        print("Wrong choice")
            