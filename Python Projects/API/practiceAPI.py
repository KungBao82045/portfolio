import requests
import pandas as pd
import regex
import csv
import json



class manage_json():


    """ 
    Her henter __init__ informasjon bruk av API.
    Dette kjører automatisk, som du slipper å kalle funksjonen
    """

    def __init__(self, get_url):
        self.r = requests.get(get_url)



    """
    Bruk 'with open' for å lage ny fil.
    Funksjonen, 'w' (write) som skriver informasjon og encoder utf-8 som kan gjøre 'æøå' lesbart
    Deretter, skriver funksjonen bruk av 'text' attributt. 
    """

    def write_json_from_url(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.r.text)
            f.close()


    


    def read_json_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.json_normalize(data)
        print(df)





#    def read_json_type_from_file(self, filename):
#        with open(filename, "r", encoding="utf-8") as f:
#            df = json.load(f)
#            print(json.dumps(df, indent=4))






class manage_csv():





    def __init__(self, get_url):
        self.r = requests.get(get_url)






    def write_csv_from_url(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.r.text)
            f.close()





    def read_csv_from_file(self, filename):
        df = pd.read_csv(filename, delimiter=";")
        print(df)





if __name__ == "__main__":




    # API test
    # KPI:              https://data.ssb.no/api/v0/dataset/1092.csv?lang=no
    # KPI:              https://data.ssb.no/api/v0/dataset/1092.json?lang=no

    # Arbeidsledige:    https://data.ssb.no/api/v0/dataset/1052.csv?lang=no
    # Arbeudsledige:    https://data.ssb.no/api/v0/dataset/1052.json?lang=no






    url = input("Hello! Please enter your URL...\n> ")
    # choose_filetype = input("Great! Choose your filetype: (csv / json)\n> ").lower()
    filetype_detection = "".join(regex.findall(r"([csv]{3}|[json]{4})", url))


    if filetype_detection != "None":
        name_the_file = "newData." + filetype_detection

    

    manage_json = manage_json(url)
    manage_csv = manage_csv(url)



    if filetype_detection == "csv":
        manage_csv.write_csv_from_url(name_the_file)
        manage_csv.read_csv_from_file(name_the_file)


    elif filetype_detection == "json":
        manage_json.write_json_from_url(name_the_file)
        manage_json.read_json_from_file(name_the_file)


    else:
        print(f"""
        Something went wrong. Please check the errors below if its correct.\n
        Filename:           {name_the_file}
        filetype detection: {filetype_detection}
        URL:                {url}
        """)





