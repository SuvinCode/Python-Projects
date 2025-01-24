# <= 500 : 2%
# <= 600 : 3%
# <= 700 : 4%
# <= 800 : 5%
# > 800 : 6%

# Data
namaRakanLst = []
komisenRakanLst = []
jumlahDuitRakan = []

# Input

# Fungsi Komisen

def komisen(jumlahJualan):
    if jumlahJualan <= 500:
        jumlahKomisen = (jumlahJualan * 2 / 100)
        return jumlahKomisen
    elif jumlahJualan <= 600:
        jumlahKomisen = (jumlahJualan * 3 / 100)
        return jumlahKomisen
    elif jumlahJualan <= 700:
        jumlahKomisen = (jumlahJualan * 4 / 100)
        return jumlahKomisen
    elif jumlahJualan <= 800:
        jumlahKomisen = (jumlahJualan * 5 / 100)
        return jumlahKomisen
    else:
        jumlahKomisen = (jumlahJualan * 6 / 100)
        return jumlahKomisen



jumlahNama = int(input("\nMasukkan bilangan rakan : "))

while jumlahNama > 0:
    print()
    namaRakan = input("Masukkan nama anda : ")
    jualanRakan = int(input("Masukkan jumlah jualan anda : "))

    namaRakanLst.append(namaRakan)

    jumlahSeluruh = komisen(jualanRakan)
    komisenRakanLst.append(jumlahSeluruh)

    jumlahSeluruh = str(jumlahSeluruh)
    jumlahSeluruh = "RM" + jumlahSeluruh
    jumlahDuitRakan.append(jumlahSeluruh)

    jumlahNama -= 1

# Simpanan untuk murid dan jumlahnya
simpanan = dict(zip(namaRakanLst, jumlahDuitRakan))

# Mengira purata
purata = sum(komisenRakanLst) / len(namaRakanLst)

# Output
print("\nNama murid dengan jumlahnya :", simpanan)
print("\nPurata : RM", purata)
