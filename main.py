import qrcode


def generate_qr_code(hospital_url):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(hospital_url)
    qr.make(fit=True)


    img = qr.make_image(fill='black', back_color='white')


    img.save(f"hospital_registration_qr.png")


if __name__ == "__main__":

    hospital_url = "https://www.google.com/search?q=nigga&rlz=1C1ONGR_enIN1048IN1048&oq=nigga&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgcIARAAGI8CMgcIAhAAGI8C0gEIMjA2MWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8&sei=Mm_hZ9O5M7KjseMPrq7m6A0"  # Replace with actual registration URL
    generate_qr_code(hospital_url)
    print("QR code generated successfully!")
