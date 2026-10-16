#looping masukkan penanda dan data kosong

total = 0
banyak = 0

#
durasi = int(input("waktu proses(menit, -1 selesai): "))
while durasi != -1:
      total = total + durasi
      banyak = banyak + 1
durasi = int(input("waktu proses(menit, -1 selesai): "))

if banyak == 0:
      print("belum ada data yang dimasukkan")

else:
    print("Banyak data:", banyak)
    print("Rata-rata:", round(total / banyak, 2), "menit")

      # waktu proses (menit, -1 selesai): 10 
      # waktu proses (menit, -1 selesai): 15
      # waktu proses (menit, -1 selesai): -1
      # ditandai -1  itu false di while 
      # banyak data 2 (menghitung berdasarkan true,false tidak dihitung)
      #rata rata 12.5 menit (hasil dari pembagian 10 + 15 / 2 = 25 / 2 = 12.5 menit )


      
      
      
      
