import qrcode

#name = str(input('Digite o nome do usuário do ramal: '))
exten = str(input('Digite o número do ramal: '))
password = str(input('Digite a senha do ramal: '))
domain = str(input('Digite o IP/DDNS: '))
port = 5060
# correio de voz = 


<?xml version="1.0" encoding='utf-8'?>
<AccountConfig version='1'>
	<Account>
		<RegisterServer>{exten}:{port}</RegisterServer>"
		<UserID>{exten}</UserID>
		<AuthID>{exten}</AuthID>
		<AuthPass>{password}</AuthPass>
		<AccountName>{exten}</AccountName>
		<DisplayName>{exten}</DisplayName>
		<Voicemail>*97</Voicemail>
		</Account>
</AccountConfig>
""")

