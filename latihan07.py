
# Latihan 7: Mengelompokkan Masalah

suhu_tertinggi = None
urutan_tertinggi = 0
banyak = 0
total = 0

for i in range(1, 9):
    suhu = int(input(f"Suhu pencatatan ke-{i}: "))

    if suhu_tertinggi is None or suhu > suhu_tertinggi:
        suhu_tertinggi = suhu
        urutan_tertinggi = i

    if suhu > 80:
        banyak += 1
        total += suhu

print("Suhu tertinggi:", suhu_tertinggi,
      f"(pencatatan ke-{urutan_tertinggi})")

if banyak > 0:
    rata_rata = round(total / banyak, 2)
    print("Suhu melebihi 80:", banyak, "kali")
    print("Rata-rata suhu yang melebihi 80:", rata_rata)
else:
    print("Tidak ada suhu yang melebihi 80")
