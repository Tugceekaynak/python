#0-40 dc
#41-60 cb
#61-80 bb
#80-100 aa

kul_vize = int(input("vize Notunuzu girin:   "))
kul_final = int(input("final Notunuzu girin:   "))

if type(kul_vize) == "int" and type(kul_final) == "int":
   if 0 < kul_vize < 100 and 0 < kul_final < 100:
        kul_not= ((kul_vize*40/100)+(kul_final*60/100))
        if 0 < kul_not <= 40:
            print("notunuz dc")
        elif 40 < kul_not <=60:
            print("notunuz cb")
        elif 60 < kul_not <=80:
            print("notunuz bb")
        elif 80 < kul_not <=100:
            print("notunuz aa")
        else:
            print("tanımsız")
else:
     print("lütfen sayı girin")

def ortalama_hesapla (gecici_vize, gecici_final):
    print(gecici_vize, type(gecici_vize))
    print(gecici_final, type(gecici_final))
    if type(gecici_vize_vize) == "int" and type(gecici_final_final) == "int":
        if 0 < gecici_vize < 100 and 0 < gecici_final < 100:
            kul_not = ((gecici_vize * 40 / 100) + (gecici_final * 60 / 100))
            if 0 < kul_not <= 40:
                print("notunuz dc")
            elif 40 < kul_not <= 60:
                print("notunuz cb")
            elif 60 < kul_not <= 80:
                print("notunuz bb")
            elif 80 < kul_not <= 100:
                print("notunuz aa")
            else:
                print("tanımsız")
    else:
        print("lütfen sayı girin")

ogr_1_vize = int (input("ilk ogrencinin vizesini giriniz"))
ogr_1_final = int (input("ilk ogrencinin finalini giriniz"))