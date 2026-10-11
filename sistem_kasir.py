namaToko = "Toko Annas"

namaCust = input("Masukkan nama anda: ")
namaProduk = input("Produk yg dibeli: ")
namaKategori = int(input("Kategori produk yg dibeli [0] = Elektronik, [1] = Fashion, [2] = Makanan: "))
hargaProduk = int(input("Harga produk(satuan) yg dibeli: "))
jumlahProduk = int(input("Jumlah produk yg dibeli: "))

subtotal = hargaProduk * jumlahProduk

produk = {"nama": namaProduk, "harga": hargaProduk, "jumlah": jumlahProduk}
kategori = ["Elektronik", "Fashion", "Makanan"]

print(f"===== {namaToko} =====\n")
print(f"Nama pembeli: {namaCust}")
print("Nama produk: ", produk["nama"])
print("Kategori produk: ", kategori[namaKategori])
print(f"Harga satuan: Rp{hargaProduk:,}".replace(",","."))
print("Jumlah produk: ", produk["jumlah"])
print("------------------------")
print(f"Total bayar: Rp{subtotal:,}".replace(",","."))
print("========================\n")
print("Terima kasih sudah berbelanja!")