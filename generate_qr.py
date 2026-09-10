import qrcode

URL = "https://ofia.github.io/data_collector/"

img = qrcode.make(URL, error_correction=qrcode.constants.ERROR_CORRECT_H)
img.save("worker_signup_qr.png")

print(f"Saved worker_signup_qr.png pointing to {URL}")
