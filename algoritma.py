uang = int(input("Masukkan jumlah uang Anda (Rp): "))


if uang >= 20000:
     menu = "Ayam Geprek + Es Teh"
     catatan = "uang cukup untuk makan enak!"
else:
     menu = "Mie Instan + Telur"
     catatan = "berhemat dulu."


print("-" * 40)
print(f"Hasil Analisis Menu:")
print(f"Menu Terpilih : {menu}")
print(f"Catatan       : {catatan}")



