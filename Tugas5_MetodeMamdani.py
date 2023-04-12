"""
Keterangan:
VARIABEL PERMINTAAN
pmtb=permintaan terbesar
pmtt=permintaan terkecil

VARIABEL PERSEDIAAN
psdb=persediaan terbanyak
psdk=persediaan terkecil

VARIABEL PRODUKSI BARANG
prod_brgmax=produksi barang max
prod_brgmin=produksi barang min
"""
pmtb=5000
pmtt=1000
psdb=600
psdk=100
prod_brgmax=7000
prod_brgmin=2000
pmt=int(input("Masukan jumlah permintaan: "))
psd=int(input("Masukan jumlah persediaan: "))


if pmt<=pmtt:
    pmt_turun=1
    print("Derajat Keanggotaan pmt_turun: ",pmt_turun)
elif pmt>=pmtt and pmt<=pmtb:
    pmt_turun=(pmtb-pmt)/(pmtb-pmtt)
    print("Derajat keanggotaan pmt_turun= ",pmt_turun)
elif pmt>=pmtb:
    pmt_turun = 0
    print("Derajat keanggotaan pmt_turun=", pmt_turun)

if pmt<=pmtt:
    pmt_naik=0
    print("Derajat Keanggotaan pmt_naik: ",pmt_naik)
elif pmt>=pmtt and pmt<=pmtb:
    pmt_naik=(pmt-pmtt)/(pmtb-pmtt)
    print("Derajat keanggotaan pmt_naik= ",pmt_naik)
elif pmt>=pmtb:
    pmt_naik = 1
    print("Derajat keanggotaan pmt_naik=", pmt_naik)

if psd<=psdk:
    psd_sedikit=1
    print("Derajat Keanggotaan psd_sedikit: ",psd_sedikit)
elif psd>=psdk and psd<=psdb:
    psd_sedikit=(psdb-psd)/(psdb-psdk)
    print("Derajat keanggotaan psd_sedikit= ",psd_sedikit)
elif psd>=psdb:
    psd_sedikit=0
    print("Derajat Keanggotaan psd_sedikit: ",psd_sedikit)

if psd<=psdk:
    psd_banyak=0
    print("Derajat Keanggotaan psd_banyak: ",psd_banyak)
elif psd>=psdk and psd<=psdb:
    psd_banyak=(psd-psdk)/(psdb-psdk)
    print("Derajat keanggotaan psd_banyak= ",psd_banyak)
elif psd>=psdb:
    psd_banyak=1
    print("Derajat Keanggotaan psd_banyak: ",psd_banyak)


#Rule 1 : IF Permintaan TURUN And Persediaan BANYAK THEN Produksi Barang BERKURANG")
def Rule1():
    prod_brg_berkurang1=min(pmt_turun,psd_banyak)
    return prod_brg_berkurang1

#Rule 2 : IF Permintaan TURUN And Persediaan SEDIKIT THEN Produksi Barang BERKURANG")
def Rule2():
    prod_brg_berkurang2=min(pmt_turun,psd_sedikit)
    return prod_brg_berkurang2
#Rule 3 : IF Permintaan NAIK And Persediaan BANYAK THEN Produksi Barang BERTAMBAH")
def Rule3():
    prod_brg_bertambah1=min(pmt_naik,psd_banyak)
    return prod_brg_bertambah1
#Rule 4 : IF Permintaan NAIK And Persediaan SEDIKIT THEN Produksi Barang BERTAMBAH")
def Rule4():
    prod_brg_bertambah2=min(pmt_naik,psd_sedikit)
    return prod_brg_bertambah2

prod_brg_berkurang=max(Rule1(),Rule2())
prod_brg_bertambah=max(Rule3(),Rule4())

if (prod_brg_berkurang>prod_brg_bertambah):
    a1=prod_brgmax-((prod_brgmax-prod_brgmin)*prod_brg_berkurang)
    a2=prod_brgmax-((prod_brgmax-prod_brgmin)*prod_brg_bertambah)
    print("Adapun nilai a1 yang didapatkan adalah ",a1,"dan nilai a2 = ",a2)
    print("***************************************")
    print("Fungsi keanggotaan yang baru")
    print(prod_brg_berkurang, ";\tz <= ", a1)
    print("(",prod_brgmax,"-z",") /", prod_brgmax-prod_brgmin, ";\t", a1, "<=", "z <= ", a2)
    print(prod_brg_bertambah, ";\tz >= ", a2)
    def m(z):
        if(z<=a1):
            mz=prod_brg_berkurang
        elif(z>a1 and z<a2):
            mz=(prod_brgmax-z)/(prod_brgmax - prod_brgmin)
        else:
            mz=prod_brg_bertambah
        return mz

elif (prod_brg_berkurang==prod_brg_bertambah):
    a1=prod_brgmax-((prod_brgmax-prod_brgmin)*prod_brg_berkurang)
    print("Adapun nilai a1 yang didapatkan adalah ",a1)
    print("***************************************")
    print("Fungsi keanggotaan yang baru")
    print(pmt_turun, ";\tz <= ", prod_brgmax)
    def m(z):
        mz=prod_brg_berkurang
        return mz

else:
    a1=((prod_brgmax-prod_brgmin)*prod_brg_berkurang)+prod_brgmin
    a2 = ((prod_brgmax - prod_brgmin) * prod_brg_bertambah) + prod_brgmin
    print("Adapun nilai a1 yang didapatkan adalah ",a1,"dan nilai a2 = ",a2)
    print("***************************************")
    print("Fungsi keanggotaan yang baru")
    print(prod_brg_berkurang, ";\tz <= ", a1)
    print("(z - ", prod_brgmin, ") / ", prod_brgmax-prod_brgmin, ";\t", a1, "<=", "z <= ", a2)
    print(prod_brg_bertambah, ";\tz >= ", a2)
    def m(z):
        if(z<=a1):
            mz=prod_brg_berkurang
        elif(z>a1 and z<a2):
            mz=(z-prod_brgmin)/(prod_brgmax-prod_brgmin)
        else:
            mz=prod_brg_bertambah
        return mz




