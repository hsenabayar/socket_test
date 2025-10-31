import socket

# Sunucu IP ve port bilgisi
HOST = "127.0.0.1"  
PORT = 5550

# Sunucu soketi oluşturuluyor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"🌐 Sunucu başlatıldı. Dinleniyor... ({HOST}:{PORT})")

# İstemciden bağlantı bekle
conn, addr = server_socket.accept()
print(f"🔗 Bağlantı kuruldu: {addr}")

# Gelen "merhaba" sayısını saymak için sayaç
merhaba_sayisi = 0
ESIK = 5  # Sunucunun sabrının taştığı nokta :)

while True:
    data = conn.recv(1024).decode("utf-8").strip()
    if not data:
        break

    print(f"📩 Gelen: {data}")

    if data.lower() == "merhaba":
        merhaba_sayisi += 1
        if merhaba_sayisi < ESIK:
            conn.sendall("sana da merhaba\n".encode("utf-8"))
        else:
            conn.sendall("Derdin ne senin?\n".encode("utf-8"))
    else:
        # Öğrenci numarası geldiyse kaydet
        with open("ogrenciler.txt", "a", encoding="utf-8") as f:
            f.write(f"{data}\n")
        conn.sendall("Kaydedildi. Görüşürüz.\n".encode("utf-8"))
        break

conn.close()
server_socket.close()
print("🔒 Bağlantı sonlandırıldı.")
