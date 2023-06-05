class CalculadoraNotas:
    def calcular_notas(self, opcao, valor):
        if opcao == 1:
            self.calcular_notas_maior_valor(valor)
        elif opcao == 2:
            self.calcular_notas_menor_valor(valor)
        elif opcao == 3:
            self.calcular_notas_meio_a_meio(valor)
        else:
            print("Opção inválida. Escolha uma opção entre 1, 2 ou 3.")

    def calcular_notas_maior_valor(self, valor):
        notas = [100, 50]
        print("Notas de maior valor:")
        for nota in notas:
            quantidade = valor // nota
            valor %= nota
            if quantidade > 0:
                print("- {} x {} reais;".format(quantidade, nota))

        self.calcular_notas_menor_valor(valor)

    def calcular_notas_menor_valor(self, valor):
        notas = [20, 10, 5, 2]
        print("Notas de menor valor:")
        for nota in notas:
            quantidade = valor // nota
            valor %= nota
            if quantidade > 0:
                print("- {} x {} reais;".format(quantidade, nota))

    def calcular_notas_meio_a_meio(self, valor):
        print("Notas meio a meio:")
        self.calcular_notas_maior_valor(valor // 2)
        self.calcular_notas_menor_valor(valor // 2)



