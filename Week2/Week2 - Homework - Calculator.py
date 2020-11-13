# Ödevi için Şafak Koç'a teşekkür ederiz ~ACM Python Kursu Ekibi

import math

print("*"*70, "\n              Hesap Makinesi Programına Hoş Geldiniz.\n","*"*68,
      "\n          -----Yapabileceğiniz işlemlerin numaraları-----\n1: iki sayının toplamı      |  6: bir sayının karekökü"
      "\n2: iki sayının farkı        |  7: bir sayının e tabanında logaritması"
      "\n3: iki sayının çarpımı      |  8: bir sayının 10 tabanında logaritması"
      "\n4: iki sayının bölümü       |  9: bir doğal sayının faktöriyel çarpımı"
      "\n5: bir sayının üslü kuvveti |  10: ikinci dereceden bir denklemin kökleri\n","*"*70)

islem=int(input("Yapmak istediğiniz işlemi giriniz:"))

if islem==1:
    add1=int(input("toplanacak sayıların ilkini giriniz:"))
    add2=int(input("toplanacak sayıların ikincisini giriniz:"))
    print("bu iki sayının toplamı: ", add1+add2)

elif islem==2:
    sub1=int(input("birbirinden çıkarmak istediğiniz sayıların ilkini giriniz:"))
    sub2=int(input("birbirinden çıkarmak istediğiniz sayıların ikincisini giriniz:"))
    print("bu iki sayının farkı:", sub1-sub2)

elif islem==3:
    mult1=int(input("çarpanların ilkini giriniz: "))
    mult2=int(input("çarpanların ikincisini giriniz: "))
    print("bu iki sayının çarpımı: ", mult1*mult2)

elif islem==4:
    div1=int(input("bölme isleminin bölünenini giriniz: "))
    div2=int(input("bölme isleminin bölenini giriniz: "))
    print("bölümün sonucu: ", div1/div2)

elif islem==5:
    ust1=int(input("üslü kuvvetini almak istediğiniz sayıyı giriniz:"))
    ust2=int(input("üssü giriniz:"))
    print("işlemin sonucu: ",pow(ust1,ust2))

elif islem==6:
    kare=int(input("karekökünü almak istediğiniz \ndoğal sayıyı giriniz: "))
    if kare<0:
        print("bu bir doğal sayı değil.")
    else:
        print("bu sayının karekökü: ",math.sqrt(kare))

elif islem==7:
    loge=int(input("e tabanında logaritmasını öğrenmek istediğiniz sayıyı giriniz: "))
    if loge<0:
        print("girdiğiniz sayı bir doğal sayı olmalıdır.")
    else:
        print("bu işlemin sonucu: ", math.log(loge))

elif islem==8:
    logten=int(input("10 tabanında logaritmasını öğrenmek istediğiniz sayıyı giriniz: "))
    if logten<0:
        print("girdiğiniz sayı bir doğal sayı olmalıdır.")
    else:
        print("bu işlemin sonucu: ", math.log10(logten))

elif islem==9:
    fakt=int(input("faktöriyel çarpımını öğrenmek istediğiniz sayıyı giriniz:"))
    if fakt<0:
        print("girdiğiniz sayı bir doğal sayı olmalıdır.")
    else:
        print("girdiğiniz sayının faktöriyeli: ", math.factorial(fakt))

elif islem==10:
    print("ax^2 + bx +c seklindeki bir denklemin\nköklerini öğrenmek için a,b,c sayılarını giriniz.")
    eqa=int(input("a:"))
    eqb=int(input("b:"))
    eqc=int(input("c:"))
    delta=(eqb**2)-(4*eqa*eqc)

    if delta<0:
        print("bu denklemin reel kökü yoktur.")
        
    else:
        root1=((-eqb)+(math.sqrt(delta)))/(2*eqa)
        root2=((-eqb)-(math.sqrt(delta)))/(2*eqa)
        denklem="("+str(eqa)+"x^2)+"+"("+str(eqb)+"x)"+"+"+"("+str(eqc)+")"
        if root1==root2:
            print(denklem, "denkleminin tek kökü {}'dir.".format(root1))
        else:
            print(denklem, "denkleminin kökleri {} ve {}'dir.".format(root1, root2))
