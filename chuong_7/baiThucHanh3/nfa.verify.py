import pyotp

# Sử dụng lại secret key ở bước trên
secret = "CM33BEY3QPPF3NM5CXDZDZLGH7CZU4WV" # Lấy secret key được tạo trước đó
totp = pyotp.TOTP(secret)

# Bước 1: Nhập mật khẩu
password = input("Nhập mật khẩu: ")
if password != "123456":
    print("❌ Mật khẩu sai!")
    exit()

# Bước 2: Nhập mã OTP
otp = input("Nhập mã OTP từ Google Authenticator: ")
if totp.verify(otp):
    print("✅ Xác thực thành công! Bạn đã đăng nhập.")
else:
    print("❌ Mã OTP sai hoặc hết hạn.")