# Uso: python make_qr.py https://SEU-USUARIO.github.io/dominox-festival/
import sys, qrcode
q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=14, border=3)
q.add_data(sys.argv[1]); q.make(fit=True)
q.make_image(fill_color="#0a2a5e", back_color="white").save("qrcode-dominox.png")
