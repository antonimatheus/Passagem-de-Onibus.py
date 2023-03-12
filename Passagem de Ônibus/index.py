def mostraLinha(tam=24):
    return '-=' * tam


def cabeçalho(txt):
    print(mostraLinha())
    print(txt.center(42))
    print(mostraLinha())


cabeçalho('PASSAGENS DE ÔNIBUS')
nome = str(input('Qual é o seu nome? '))
print(f'Seja Bem-Vindo a nossa companhia, {nome}!')
viagem = str(input(f'Gostaria de ver nossas passagens de ônibus? S/N ')).upper()
if viagem == 'S':
    contaminado = str(input('Somente uma pergunta! Você está contaminado com a COVID-19? S/N ')).upper()
    if contaminado == 'S':
        print(f'{nome}, o senhor(a) não pode prosseguir com sua viagem! Você está contaminado e será um risco para os outros passageiros!')
        print('Obrigado por visitar nossa companhia, volte quando estiver curado :)')

    elif contaminado == 'N':
        print('OK! o senhor(a) está liberado.')
        cabeçalho('TABELA DE PREÇO DE PASSAGENS')
        preços = [
                '[1] - passagem: R$10.00',
                '[2] - passagem: R$20.00',
                '[3] - passagem: R$30.00',
                '[4] - passagem: R$40.00'
            ]
        print(preços[0])
        print(preços[1])
        print(preços[2])
        print(preços[3])
        print('-=' * 24)

# de acordo com o número da passagem.. escolher e selecionar para compra
        escpreço = str(input(f'{nome}, o senhor(a) deseja adquirir alguma dessas passagens? S/N ')).upper()
        while True:
            if escpreço == 'S':
                psg = str(input('Escolha sua passagem de acordo com a numeração: Ex:[1] '))
                pagamento = [
                    '[1] - Dinheiro',
                    '[2] - Cartão',
                    '[3] - Pix',
                    '[4] - Milhas'
                ]
                if psg == '1': #Escolha 1

                    cabeçalho('QUAL FORMA DE PAGAMENTO? ')

                    print(pagamento[0])
                    print(pagamento[1])
                    print(pagamento[2])
                    print(pagamento[3])
                    print('-=' * 24)

                    while True:
                        cont = str(input('Qual forma de pagamento gostaria? '))
                        if cont == '1':  # dinheiro
                            print(pagamento[0])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break

                            break
                        elif cont == '2':  # cartão
                            print(pagamento[1])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '3':  # pix
                            print(pagamento[2])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '4':  # milhas
                            print(pagamento[3])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar == escpreço
                                    break

                                # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO


                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont not in ['1', '2', '3', '4']:
                            print("Opção inválida. Tente novamente.")
                            continue
                        else:
                            break

                    break
                elif psg == '2': #Escolha 2
                    cabeçalho('QUAL FORMA DE PAGAMENTO? ')

                    print(pagamento[0])
                    print(pagamento[1])
                    print(pagamento[2])
                    print(pagamento[3])
                    print('-=' * 24)

                    while True:
                        cont = str(input('Qual forma de pagamento gostaria? '))
                        if cont == '1': # dinheiro
                            print(pagamento[0])
                            #print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break

                            break
                        elif cont == '2': # cartão
                            print(pagamento[1])
                            #print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '3': #pix
                            print(pagamento[2])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '4': # milhas
                            print(pagamento[3])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont not in ['1', '2', '3', '4']:
                            print("Opção inválida. Tente novamente.")
                            continue
                        else:
                            break

                    break
                elif psg == '3': #Escolha 3
                    cabeçalho('QUAL FORMA DE PAGAMENTO? ')

                    print(pagamento[0])
                    print(pagamento[1])
                    print(pagamento[2])
                    print(pagamento[3])
                    print('-=' * 24)

                    while True:
                        cont = str(input('Qual forma de pagamento gostaria? '))
                        if cont == '1':  # dinheiro
                            print(pagamento[0])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break

                            break
                        elif cont == '2':  # cartão
                            print(pagamento[1])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '3':  # pix
                            print(pagamento[2])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '4':  # milhas
                            print(pagamento[3])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont not in ['1', '2', '3', '4']:
                            print("Opção inválida. Tente novamente.")
                            continue
                        else:
                            break

                    break
                elif psg == '4': #Escolha 4
                    cabeçalho('QUAL FORMA DE PAGAMENTO? ')

                    print(pagamento[0])
                    print(pagamento[1])
                    print(pagamento[2])
                    print(pagamento[3])
                    print('-=' * 24)

                    while True:
                        cont = str(input('Qual forma de pagamento gostaria? '))
                        if cont == '1':  # dinheiro
                            print(pagamento[0])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break

                            break
                        elif cont == '2':  # cartão
                            print(pagamento[1])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '3':  # pix
                            print(pagamento[2])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont == '4':  # milhas
                            print(pagamento[3])
                            # print('Compra Realizada! Boa Viagem!')
                            conticomprar = str(input('Deseja continuar a compra? S/N ')).upper()
                            while True:
                                if conticomprar == 'S':
                                    conticomprar = escpreço  # RESOLVER O LOOP PARA PODER CONTINUAR COMPRANDO
                                    break

                                elif conticomprar == 'N':
                                    print('Compra Realizada! Boa Viagem!')
                                    break
                                else:
                                    print('Opção inválida. Tente novamente.')
                                    break
                            break
                        elif cont not in ['1', '2', '3', '4']:
                            print("Opção inválida. Tente novamente.")
                            continue
                        else:
                            break

                    break
            else:
                print('Obrigado por visitar nossa companhia.')
                break
else:
    print('Obrigado por visitar nossa companhia.')
    