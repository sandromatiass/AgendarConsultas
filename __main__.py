from data.data_paciente import pacientes
from src.paciente import consultar_paciente_por_cpf
from src.cadastro import cadastrar_cliente

def main():
    print("Bem-vindo ao sistema de agendamento de consultas!")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Consultar paciente por CPF")
        print("2 - Cadastrar novo cliente")
        print("3 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cpf_paciente = input("Digite o CPF do paciente que deseja consultar (apenas números): ")
            paciente = consultar_paciente_por_cpf()
            if paciente:
                print("\nPaciente encontrado:")
                print("Nome:", paciente['nome'])
                print("Telefone:", paciente['telefone'])
            else:
                print("\nPaciente não encontrado.")
        elif opcao == "2":
            cadastrar_cliente() 
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
