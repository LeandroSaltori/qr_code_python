def gerar_qrcode(exten, password, domain, port):
    import qrcode 
    img_qrcode = qrcode.make(f"""
    <?xml version="1.0" encoding='utf-8'?>
    <AccountConfig version='1'>
        <Account>
            <RegisterServer>{domain}:{port}</RegisterServer>"
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
    img_qrcode.save(f"QRCode-Ramal{exten}.png")
    return img_qrcode
   