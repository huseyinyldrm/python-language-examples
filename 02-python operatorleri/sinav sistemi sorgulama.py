
# kosul ifadeleri: if,elif,else
#karsilastirma operatorleri: ==,!=,<,>,>=,<=
#matiksal operatorler: and, or,not

ort=0 #ilklendirme 
print("\nBasit Ortalama Hesaplama Uygulamasi\n")
not1=int(input("Vize notunuzu giriniz:"))
not2=int(input("Final notunuzu giriniz:"))

ort=(float)(not1*0.4 + not2*0.6)

if (ort<49.5):
    print("Bute kaldiniz.Ortalamaniz: ",ort)

elif ort>=49.5 and ort<60:
    print("Sartli gectiniz.Ortalamaniz: ",ort)

else:
    print("Tebrikler gectiniz.Ortalamaniz: ",ort)