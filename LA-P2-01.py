# ibu ingin membeli telur sebesar 5kg, dan harga 1 kg telur adalah Rp 26000, dan ongkos sekali naik angkot(pulang pergi) sebesar Rp 3500. berapa sisa uang yang dimiliki ibu, jika ibu membawa uang sebesar Rp 200000

print("================================================================")
print("Tugas Pertemuan 2 : Menghitung sisa uang ibu saat membeli telur")
print("================================================================")

brt     = int(input("Masukkan berat telur (kg) : "))
hrg     = int(input("Masukkan harga telur (per kg) : "))
ongkos  = int(input("Masukkan biaya transport : "))
uang    = int(input("Masukkan jumlah uang yang dimiliki : "))

sisa=uang - (ongkos*2) - (brt * hrg)
print("Sisa uang ibu untuk membeli telur dan bepergian adalah sebesar Rp", sisa)