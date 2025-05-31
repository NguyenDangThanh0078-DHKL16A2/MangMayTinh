import pyshark

cap = pyshark.FileCapture('C:\\Users\\ADMIN\\OneDrive\\Documents\\mang_may_tinh\\chuong_4\\kt\\dhkl16a2hn_kiemtra.pcapng')

for pkt in cap:
    try:
        print("=" * 30)
        # Lớp 2: Ethernet
        if 'eth' in pkt:
            print(f"MAC nguồn: {pkt.eth.src}")
            print(f"MAC đích: {pkt.eth.dst}")

        # Lớp 3: IP
        if 'ip' in pkt:
            print(f"IP nguồn: {pkt.ip.src}")
            print(f"IP đích: {pkt.ip.dst}")
    except AttributeError:
        continue
