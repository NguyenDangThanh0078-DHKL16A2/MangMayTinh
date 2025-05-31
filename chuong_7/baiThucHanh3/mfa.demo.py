import pyotp
import qrcode

# 1. Sinh secret key
secret = pyotp.random_base32()
print("SECRET:", secret)

# 2. Tạo URI chuẩn otpauth

totp = pyotp.TOTP(secret)
uri = totp.provisioning_uri(name="user@example.com", issuer_name="DemoApp")

# 3. Tạo mã QR để quét
img = qrcode.make(uri)
img.save("otp_qr.png")
print("Đã tạo mã QR trong file 'otp_qr.png'")