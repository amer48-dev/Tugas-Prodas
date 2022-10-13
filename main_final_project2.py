# Membuat Final project
# Membuat Tampilan Aplikasi
from ast import Pass
from tabulate import tabulate
paket_yang_tersedia = [
    ["Kode Paket", "Rute Perjalanan", "Minimum Peserta", "Tarif"],
    ["1", "Karawang-Pantai Pakis Jaya", "6 Orang", "Rp.1000.000"],
    ["2", "Karawang - Curug Cigentis - Gunung Sanggabuana", "6 Orang", "Rp.500.000"],
    ["3", "Karawang - Candi Jiwa", "4 Orang", "Rp.600.000"],
    ["4", "Karawang - Pantai Samudra", "5 Orang", "Rp.850.000"]
 ]
print("\n PD.Travel menyediakan paket perjalanan sebagai berikut :\n")
print(tabulate(paket_yang_tersedia, headers="firstrow", tablefmt="fancy_grid"))

paket_tambahan = [
    ["Kode Tambahan", "Fasilitas", "Tarif"],
    ["A", "Penginapan", "Rp.600.000"],
    ["B", "Penjemputan", "Rp.300.000"],
    ["C", "Kuliner", "Rp.300.000"]
]

lanjutkan = input('\n Lanjut pemesanan (y/t) : ')
if lanjutkan == 'Y' or lanjutkan == 'y':
    print()
    pass
elif lanjutkan == 'T' or lanjutkan == 't':
    print('\n  Terima Kasih Telah Mengunjungi Kami \n' )
    quit()

# Variabel 
jumlah_tarif = 0
pajak = 11/100
tarif_paket = []
nama_paket = []
nama_peserta = []
kode_paket_tambahan = []
fasilitas = []
tarif_paket_tambahan = []
rincian_pemesanan = []


# Membuat input data user pembeli
nama_peserta = input(' Masukan Nama Peserta   : ')
kode_paket = int(input(' Masukan Kode Paket     : '))
if kode_paket == 1 :
    nama_paket.append('Karawang - Pantai Pakis Jaya')
    tarif_paket.append(1000000)
    jumlah_tarif += 1000000
    print('\n', nama_paket,tarif_paket)
elif kode_paket == 2:
    nama_paket.append('Karawang - Curug Cigentis - Gunung Sanggabuana')
    tarif_paket.append(500000)
    jumlah_tarif += 500000
    print('\n', nama_paket,tarif_paket)
elif kode_paket == 3:
    nama_paket.append('Karawang - Candi Jiwa')
    tarif_paket.append(600000)
    jumlah_tarif += 600000
    print('\n', nama_paket,tarif_paket)
elif kode_paket == 4:
    nama_paket.append('Karawang - Pantai Samudra')
    tarif_paket.append(850000)
    jumlah_tarif += 850000
    print('\n', nama_paket,tarif_paket)
else :
    print('Paket Tidak Tersedia')

#Harga total tanpa paket tambahan
ppn = int(pajak * jumlah_tarif)
jumlah_biaya = int(ppn + jumlah_tarif)
#Tampilan Pembayaran Tanpa Paket Tambahan
rincian_pemesanan_paket_perjalanan = [
    ["INPUT PEMBAYARAN TRAVEL"],
    ["Nama Peserta :", nama_peserta],
    ["Kode Paket :", kode_paket],
    ["Nama Paket :", nama_paket],
    ["Tarif Paket :", tarif_paket],
    ["Kode Tambahan :", '-'],
    ["Fasilitas:", '-'],
    ["Tarif Tambahan :", '-'],
    ["PPN 11% :", ppn ],
    ["Jumlah Biaya :", jumlah_tarif],
 ]
# Input Pemesanan Paket Tambahan
lanjutkan_paket_tambahan = input('\n Ingin memesan Paket Tambahan (y/t) : ')
if lanjutkan_paket_tambahan == 'Y' or lanjutkan_paket_tambahan == 'y':
    print("\n PD.Travel menyediakan paket tambahan lainnya yaitu :\n")
    print(tabulate(paket_tambahan, headers="firstrow", tablefmt="fancy_grid"))
elif lanjutkan_paket_tambahan == 'T' or lanjutkan_paket_tambahan == 't':
    print(tabulate(rincian_pemesanan_paket_perjalanan,headers="firstrow", tablefmt="fancy_grid"))
