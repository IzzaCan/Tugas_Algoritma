print("Selamat Datang di pemesanan billing Warnet")

nomor_meja = input("Masukan nomor meja:")
tipe_paket = input("Pilih jenis paket (regular/premium/VIP): ")
durasi = float(input("Masukan berapa jam yang diinginkan: "))

harga_paket = {"regular": 5000, "premium": 7500, "VIP": 10000}

if tipe_paket in harga_paket:
    harga_perjam = harga_paket[tipe_paket]
    total_harga = harga_perjam * durasi
    print(f"Biaya total pemesanan untuk meja {nomor_meja} adalah Rp {total_harga}")
else:
    print("Jenis paket tidak valid.")