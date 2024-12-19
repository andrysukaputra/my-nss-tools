"""
Ini adalah program/alat pemindai port sederhana yang saya buat menggunakan Python.
Alat ini saya beri nama nss_v1.
Alat ini memindai port dalam jaringan seperti server, router, dll.
Alat ini dibuat menggunakan pustaka "socket" seperti fungsi "socket.AF_INET dan socket.SOCK_STREAM"
Oleh karena itu, pemindaian yang dijalankan tertuju pada jaringan TCP/IP.
"""

import socket

"""
Kita buat fungsi pemindai port yang terdiri dari 2 parameter.
Target: sebagai IP target yang nantinya kita masukkan.
Ports: list dari port mana saja yang akan dipindai.
"""
def pemindai_port(target, ports):
    """
    Setelah itu dibuatlah fungsi "Looping" menggunakan for-in.
    Hal tersebut dilakukan untuk memindai urutan port yang kita tuliskan.
    """
    for port in ports:
        """
        socket.AF_INET: Adalah parameter standar alamat IPv4 atau hostname.
        socket.SOCK_STREAM: Adalah parameter yang mengindikasikan bahwa ini adalah TCP.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        """
        setdefaulttimeout: Adalah besaran waktu timeout respon port terhadap alat pindai yang kita buat.
        Angka (1) artinya waktu timeout adalah satu detik.
        """
        socket.setdefaulttimeout(1)
        """
        connect_ex: Adalah pengait dari seluruh fungsi yang dimasukkan dalam variabel "hasil".
        Selain itu, ditambahkan fungsi "sock" yang telah dibuat sebelumnya yang
        berisis IPv4 dan TCP. Selanjutnya kita kembalikan nilainya ke dalam "target" dan "port".
        """
        hasil = sock.connect_ex((target, port))
        """
        Karena kita ingin hasil yang ditampilkan berupa "Terbuka" atau "Tertutup"
        Maka, kita buat fungsi "if-else". Jika nilai = 0 maka tampilkan "Terbuka", begitu pun sebaliknya.
        Jika list port sudah habis berdasarkan timeout 1 detik maka fungsi akan tertutup.
        """
        if hasil == 0:
            print(f"Port {port}: Terbuka")
        else:
            print(f"Port {port}: Tertutup")
        sock.close()
"""
target berisi input-an alamat IP. Di sisni saya menggunakan Google Public DNS Server (8.8.8.8)
"""
"""
Seperti yang telah disinggung sebelumnya, kita membutuhkan list port. Maka dari itu,
list port kita isikan dengan port berupa angka yang sering digunakan sebagai target scanning dan sniffing
seperti di bawah (Kalian juga bisa mencari port lainnya di internet). Kita menuliskannya dalam betuk list di Python dengan "[]".
Setelah itu kembalikan semua nilainya ke dalam fungsi "pemindai_port" yang berisi parameter
"target" dan "ports". Untuk menjalankannya, buka terminal setelah itu ketikkan "python nss_v1.py" tanpa tanda petik.
"""
if __name__ == "__main__":
    target = input("Masukkan IP target: ")
    print(f"Memindai target: {target}")
    ports = [21, 22, 53, 80, 443, 8080]
    
    pemindai_port(target, ports)

"""
PROS:
- Program ini sangat sederhana. Namun, dengan program ini kita dapat mengerti bagaimana cara port dipindai.
- Kita dapat membuat alat peretasan/cybersecurity dengan tangan kita sendiri.
- Melalui alat ini, kita bukan lagi "Script Kiddies".
- Meskipun alat ini juga berdasarkan referensi pencipta lainnya. Namun kita menuliskannya lagi sesuai
dengan bahasa kita dan kita mempelajari isisnya.
- Melalui alat ini kita tidak hanya menggunakan tools hacking yang sudah ada, tapi kita juga
belajar pemrograman, logika program, dan menghapai error.

CONS:
- Alat ini jauh dari kata kuat. Alat ini dapat terdeteksi dengan mudah pada jaringan sever atau router
yang memiliki keamanan tinggi. Alat ini bisa dianggap sebagai anomali sehingga respon port akan langsung ditutup.
- Alat ini tidak bisa menembus firewall yang kuat. Beberapa port dalam jaringan dengan keamanan tinggi selalu
memiliki firewall yang kuat.
- Banyak alat lain yang lebih kuat dari ini seperti NMAP, Aplikasi FIng, fungsi di Terminal, dll yang dikembangkan oleh
banyak orang, riset, dan berbagai metode yang lebih efisien.
- Perlu diingat bahwa alat ini hanya kita sendiri yang membuatnya, sehingga memiliki keterbatasan. Oleh karena itu,
alat ini efektif jika kalian coba di lab cyber anda sendiri atau jaringan dengan port yang sengaja kalian buka.
"""

"""
KESIMPULAN
Kenapa dengan Pemindaian Port? Port yang terbuka di dalam jaringan dapat menjadi titik masuk awal
penyalahgunaan peretas untuk potensi serangan cyber lanjutan atau yang lebih besar. Jika memang terbuka tanpa ada otorisasi,
maka celah tersebut harus segera diamankan dengan melakukan update port atau firewall melalui penyedia alat atau jaringan terkait.
Bisa juga dengan menghubungi konsultan cybersecurity untuk rekomendasi langkah-langkah keamanan.
"""

"""
DISCLAIMER
Alat yang saya buat ini tidak berbahaya. Namun barang siapa yang menggunakannya pada jaringan yang ia tidak memiliki hak, izin, otoritas, dsb
dengan alasan apapun akan dianggap sebagai tindakan ilegal dan kriminal. Walaupun sederhana, alat ini masihlah alat peretasan seperti pedang bermata dua.
Saya harap kalian menggunakannya atas dasar pengetahuan dan kepatuhan terhadap hukum yang berlaku.
Segala tanggung jawab dan resiko ada di tangan kalian sendiri. Sekali lagi, mohon gunakan alat ini untuk kebajikan dan hal baik.
"""