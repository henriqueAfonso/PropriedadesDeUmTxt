#Henrique Afonso Martins
#19178


while True:
    print("------------------------------------\n")
    print("1 - Propriedades de um arquivo texto")
    print("2 - Sair\n")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        caminho_arquivo = input("Digite o caminho do arquivo para leitura: ")
        caminho_arquivo_saida = input("Digite o caminho do arquivo de saída: ")
        try:
            saida = open(caminho_arquivo_saida, "w")
            arquivo = open(caminho_arquivo, "r")

            vogais = 0
            consoantes = 0
            espacos = 0

            for letra in arquivo.read():
                if letra in "AEIOUaeiou":
                    vogais += 1
                elif letra == " ":
                    espacos += 1
                else:
                    consoantes += 1

            arquivo.close()

            saida.write("Arquivo:           " + caminho_arquivo)
            saida.write("\nVogais:            " + str(vogais))
            saida.write("\nConsoantes:        " + str(consoantes))
            saida.write("\nEspaços em branco: " + str(espacos))
            saida.write("\n-------------------------------------\n")

            saida.close()

            print("\n------------------------------------")
            print("Este arquivo contém: \n")
            print(str(vogais) + " vogais")
            print(str(consoantes) + " consoantes")
            print(str(espacos) + " espaços em branco")
        except :
            print("------------------------------------")
            print("\n          Arquivo inválido          \n")
            print("------------------------------------")
            break
    elif opcao == "2":
        break

    else:
        print("------------------------------------")
        input("\n           Opção inválida           \n")
        print("------------------------------------")
        break