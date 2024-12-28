"""
Alat ini hampir sama dengan nss-v1 yang telah saya buat sebelumnya.
Perbedaannya adalah pada fungsi "for" dengan menambahkan +1.
Tujuannya agar pemindaian dimulai dari port awal dengan menambahkan angka 1 sampai port akhir.
Oleh karena itu, kita tidak lagi menambahkan list port pada kode. Kita bisa memindai
mulai dari awal hingga akhir port sesuai kebutuhan, sehingga nss-v2 ini dapat berjalan lebih
efisien dari nss-v1. Jika terdapat port yang terbuka maka port tersebut akan ditampilkan.
Jika tidak ada port yang terbuka maka program akan berhenti secara otomatis.
"""

import socket

def pemindai_port(target, port_awal, port_akhir):
    print(f"Memindai Target: {target}")
    for port in range(port_awal, port_akhir + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        hasil = sock.connect_ex((target, port))
        
        if hasil == 0:
            print(f"Port {port} Terbuka")

        sock.close()

if __name__ == "__main__":
    target = input("Masukkan IP Target: ")
    port_awal = int(input("Masukkan Angka Port Awal: "))
    port_akhir = int(input("Masukkan Angka Port Akhir: "))

    pemindai_port(target, port_awal, port_akhir)

"""
DISCLAIMER
Alat yang saya buat ini tidak berbahaya. Namun barang siapa yang menggunakannya pada jaringan yang ia tidak memiliki hak, izin, otoritas, dsb
dengan alasan apapun akan dianggap sebagai tindakan ilegal dan kriminal. Walaupun sederhana, alat ini masihlah alat peretasan seperti pedang bermata dua.
Saya harap kalian menggunakannya atas dasar pengetahuan dan kepatuhan terhadap hukum yang berlaku.
Segala tanggung jawab dan resiko ada di tangan kalian sendiri. Sekali lagi, mohon gunakan alat ini untuk kebajikan dan hal baik.
"""