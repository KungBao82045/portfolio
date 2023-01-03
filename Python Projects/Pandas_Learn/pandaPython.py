from distutils.command.clean import clean
from os import system
system("clear")
import pandas as pd
    
def test1():
    # print(pd.__file__)

    dataSet = {
        "cars": ["BNW", "Volvo", "Ford"],
        "passages": [3, 7, 2]
    }

    myvar = pd.DataFrame(dataSet) # Returnerer liste av data. 5 liste fra topp og 5 liste fra bunn. 2d dimensjon data.
    # print(myvar)

    dataNum = [65, 334, 12]

    myvar1 = pd.Series(dataNum, index = ["z", "x", "y"]) # Med index, du kan endre fra 1, 2, 3 til z, x, y
    # print(myvar1)

    dataCSV = pd.read_csv("vgsales.csv") # Lese CSV
    # print(dataCSV.to_string()) # Returnerer full liste av data
    # print(dataCSV)

    dataJSON = pd.read_json("data.json") # Lese json
    print(dataJSON.to_string())


    # print(dataCSV.head(20)) # Starter fra top til bunn. Itererer 5 som default hvis tall ikke ble spesifisert
    # print(dataCSV.tail(5)) # Starter fra bunn til top. Itererer 5 som default hvis tall ikke ble spesifisert

    dataCSV1 = pd.read_csv("vgsales.csv")
    # print(dataCSV1.info())


# test1()

def clean_test():
    dataJSON = pd.read_json("data.json")
    dataJSON1 = dataJSON.dropna() # Fjerner tomt data
    # print(dataJSON1.to_string()) # Returnerer full DataFrame

    dataJSON2 = dataJSON.fillna(130, inplace = True)
    #print(dataJSON.to_string())


    # Mean = the average value (the sum of all values divided by number of values).
    # Median = the value in the middle, after you have sorted all values ascending.
    # Mode = the value that appears most frequently.

    df = pd.read_csv("data.csv")
    x = df["Calories"].mean()
    df["Calories"].fillna(x, inplace=True)
    print(df.to_string())

clean_test()

