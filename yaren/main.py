n = input('Sayıyı Girin : ')
tekToplam=0
tekcarp=1
ciftkare=0
for i in range(1,int(n),1):
      if(i%2==1):
            tekToplam+=i
      elif (i !=1):
            tekcarp *=i
      elif (i%2==0):
            ciftkare+=i*i

print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Tek Sayıların Çarpımı : {0}".format(tekcarp))
print("Çift Sayıların Karelerinin Toplamı : {0}".format(ciftkare))