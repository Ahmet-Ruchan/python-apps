import seaborn as sns
import pandas as pd

###todo VERİ GÖRSELLEŞTİRME
###todo VERİ SETİNİN YAPISININ İNCELENMESİ
###todo VERİ SETİNİN BETİMLENMESİ
###todo EKSİK DEĞERLERİN İNCELENMESİ
###todo KATEGORİK DEĞİŞKEN ÖZETLERİ
###todo SÜREKLİ DEĞİŞKEN ÖZETLERİ
###todo SÜTUN GRAFİK (BAR PLOT)

print()

###todo VERİ SETİNİN YAPISININ İNCELENMESİ
# planets = sns.load_dataset('planets')
# print(planets.head())
# #veri setinin hikayesi nedir

# df = planets.copy()
# #print(df.head())
# print(df.info())
# print(df.dtypes)

# df.method = pd.Categorical(df.method) #method isimli değişkeni category yaptık, yapmadan önce object idi.
# print(df.dtypes)

###todo VERİ SETİNİN BETİMLENMESİ
# planets = sns.load_dataset("planets")
# df = planets.copy()
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.describe().T)

###todo EKSİK DEĞERLERİN İNCELENMESİ
# planets = sns.load_dataset("planets")
# df = planets.copy()
# print(df.head())

# #* Eksik Gözlem Var mı?
# print(df.isnull().values.any()) # True çıktısı verdi yani veri setinde eksik var demektir
# #* Hangi değişkende kaçar tane eksik var?
# print(df.isnull().sum())

# #! orbital_period değişkeninde 43 adet eksik var bunu kısa vadede, geçici olarak çözebiliriz
# df["orbital_period"].fillna(0, inplace = True) #True olan yerleri yani eksik olan yerleri 0 yap, eksiği gider. Ama bu geçici kısa bir çözümdür.
# print(df.isnull().sum()) #şimdi 43 değerinin yerini 0 değeri aldı

# #eksik değerler yerine 0 koymak değil, ortalama değerlerini koymak istersek
# df.fillna(df.mean(), inplace = True)
# print(df.isnull().sum()) #şimdi hepsinde 0 yazıyor çünkü veri setindeki eksik olan bütün kısımlar ortalama değerler ile yer değiştirildi.

###todo KATEGORİK DEĞİŞKEN ÖZETLERİ
# planets = sns.load_dataset("planets")
# df = planets.copy()
# print(df.head())

# #*Sadece kategorik değişkenler ve özetleri
# kat_df = df.select_dtypes(include = ["object"]) #"object" yazarak veri seti içerisindeki kategorik değişkenleri seç demiş olduk
# print(kat_df.head())

# #*Kategorik değişkenlerin sınıflarına ve sınıf sayılarına erişmek
# print(kat_df.method.unique())
# print(kat_df["method"].value_counts().count()) #kaç tane olduğunu göstermek için

# #*Kategorik değişkenlerin sınıflarının frekanslarına erişmek
# print(kat_df["method"].value_counts())

# print(kat_df["method"].value_counts().plot.barh()) #barh() demek sütun grafiği ver demek #Google Colab üzerinden görselleştirebilirsin

###todo SÜREKLİ DEĞİŞKEN ÖZETLERİ
# planets = sns.load_dataset("planets")
# df = planets.copy()

# df_num = df.select_dtypes(include = ["float64", "int64"])
# print(df_num.head())

###todo SÜTUN GRAFİK (BAR PLOT)
# diamonds = sns.load_dataset('diamonds')
# df = diamonds.copy()
# #print(df.head())

# #print(df.info())
# #print(df.describe().T)

# # print(df.head())
# # print(df["cut"].value_counts())
# # print('\n')
# # print(df["color"].value_counts())

# #*Ordinal tanımlama
# from pandas.api.types import is_categorical_dtype
# # print(df.cut.head())
# df.cut = df.cut.astype(pd.CategoricalDtype(ordered = True))
# # print(df.cut)
# # print(df.cut.head(1))

# cut_kategoriler = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
# df.cut = df.cut.astype(pd.CategoricalDtype(categories = cut_kategoriler, ordered = True))
# print(df.cut.head(1))

###todo SÜTUN GRAFİK OLUŞTURMAK (BAR PLOT)
# diamonds = sns.load_dataset('diamonds')
# df = diamonds.copy()

# print(df["cut"].value_counts().plot.barh().set_title("Cut Değişkeninin Sınıf Frekansları")) #set_title kısmı grafiğin üzerine başlık koymak için #sütun grafik verecek Colab üzerinden görebilirsin

# print(sns.barplot(x = "cut", y = df.cut.index, data = df)) #seaborn ile görselleştirme yaptık benzer şekilde ama renkli oldu bu sefer

###todo SÜTUN GRAFİK ÇAPRAZLAMALAR
from pandas.api.types import is_categorical_dtype

diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()

cut_kategoriler = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
df.cut = df.cut.astype(pd.CategoricalDtype(categories = cut_kategoriler, ordered = True))
print(df.head())

sns.catplot(x = "cut", y = "price", data = df) #cut ve price değişkenlerinin çaprazlanarak bir sütun grafik elde edildi

sns.barplot(x = "cut", y = "price", hue = "color", data = df)




























print()