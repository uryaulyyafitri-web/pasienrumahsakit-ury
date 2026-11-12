print("=== DATA PASIEN RAWAT INAP RUMAH SAKIT ===")
nama = input("Masukkan nama pasien: ")
penyakit = input("Masukkan penyakit: ")
hari = int(input("Lama rawat inap (hari): "))
tambahan = 1000000

if hari > 3:
    biaya = (hari - 3) * tambahan
else:
    biaya = 0
print("\n=== HASIL DATA PASIEN ===")
print("Nama pasien:", nama)
print("Penyakit:", penyakit)
print("Lama rawat:", hari, "hari")
print("\n=== FASILITAS YANG DIDAPAT ===")
print("1. Tempat tidur pasien")
print("2. Makan 3 kali sehari")
print("3. Pemeriksaan dokter")
print("4. Pemeriksaan perawat")
print("5. Obat sesuai resep")
print("6. Ruangan rawat inap")
print("7. Fasilitas kamar mandi")
print("\n=== BIAYA TAMBAHAN ===")
if hari > 3:
    print("Rawat inap lebih dari 3 hari")
    print("Biaya tambahan: Rp", biaya)
else:
    print("Rawat inap tidak lebih dari 3 hari")
    print("Tidak ada biaya tambahan")
print("==============================")
print("Terima kasih")
