from function import gerar_qrcode
import tkinter as tk

"""
name = str(input('Digite o nome do usuário do ramal: '))
exten = str(input('Digite o número do ramal: '))
password = str(input('Digite a senha do ramal: '))
domain = str(input('Digite o IP/DDNS: '))
port = 5060
# correio de voz = str(input('Digite o Número Correo de voz: ')) 

gerar_qrcode(exten, password, domain, port)
"""

# Criando a interface Gráfica com TkInter.
janela = tk.Tk()

janela.title('QR Code - Prisma Telecom')

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text='Sistema Gerar QRCode Prisma Telecom', font='bold',fg='white', bg='black', width='35', height='1') # Fonte = Batman Forever
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')

#Nome Ramal
name_texto = tk.Label(text='Digite o nome do usuário do ramal: ')
name_texto.grid(row=1, column=0)
name = tk.Entry()
name.grid(row=1, column=1)

#Numero Ramal
exten_texto = tk.Label(text='Digite o número do ramal: ')
exten_texto.grid(row=2, column=0)
exten = tk.Entry()
exten.grid(row=2, column=1)

#Senha do ramal
password_texto = tk.Label(text='Digite a senha do ramal ')
password_texto.grid(row=3, column=0)
password = tk.Entry()
password.grid(row=3, column=1)

#IP / Dominio de registo do ramal
domain_texto = tk.Label(text='IP/ Dominio:  ')
domain_texto.grid(row=4, column=0)
domain = tk.Entry()
domain.grid(row=4, column=1)


#Gerar Botão
botao = tk.Button(text='Gerar QR Code', command=gerar_qrcode)
botao.grid(row=7, column=0, columnspan=2, sticky='NSEW')




janela.mainloop()