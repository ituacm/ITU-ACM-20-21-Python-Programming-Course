#Ödevi için Ahmet Akın'a teşekkür ederiz ~ACM Python Kursu Ekibi

while True:
    try:
        basla = int(input())
        hedef = int(input())
        artis = int(input())

        if basla == 0 and hedef == 0 and artis == 0:
            break

        for oruntu in range(basla, hedef, artis):
            print(oruntu)

    except(ValueError):
        print("lütfen yalnızca sayı giriniz!")

   
