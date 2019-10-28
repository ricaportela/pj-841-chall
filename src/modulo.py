count = {"UPPER": 0, "LOWER": 0}

def func(pedras="", joia=""):
    arguments = locals()

    for k, v in arguments.items():
        print(k,v)
        count["UPPER"] += sum(map(str.isupper, v))
        count["LOWER"] += sum(map(str.islower, v))
 

    print("Quantidade de letras maiusculas {}".format(count["UPPER"]))
    print("Quantidade de letras minusculas {}".format(count["LOWER"]))


print(func("aaaA", "bbbA"))
