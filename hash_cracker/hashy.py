class CyberSecurities:

    def cyber_security1(self, Red, Cyan, Yellow, White, Green, Purple):
        import hashlib
        import time

        print(f"\n\n\nRunning, {Green}Cyber Security Training NO.1{White}!")
        print(f"Created By{Yellow} Jacky{White}")
        print(f'''\nv1.2 {Cyan}- You can now use other hashes like SHA1, SHA224 ect.
     - Program will no longer give you double warning when you choose to iterate
     - Program will now send an error if you type improperly{White}''')

        flag = 0
        hash_types = ("MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512")
        
        hash_enter = str(input(f"\n[*] Select Hash Type({Cyan}MD5{White}, {Red}SHA1{White}, {Yellow}SHA224{White}, SHA256, {Green}SHA384{White}, {Purple}SHA512{White}): ")).upper()
       
        if hash_enter not in hash_types:
            quit(f"[{Cyan}-{White}] Cannot start. Make sure to type the hash properly")

        pass_hash = input(f"\n{White}[{Cyan}*{White}] Enter Hash: ")

        if len(pass_hash) != 32 and hash_enter == "MD5":
            print(f"[{Cyan}-{White}]{Red} MD5 must contain 32 letters!{White}")
            quit(0)
        
        elif len(pass_hash) != 40 and hash_enter == "SHA1":
            print(f"[{Cyan}-{White}]{Red} SHA1 must contain 40 letters!{White}")
            quit(0)
        
        elif len(pass_hash) != 56 and hash_enter == "SHA224":
            print(f"[{Cyan}-{White}]{Red} SHA224 must contain 56 letters!{White}")
            quit(0)
        
        elif len(pass_hash) != 64 and hash_enter == "SHA256":
            print(f"[{Cyan}-{White}]{Red} SHA256 must contain 64 letters!{White}")
            quit(0)
        
        elif len(pass_hash) != 96 and hash_enter == "SHA384":
            print(f"[{Cyan}-{White}]{Red} SHA384 must contain 96 letters!{White}")
            quit(0)
        
        elif len(pass_hash) != 128 and hash_enter == "SHA512":
            print(f"[{Cyan}-{White}]{Red} SHA512 must contain 128 letters!{White}")
            quit(0)

        Wordlist = input(f"[{Cyan}*{White}] Enter File Name: ")

        try:
            pass_file = open(Wordlist, "r")

        except:

            quit(f"\n[{Cyan}-{White}]{Red} File Not Found:{White} %s" % Wordlist)

        choice = input(f'[{Cyan}*{White}] (Y/N)Would You Like To Iterate({Yellow}WARNING: Iteration Can Slower The Process{White}): ')

        if choice.lower() == "y" or choice.lower() == "yes":

            print("\nIterating! Please Wait While Jacky Is Searching For Matching Hash. Go Grab Some Coffee!"); flag = 1; time.sleep(3)

        elif choice.lower() == 'n' or choice.lower() == "no":

            print("\nInitiating. Please Wait While Jacky Is Searching For Matching Hash. Go Grab Some Coffee!")

        else:

            quit(f'{Red}ERROR: Couldn\'t Initiate The Code. Exiting...')

        start = time.perf_counter()
        for word in pass_file:
            enc_wrd = word.encode('utf-8')
            try:
                if hash_enter == "MD5":
                    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
                elif hash_enter == "SHA1":
                    digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
                elif hash_enter == "SHA224":
                    digest = hashlib.sha224(enc_wrd.strip()).hexdigest()
                elif hash_enter == "SHA256":
                    digest = hashlib.sha256(enc_wrd.strip()).hexdigest()
                elif hash_enter == "SHA384":
                    digest = hashlib.sha384(enc_wrd.strip()).hexdigest()
                elif hash_enter == "SHA512":
                    digest = hashlib.sha512(enc_wrd.strip()).hexdigest()
                else:
                    raise ValueError("ERROR: Couldn't Go To The Next Step. Exiting")
            except Exception as v_E:
                print(v_E)

            if flag == 1:
                print(pass_hash); print(digest); print(word)

            if digest == pass_hash:
                finish = time.perf_counter()
                print(f"\n------------------------------------------")
                print(f"\n    -- MATCHING HASH FOUND -- ")
                print(f"\n[{Cyan}*{White}] {hash_enter} hash used: " + pass_hash)
                print(f"[{Cyan}*{White}] Wordlist used: " + Wordlist)
                print(f"[{Cyan}*{White}] Elapsed TIme: {round(finish-start)} second(s)")
                print(f"\n[{Cyan}!!{White}]{Green} Original String: %s{White}" % word)
                print(f"{White}------------------------------------------")
                break

        else:
            finish = time.perf_counter()
            print("\n------------------------------------------")
            print(f"\n[{Cyan}*{White}] {hash_enter} hash used: {White}%s" % pass_hash)
            print(f"[{Cyan}*{White}] Elapsed TIme: {round(finish-start)} second(s)")
            print(f"[{Cyan}-{White}]{Red} No Hashes Found In {White}%s" % Wordlist)
            print(f"\n{White}------------------------------------------")


    def hash_converter(self, Red, Cyan, Yellow, White, Green, Purple):
        import hashlib
        import os
        import time

        hash_converter_file = "H_converter.txt"

        if os.path.exists(hash_converter_file):
            os.remove(hash_converter_file)
            time.sleep(0.5)

        print(f"""\nRunning, {Green}Hash Converter{White}!
Created By{Yellow} Jacky
v1.0{White}""")

        has_types = ("MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512")
        hash_type = str(input(f"\nSelect Hash Type({Cyan}MD5{White}, {Red}SHA1{White}, {Yellow}SHA224{White}, SHA256, {Green}SHA384{White}, {Purple}SHA512{White}): ")).upper()
        if hash_type not in has_types:
            print("\"{}\" Hash Type Not Found.\n".format(hash_type))
            quit()

        hash_converter = input("Enter Your String: ")
        

        with open(hash_converter_file, "x"):
            with open(hash_converter_file, "w") as f:
                f.write(hash_converter)
                try:
                    pass_file = open(hash_converter_file, "r")

                except FileNotFoundError as F_Error:
                    print(F_Error + ", Exiting")
                    exit()

                f.close()


        for word in pass_file:
            enc_wrd = word.encode('utf-8')
            if hash_type == "MD5":
                digest = hashlib.md5(enc_wrd.strip()).hexdigest()
            elif hash_type == "SHA1":
                digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
            elif hash_type == "SHA224":
                digest = hashlib.sha224(enc_wrd.strip()).hexdigest()
            elif hash_type == "SHA256":
                digest = hashlib.sha256(enc_wrd.strip()).hexdigest()
            elif hash_type == "SHA384":
                digest = hashlib.sha384(enc_wrd.strip()).hexdigest()
            elif hash_type == "SHA512":
                digest = hashlib.sha512(enc_wrd.strip()).hexdigest()
            else:
                raise ValueError("ERROR: Couldn't Go To The Next Step. Exiting")


            print("\n" + digest + "\n")
            


