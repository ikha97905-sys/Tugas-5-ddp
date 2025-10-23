
# Program Menghitung Luas Bangun Datar (Versi Simpel)


print("--- Hitung Luas Bangun Datar ---")
print("1: Persegi")
print("2: Lingkaran")
print("3: Segitiga")


try:
    pilih = int(input("Masukkan pilihan (1/2/3): "))
except ValueError:
    pilih = 0 # Jika input non-angka, dianggap salah


match pilih:
    case 1:
        
        try:
            s = float(input("Masukkan sisi: "))
            luas = s * s
            print(f"Luas Persegi: {luas}")
        except ValueError:
            print("Input sisi harus angka.")

    case 2:
       
        try:
            r = float(input("Masukkan jari-jari: "))
            luas = 3.14 * r * r
            print(f"Luas Lingkaran: {luas}")
        except ValueError:
            print("Input jari-jari harus angka.")

    case 3:
       
        try:
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))
            luas = 0.5 * a * t
            print(f"Luas Segitiga: {luas}")
        except ValueError:
            print("Input alas dan tinggi harus angka.")

    case _:
        
        print("salah pilih")
