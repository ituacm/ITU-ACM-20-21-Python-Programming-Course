import random

ben, pc = 0, 0

while True:
    seçim = input("Taş için 1 Kağıt için 2 Makas için 3 giriniz: ")
    pcSeçim = random.choice(["1", "2", "3"])
    print(pcSeçim)
    if seçim == pcSeçim:
        print("ben:", ben, "pc", pc)
        continue
    elif seçim == "1" and pcSeçim == "2":
        pc += 1
        print("ben:", ben, "pc", pc)
    elif seçim == "1" and pcSeçim == "3":
        ben += 1
        print("ben:", ben, "pc", pc)
    elif seçim == "2" and pcSeçim == "1":
        ben += 1
        print("ben:", ben, "pc", pc)
    elif seçim == "2" and pcSeçim == "3":
        pc += 1
        print("ben:", ben, "pc", pc)
    elif seçim == "3" and pcSeçim == "1":
        pc += 1
        print("ben:", ben, "pc", pc)
    elif seçim == "3" and pcSeçim == "2":
        pc += 1
        print("ben:", ben, "pc", pc)
    if seçim == "-1":
        print("ben:", ben, "pc", pc)
        break
