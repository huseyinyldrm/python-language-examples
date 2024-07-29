'''sözlük oluşturulurken {} kullanilir.Listeden farkli olarak ikili olarak ilşkilendirilir.
   dict([]) ile de sözlük oluşturulabilir.
'''
mevsim={'kis':1,'ilkbahar':2,'yaz':3,'sonbahar':4} # ilk deger anahtar-key , 2. girilen değer - value
print(mevsim)
print(mevsim.keys())# sadece anahtarları yani keysleri yazdırır.
print(mevsim.values()) # sadece değerleri yazdırır.
print(mevsim['kis']) # 'kis' anahtarının değerini döndürür.
print(mevsim.get('su','yok')) # bir key değerini getirir. eğer o değer yoksa 'yok' mesajı döner.
print(mevsim.pop('yaz')) # 'yaz' anahtarını siler.
print(mevsim)

