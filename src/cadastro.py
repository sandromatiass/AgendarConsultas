import sys
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

diretorio_pai = os.path.dirname(diretorio_atual)

caminho_data = os.path.join(diretorio_pai, 'data')
sys.path.append(caminho_data)

from data_paciente import pacientes

def cadastrar_cliente():
    print("==== Cadastro de Cliente ====")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
    genero = input("Gênero: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    convenio = input("Convênio: ")
    
    novo_cliente = {
        'nome': nome,
        'telefone': telefone,
        'data_nascimento': data_nascimento,
        'genero': genero,
        'email': email,
        'cpf': cpf,
        'endereco': endereco,
        'convenio': convenio
    }
    
    pacientes.append(novo_cliente)

    print("Cliente cadastrado com sucesso!")

def main():
    cadastrar_cliente()

if __name__ == "__main__":
    main()
