def gerar_qrcode(exten, password, domain, port=5060):
    # Esta função gera o QR Code com as informaçoes recebidas do botão.;
    import qrcode 
    img_qrcode = qrcode.make(f"""
    <AccountConfig version='1'>
        <Account>
            <RegisterServer>{domain}:{port}</RegisterServer>"
            <OutboundServer>{domain}</OutboundServer>
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


