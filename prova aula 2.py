contato={}

def adicionar_contato(nome,telefone,email):
    contato['nome'] = nome
    contato['telefone'] = telefone
    contato['email'] = email
    print(f'contato adicionado! o dicionario com as informações do contato ficou assim {contato}')

nome=input('digite o nome do contato que deseja adicionar: ')
telefone=input('digite o numero do contato que deseja adicionar: ')
email=input('digite o email do contato que deseja adicionar: ')

adicionar_contato(nome,telefone,email)
