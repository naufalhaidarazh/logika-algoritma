#penjual mangga menjual dagangan mangganya per kg dengan harga tertentu, jika pembeli ingin membeli mangganya, para pembeli harus membayarkan mangga tersebut sesuai dengan berat mangga yang dibeli. buat algoritma harga yang harus dibayar pembeli

print("=========================================================================")
print("Tugas Pertemuan 2 : Menghitung harga mangga yang harus dibayarkan pembeli")
print("=========================================================================")

hrg     = int(input("Masukkan harga mangga (per kg) : "))
brt     = int(input("Masukkan berat mangga yang dibeli (kg) : "))

byr     = hrg * brt
print("Jumlah harga mangga yang harus dibayarkan oleh pembeli sebesar Rp", byr)