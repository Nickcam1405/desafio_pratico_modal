from calculadora import CalculadoraNotas

def calcular_emprestimo():
    nome = input("Digite o nome do colaborador: ")
    data_admissao = input("Digite a data de admissão (DD/MM/AAAA): ")
    salario_atual = float(input("Digite o salário atual do colaborador: "))
    valor_emprestimo = float(input("Digite o valor do empréstimo desejado: "))

    # Verificar se o colaborador atende aos requisitos mínimos
    tempo_casa = 2023 - int(data_admissao[-4:])
    if tempo_casa < 5:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return

    # Verificar se o valor do empréstimo é múltiplo de 2
    if valor_emprestimo % 2 != 0:
        print("Insira um valor válido!")
        return

    # Verificar se o valor do empréstimo não excede o limite permitido
    limite_emprestimo = salario_atual * 2
    if valor_emprestimo > limite_emprestimo:
        print("O valor do empréstimo excede o limite permitido.")
        return

    # Exibir opções de retirada
    print("Opções de retirada:")
    print("1. Notas de maior valor")
    print("2. Notas de menor valor")
    print("3. Notas meio a meio")
    
    opcao = int(input("Escolha a opção desejada: "))
    print()
    
    calculadora = CalculadoraNotas()
    
    
    print('Nome: ' + nome)
    print('Data de admissão: ' + data_admissao)
    print('Salario Atual: ' + str(salario_atual))
    print('Valor do emprestimo: ' + str(valor_emprestimo))
    print('Detalhes do saque: ')
    print()
    calculadora.calcular_notas(opcao, valor_emprestimo)
    print('------------------------------')
    
calcular_emprestimo()
