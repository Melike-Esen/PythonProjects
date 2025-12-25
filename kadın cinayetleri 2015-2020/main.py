#VERİ YÜKLME TANIMLAMA
import data as data
import numpy as np #Liner Cebir
import pandas as pd # veri işleme, CSV dosyası G/Ç (ör. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import missingno as msno
import plotly.express as px



# Giriş verileri dosyaları salt okunur "../input/" dizininde bulunur
# Örneğin, bunu çalıştırmak (çalıştır'a tıklayarak veya Shift+Enter tuşlarına basarak) giriş dizini altındaki tüm dosyaları listeleyecektir.
from plotly.offline import iplot

veri = pd.read_csv('veriler.csv')
print(veri)
data = veri.replace({"^\s*|\s*$":""}, regex=True) #verilerimizdeki boslukları yok edebilmek için
year = data['yil'] = data['yil'].astype('int') #yearımızın degeri float olarak görünüyor o yüzden int e çevirdik
data['sehir'] = data['sehir'].astype('str')
boy = veri[['yil']] #sadece yıl bilgisini yazdır

#VERİTANIMLAMA
data.info()#veri başlıklarını listeler
data.tail()#veri büyüklüğünü/ içeriğini belirtir

#SAYISAL DEĞER BELİRLEME
yillaragoreolum = data.yil.value_counts().head(13).sort_index() # hangi yılda kaç kadın öldürüldüğü görülmektedir. 2015 yılında 294 kadın öldürülmüştür.
print(yillaragoreolum)

kimtarafindan = data.katil1.value_counts().head(15) #2015-2020 yılları arasında maktüllerin kim tarafından öldürüldüğü görülmektedir.
print(kimtarafindan)

kdurum=data.katildurumu.value_counts().head(7) #kod verilerde katillerin durumu gösterir.
print(kdurum)

#SORGU VE VERİ GÖRSELLEŞTİRME
data[((data.katil1 == 'Kocasi') | (data.katil2 == 'Kocasi')) &
    ((data.oldurmeyolu1 == 'Atesli Silah') | (data.oldurmeyolu2 == 'Atesli Silah')|(data.oldurmeyolu3 == 'Atesli Silah'))
] #yazılan sorguda kocası tarafından 2015-2020 tarihleri arasında ateşli silahla öldürülenler listelenmiştir.

#Ocak 2015 ve Ağustos 2020 Tarihleri Arasında Ölen Kadınlar Histogram Grafiği
yillaragoreolenkadinlar =data.yil.plot(kind = 'hist' , bins = 30 , figsize = (10,6) , range = (2015 , 2020) , label = 'Yil' )
yillaragoreolenkadinlar.set_title("Ocak 2015 ve Ağustos 2020 Tarihleri Arasında Öldürülen Kadınlar" , fontsize = 12)
yillaragoreolenkadinlar.set_xlabel("Yıl", fontsize = 12)
yillaragoreolenkadinlar.set_ylabel("Ölen Kadınlar", fontsize = 12)
plt.show()
#çıktı alındı

#Öldürülme Şekli Pie Chart Grafiği
degerler = data.oldurmeyolu1.value_counts().head(7)
nasiloldurulduler = degerler.plot(kind='pie'  , figsize = (9, 8) , startangle = 60 , shadow = False , autopct = "%1.1f%%")
nasiloldurulduler.set_title("Öldürülme Şekli" , fontsize = 15)
nasiloldurulduler.set_ylabel("" , fontsize = 15)
plt.show()
#çıktı geliyo

#Koruma Kararı Pie Chart Grafiği
var = data[data.korumaemri == 'Var']
yok = data[data.korumaemri == 'Yok']
tespitedilemeyen = data[data.korumaemri == 'Tespit Edilemeyen']
fig = go.Figure()
fig.add_trace(go.Histogram(
    x=var.yil,
    name='Var',
    xbins=dict(
        start=2008,
        end=2021,
        size=0.5
    ),
    marker_color='#EB89B5',
    opacity=0.75
))
fig.add_trace(go.Histogram(
    x=yok.yil,
    name='Yok',
    xbins=dict(
        start=2008,
        end=2021,
        size=0.5
    ),
    marker_color='#777CE8',
    opacity=0.75
))

fig.add_trace(go.Histogram(
    x=tespitedilemeyen.yil,
    name='Tespit Edilemeyen',
    xbins=dict(
        start=2008,
        end=2021,
        size=0.5
    ),
    marker_color='#74D6B4',
    opacity=0.75
))


fig.update_layout(
    title_text='Yıllara Göre Koruma Kararı Durumları',
    xaxis_title_text='Yıl',
    yaxis_title_text='Sayı',
)

fig.show()
#çıktı alındo

#Katillerin Durumu Pie Chart Grafiği
degerler3 = data.katildurumu.value_counts().head(6)
katdurum = degerler3.plot(kind='pie'  , figsize = (9, 8) , startangle = 60 , shadow = False , autopct = "%1.1f%%")
katdurum.set_title("Katillerin Durumu" , fontsize = 15)
katdurum.set_ylabel("" , fontsize = 15)
plt.show()
#çıktı alındı

#illere göre katledilme
sehir1 = data[(data['sehir'] == 'Izmir') | (data['sehir'] == 'Istanbul') | (data['sehir'] == 'Ankara')
             | (data['sehir'] == 'Bursa') | (data['sehir'] == 'Antalya') | (data['sehir'] == 'Adana') | (data['sehir'] == 'Gaziantep') ]
fig=px.scatter(x = sehir1.yil,y = sehir1.sehir, color=sehir1.oldurmeyolu1)
fig.update_layout(xaxis_title="Sayı",
                  yaxis_title="Büyükşehirler",
                  title="Büyükşehirlerdeki kadınların öldürülme şekilleri")
fig.show()
#çıktı geliyor

#yasa göre koruma
resit = data[data.yas == 'Resit']
resitdegil = data[data.yas == 'Resit Degil']
tespitedilemeyen = data[data.yas == 'Tespit Edilemeyen']
fig = go.Figure()
fig.add_trace(go.Histogram(
    x=resit.korumaemri,
    name='Resit',
    marker_color='#EB89B5',
    opacity=0.75
))
fig.add_trace(go.Histogram(
    x=resitdegil.korumaemri,
    name='Resit Degil',
    marker_color='#777CE8',
    opacity=0.75
))

fig.add_trace(go.Histogram(
    x=tespitedilemeyen.korumaemri,
    name='Tespit Edilemeyen',
    marker_color='#74D6B4',
    opacity=0.75
))


fig.update_layout(
    title_text='Yaşa Göre Koruma Kararı Durumları',
    xaxis_title_text='Koruma Kararı',
    yaxis_title_text='Sayı',
)

fig.show()



