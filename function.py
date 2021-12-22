import qrcode 


def generate_qrcode(exten, password, domain):
    img_qrcode = qrcode.make(f"""
    <?xml version="1.0" encoding='utf-8'?>
    <AccountConfig version='1'>
        <Account>
            <RegisterServer>{domain}</RegisterServer>"
            <UserID>{exten}</UserID>
            <AuthID>{exten}</AuthID>
            <AuthPass>{password}</AuthPass>
            <AccountName>{exten}</AccountName>
            <DisplayName>{exten}</DisplayName>
            <Voicemail>*97</Voicemail>
            </Account>
    </AccountConfig>
    """)
    type(img_qrcode)  # qrcode.image.pil.PilImage
    return img_qrcode.save("qrcode.png")