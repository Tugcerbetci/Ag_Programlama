import pandas as pd

# json formatına dönüştürme kodları
excel_data = pd.read_excel('dataset.xlsx')

json_data = excel_data.to_json('kucuk.json', orient='records')




# Belirtilen sütunlarda aynı değere sahip olan satırları filtrele
df = pd.read_excel('dataset.xlsx')
df_filtered = df.drop_duplicates(subset=['KAYNAK_PROTOKOL', 'HEDEF_PROTOKOL', 'SALDIRI_TIPI'])

# Sonucu JSON formatında 'data.json' adlı dosyaya yaz
df_filtered.to_json('dataset.json', orient='records')


# KAYNAK_PROTOKOL sütununun unique değerlerini alın
veri_seti = pd.read_excel("dataset.xlsx")

unique_degerler = veri_seti["SALDIRI_TIPI"].unique()
print(unique_degerler)