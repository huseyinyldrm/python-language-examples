# enumerate() ile listeler numaralandırılır.

gun=['Pazartesi','Sali','Carsamba','Persembe','Cuma','Cumartesi','Pazar']

for i,deger  in enumerate(gun):
    print(str(i+1)+".gün "+ deger)