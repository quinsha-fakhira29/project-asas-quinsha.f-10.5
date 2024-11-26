import datetime as dt

print (f"{ 'SEBERAPAKAH KAMU HIDUP ?' :_^40}" )

#memasukan input data ke dalam variable tanggal, bulan tahun 
nama = str(input("masukan nama kamu :"))
tanggal = int(input("masukan tanggal lahir kamu:"))
bulan = int(input("masukan bulan lahir kamu :"))
tahun = int(input("masukan tahun lahir kamu :"))
tanggal_lahir = dt.date(tahun,bulan,tanggal)

print("________hasil________")
print(f"hallo {nama}")
print(f"anda lahir pada : {tanggal_lahir}")
hari_ini = dt.date.today()
#menghitung lama hidup rumus (today - years- month- day)
lama_hidup = hari_ini - tanggal_lahir
#menghitung tahun (lama_hidup // 365)
tahun_lahir = lama_hidup.days // 365
bulan_lahir = (lama_hidup.days % 365) // 30
#memanggil hasil dari masing masing variable
print("anda lahir pada hari/days :{tanggal_lahir:%A}")
print(f"anda telah hidup di bumi selama: {lama_hidup},{bulan_lahir}")
print(f"umur anda sekarang: {tahun_lahir}, tahun :)")