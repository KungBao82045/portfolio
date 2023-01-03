import os
import shutil # Brukes til å flytte filer

path = input("Which path do you want to organize: ")

files = os.listdir(path)

for file in files:
    name, type = os.path.splitext(file)
    type = type[1:]
    # if bool(type):
    #     print(name, "=", type)

    if os.path.exists(path + "/" + type): # Hvis mp4, png mappe som eksempel finnes, flytt mp4 filen til mp4 mappen
        shutil.move(path + "/" + file, path + "/" + type + "/" + file)
    else:
        os.makedirs(path + "/" + type) # Hvis ikke finnes, lag en mappe og flytt alle filer til spesifikk mappe
        shutil.move(path + "/" + file, path + "/" + type + "/" + file)
else:
    print("Done!")
    # choice = input("> ").lower()
    # if choice == "y" or "yes":
    #     try:
    #         for file in files:
    #             name, type = os.path.splitext(file)
    #             type = type[1:]
    #             os.system("" + path + "/" + type)
    #             print("Removed: " + path + "/" + type)
    #     except PermissionError as e:
    #         print(e)
    #         print("1. Navigate to System Preference > Security & Privacy > Full Disk Access ")
    #         print("2. Click the “+” sign button and navigate to Application > Utilities > Terminal")
    #         print("3. If Terminal now checked, check it")
    #         print("4. Done!")
    #     except Exception as ee:
    #         print(ee)