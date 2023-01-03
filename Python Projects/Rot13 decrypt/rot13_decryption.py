
# This is ROT-13 project

rot_input = input("Type inn ROT-13 to decrypt/encrypt: ")
rot_decrypt_list = {
    "a": "n",
    "b": "o",
    "c": "p",
    "d": "q",
    "e": "r",
    "f": "s",
    "g": "t",
    "h": "u",
    "i": "v",
    "j": "w",
    "k": "x",
    "l": "y",
    "m": "z",
    "n": "a",
    "o": "b",
    "p": "c",
    "q": "d",
    "r": "e",
    "s": "f",
    "t": "g",
    "u": "h",
    "v": "i",
    "w": "j",
    "x": "k",
    "y": "l",
    "z": "m"
}

for x in rot_input:
    if x in rot_decrypt_list.keys():
        print(rot_decrypt_list[x], end="")
    elif x.isupper():
        rot_decrypt_list.update({k.upper(): v.upper() for k, v in rot_decrypt_list.items()})
        print(rot_decrypt_list[x], end="")
    else:
        print(x, end="")
