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
nome_texto = tk.Label(text='Digite o nome do usuário do ramal: ')
nome_texto.grid(row=1, column=0)
nome = tk.Entry()
nome.grid(row=1, column=1)
name = nome.get()

#Numero Ramal
ramal_texto = tk.Label(text='Digite o número do ramal: ')
ramal_texto.grid(row=2, column=0)
ramal = tk.Entry()
ramal.grid(row=2, column=1)

#Senha do ramal
senha_texto = tk.Label(text='Digite a senha do ramal ')
senha_texto.grid(row=3, column=0)
senha = tk.Entry()
senha.grid(row=3, column=1)

#IP / Dominio de registo do ramal
dominio_texto = tk.Label(text='IP/ Dominio:  ')
dominio_texto.grid(row=4, column=0)
dominio = tk.Entry()
dominio.grid(row=4, column=1)

#Porta de Registro do Ramal
porta_texto = tk.Label(text='Porta(5060):  ')
porta_texto.grid(row=5, column=0)
porta = tk.Entry()
porta.grid(row=5, column=1)

    
#Gerar Botão
def info_botao():    
    exten = ramal.get()
    password = senha.get()
    domain = dominio.get()
    port = porta.get()
    gerar_qrcode(exten,password,domain,port)


botao = tk.Button(text='Gerar QR Code', command=info_botao)
# botao.grid(row=6, column=0, columnspan=2, sticky='NSEW')
botao.grid(row=6, column=0, columnspan=2)


# Check box email
envia_email = tk.IntVar()
checkbox_email = tk.Checkbutton(text = 'Enviar QR Code por Email ', variable=envia_email)
checkbox_email.grid(row=9, column=0)


def enviar():
    print(envia_email.get())
    if envia_email.get():        
        # Criando janela info email.
        janela = tk.Tk()
        janela.title('Email')
        janela.rowconfigure(0, weight=1)
        janela.columnconfigure([0, 1], weight=1)
        mensagem = tk.Label(text=f'Email enviado para: ', font='bold',fg='white', bg='black', width='10', height='1') # Fonte = Batman Forever
        mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')
        janela.mainloop()
  
    

email_texto = tk.Label(text='E-mail:  ')
email_texto.grid(row=8, column=0)

botao_email = tk.Button(text='Enviar', command=enviar)
botao_email.grid(row=9, column=1, columnspan=2)

email = tk.Entry()
email.grid(row=8, column=1)




janela.mainloop()