class Operative_Systems:

    def file_text_append(self):
        import os

        flag = False
        accept_decline = ("y", "yes")

        word_enter = input("Enter a word to append: ")
        file = input("Enter file text (example.txt): ")
        if not os.path.exists(file):
            print("File not found. You need to create one.")
            quit(0)


        iteration_ = input("Do you want to output text? (Y/N): ")

        if iteration_ in accept_decline:
            flag = True

        with open(file, "r") as f:
            for index, line in enumerate(f.readlines()):
                if flag == True:
                    print("Line" + str(index + 1) + ", " + str(line))

                if word_enter in line:
                    print("\n[-] " + word_enter + " Already Existed In Line", str(index + 1))
                    exit(0)

            else:
                with open(file, "a") as a_f:
                    a_f.write(f"\n{word_enter}")
                    print("\n[+] Appended: [" + str(word_enter) + "] At The End Of The Line.")
                    
                    a_f.close()
    def os_commands(self):
        import os
        print("You can type a command as usual as cmd. Type '?help' for info")
        while True:

            x = input("Enter command: ")
            if x == "?help":
                print("""- ?exit - to exit the program
- ?link - to open a link (opens best Python Courses!)""")
            elif x == "?exit":
                break
            elif x == "?link":
                lol = ['X', 'c', 'Q', '4', '9', 'w', 'd', 'W', 'g']
                enc = ("h" + "t" + "t" + "p" + "s" + ":" + "/" + "/" + "y" + "o" + \
"u" + "t" + "u" + "." + "b" + "e" + "/" + lol[6] + lol[2] + lol[5] + lol[3] + \
lol[5] + lol[4] + lol[-2] + lol[-1] + lol[0] + lol[1] + lol[2])
                os.system("start %s" % enc)
            else:
                os.system(x)
            
   

Cyber_Initiate = CyberSecurities()
operative_systems = Operative_Systems()

def mode_1(Green, White, Purple):
    x = int(input(f"Select mode({Green}1 - Hash_Cracker, 2 - Hash_Converter {Purple}3 - Operative_Systems, 4 - os_commands){White}: "))
    if x == 1:
        Cyber_Initiate.cyber_security1(Red='\033[91m', Cyan='\033[96m', Yellow='\033[93m', White='\033[0m', Green='\033[92m', Purple = '\033[95m')
    elif x == 2:
         Cyber_Initiate.hash_converter(Red='\033[91m', Cyan='\033[96m', Yellow='\033[93m', White='\033[0m', Green='\033[92m', Purple = '\033[95m')
    elif x == 3:
        operative_systems.file_text_append()
    elif x == 4:
        operative_systems.os_commands()
    else:
        quit("Invalid number. Exiting...")


if __name__ == "__main__":
    mode_1(Green='\033[92m', White='\033[0m', Purple = '\033[95m')
