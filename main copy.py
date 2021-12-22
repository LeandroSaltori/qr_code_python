import qrcode

import qrcode

exten = str(input('Digite o número do ramal: '))
password = 
domain = str(input('Digite o IP/DDNS: '))

img = qrcode.make("""<?xml version="1.0" encoding='utf-8'?>
<AccountConfig version='1'>
	<Account>
		<RegisterServer>pabxeuro.ddns.com.br:5060</RegisterServer>"
		<UserID>900</UserID>
		<AuthID>900</AuthID>
		<AuthPass>Pr1sM4@Eurolatina#900</AuthPass>
		<AccountName>900</AccountName>
		<DisplayName>900</DisplayName>
		<Voicemail>*97</Voicemail>
		</Account>
</AccountConfig>
""")
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode.png")