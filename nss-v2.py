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