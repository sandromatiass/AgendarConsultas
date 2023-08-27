import sys
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

diretorio_pai = os.path.dirname(diretorio_atual)

caminho_data = os.path.join(diretorio_pai, 'data')
sys.path.append(caminho_data)

from data_paciente import pacientes

def consultar_paciente_por_cpf(cpf):
    for paciente in pacientes:
        if paciente['cpf'] == cpf:
            return paciente
    return None

def main():
    cpf_paciente = input("Digite o CPF do paciente que deseja consultar (apenas números): ")
    paciente = consultar_paciente_por_cpf(cpf_paciente)
    if paciente:
        print("Paciente encontrado:")
        print("Nome:", paciente['nome'])
        print("Telefone:", paciente['telefone'])
        print("Data de Nascimento:", paciente['data_nascimento'])
        print("Gênero:", paciente['genero'])
        print("Email:", paciente['email'])
        print("CPF:", paciente['cpf'])
        print("Endereço:", paciente['endereco'])
        print("Convênio:", paciente['convenio'])
    else:
        print("Paciente não encontrado.")

if __name__ == "__main__":
    main()
