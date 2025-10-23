
list_kendaraan = [
    "namaKendaraan",
    "JenisKendaraan",
    "ccKendaraan",
    "warnaKendaraan",
    "rodaKendaraan"
]

print(f"1.list pertama: {list_kendaraan}")
list_kendaraan.extend(["harga_kendaraan", "tipe_kendaraan"])
print(f"2.list kedua: {list_kendaraan}")
list_kendaraan.insert(2, "merk_kendaraan")

print(f"3. List ketiga: {list_kendaraan}")
