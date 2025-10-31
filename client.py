import socket
import time

# Sunucu IP ve port bilgisi
HOST = "127.0.0.1"  
PORT = 5550

# İstemci soketi oluşturuluyor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("💬 Sunucuya bağlanıldı!")

# Sunucuya sürekli "merhaba" gönder
while True:
    # "merhaba" gönder
    client_socket.sendall("merhaba\n".encode("utf-8"))
    print("📤 Gönderildi: merhaba")

    # Sunucudan cevap al
    data = client_socket.recv(1024).decode("utf-8").strip()
    print(f"📩 Sunucudan: {data}")

    # Eğer sunucu "Derdin ne senin?" dediyse öğrenci numarasını gönder
    if data == "Derdin ne senin?":
        time.sleep(1)
        ogr_no = "22060348"  # kendi öğrenci numaranı buraya yaz
        client_socket.sendall(f"{ogr_no}\n".encode("utf-8"))
        print(f"🎓 Öğrenci numarası gönderildi: {ogr_no}")

        # Sunucudan son mesajı al
        data = client_socket.recv(1024).decode("utf-8").strip()
        print(f"📩 Sunucudan: {data}")
        break

    # Araya küçük bir bekleme koyalım
    time.sleep(1)

client_socket.close()
print("🔒 Bağlantı kapatıldı.")