# Daftar pembayaran paket perjalanan
    laporan_pembayaran_paket_perjalanan = input('\n Mau Bayar Sekarang? (y/t) : ')
    while True:
     if laporan_pembayaran_paket_perjalanan == 'Y' or laporan_pembayaran_paket_perjalanan == 'y':
      bayar = int(input('\n Masukan Pembayaran Anda : '))
     if bayar == jumlah_biaya:
         print('\n Selamat Pembayaran Berhasil')
         status = 'Lunas'
         break
     elif bayar > jumlah_biaya:
         print('\n Selamat Pembayaran Berhasil')
         kembalian = bayar - jumlah_biaya
         print('\n Kembalian Anda : ', kembalian)
         status = 'Lunas'
         break
     elif bayar < jumlah_biaya:
         print('\n Pembayaran Gagal')
         kredit = bayar - jumlah_biaya
         print('\n Maaf Pembayaran Anda Kurang : ', kredit)
         status = 'Menunggu Pembayaran'
         break
     if laporan_pembayaran_paket_perjalanan == 'T' or laporan_pembayaran_paket_perjalanan == 't':
         print('Menunggu pembayaran')
         break
    print('\n Tampilan Laporan pembayaran Anda \n')
    daftar_pembayaran = [
    ['No', 'Nama Peserta', 'Nama Paket', 'Fasilitas Tambahan', 'Jumlah Tarif', 'Status'],
    ['1', nama_peserta, nama_paket, '-' , jumlah_biaya, status]
    ]
    print(tabulate(daftar_pembayaran, headers='firstrow', tablefmt='fancy_grid'))
    quit()


# Input Kode Paket Tambahan

kode_paket_tambahan = input('\n Masukan Kode Paket Tambahan : ')
if kode_paket_tambahan == 'A' or kode_paket_tambahan == 'a':
     fasilitas.append('Penginapan')
     tarif_paket_tambahan.append(600000)
     jumlah_tarif += 600000
     print('\n', fasilitas, tarif_paket_tambahan,'\n')
elif kode_paket_tambahan == 'B' or kode_paket_tambahan == 'b':
     fasilitas.append('Penjemputan')
     tarif_paket_tambahan.append(300000)
     jumlah_tarif += 300000
     print('\n', fasilitas, tarif_paket_tambahan,'\n')
elif kode_paket_tambahan == 'C' or kode_paket_tambahan == 'c':
     fasilitas.append('Kuliner')
     tarif_paket_tambahan.append(300000)
     jumlah_tarif += 300000  
     print('\n', fasilitas, tarif_paket_tambahan,'\n')
else:
     print('Paket Tidak Tersedia')
#Harga total
ppn = int(pajak * jumlah_tarif)
jumlah_biaya = int(ppn + jumlah_tarif)
# Tampilan Data Pembeli
rincian_pemesanan = [
    ["INPUT PEMBAYARAN TRAVEL"],
    ["Nama Peserta :", nama_peserta],
    ["Kode Paket :", kode_paket],
    ["Nama Paket :", nama_paket],
    ["Tarif Paket :", tarif_paket],
    ["Kode Tambahan :", kode_paket_tambahan],
    ["Fasilitas:", fasilitas],
    ["Tarif Tambahan :", tarif_paket_tambahan],
    ["PPN 11% :", ppn ],
    ["Jumlah Biaya :", jumlah_biaya ],
 ]

rincian_pembayaran = input('\n Ingin Tampilkan Rincian Pemesanan Anda? (y/t) : ')
if rincian_pembayaran == 'Y' or rincian_pembayaran == 'y':
    print(tabulate(rincian_pemesanan,headers="firstrow", tablefmt="fancy_grid"))
else:
    if rincian_pembayaran == 'T' or rincian_pembayaran == 't':
     cancel = input('\n Apakah Anda Ingin Membatalkan Pesanan? (y/t) :')
     if cancel == 'Y' or cancel =='y':
      print('Terimakasih Telah Mengujungi Kami\n')
      quit()
     elif cancel == 'T' or cancel == 't':
      print(tabulate(rincian_pemesanan,headers="firstrow", tablefmt="fancy_grid"))
      
# Daftar pembayaran

laporan_pembayaran = input('\n Mau Bayar Sekarang? (y/t) : ')
def laporan_pembayaran():
    while True:
        if laporan_pembayaran == 'Y' or laporan_pembayaran == 'y':
            bayar = int(input('\n Masukan Pembayaran Anda : '))
            if bayar == jumlah_biaya:
                print('\n Selamat Pembayaran Berhasil')
                status == 'Lunas'
                break
            elif bayar > jumlah_biaya:
                print('\n Selamat Pembayaran Berhasil')
                kembalian = bayar - jumlah_biaya
                print('\n Kembalian Anda : ', kembalian)
                status == 'Lunas'
                break
            elif bayar < jumlah_biaya:
                print('\n Pembayaran Gagal')
                kredit = bayar - jumlah_biaya
                print('\n Maaf Pembayaran Anda Kurang : ', kredit)
                status == 'Menunggu Pembayaran'
                break
        if laporan_pembayaran == 'T' or laporan_pembayaran == 't':
            print('Menunggu pembayaran')
            quit()
print('\n Tampilan Laporan pembayaran Anda \n')
daftar_pembayaran_lengkap = [
    ['No', 'Nama Peserta', 'Nama Paket', 'Fasilitas Tambahan', 'Jumlah Tarif', 'Status'],
    ['1', nama_peserta, nama_paket, fasilitas, jumlah_biaya, status]
]
print(tabulate(daftar_pembayaran_lengkap, headers='firstrow', tablefmt='fancy_grid'))