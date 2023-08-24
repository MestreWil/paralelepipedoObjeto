from paralelepipedo import Paralelepipedo

pipedo = Paralelepipedo()

while True:
  menu = -1
  try:
    while menu not in (0, 1, 2):
      menu = int(input('Digite uma das opções abaixo:\n[ 0 ] Encerrar\n[ 1 ] Imprimir\n[ 2 ] Definir um novo paralelepípedo\nSua opção: '))
  except:
    print('-'*55)
    print('Por favor, digite um número correspondente as opções!!')
    print('-'*55)
  match menu:
    case 2:
      pipedo.limpa()
      print('-'*30)
      print('Defina seu PARALELEPÍPEDO:')
      print('-'*30)
      try:
        l1 = float(input('Comprimento: '))
        l2 = float(input('Largura: '))
        l3 = float(input('Alutura: '))
        pipedo.novo(l1, l2, l3)
        print('PARALELEPÍPEDO ANALISADO COM SUCESSO!')
      except:
        print('-'*55)
        print('Por favor, digite um número correspondente as opções!!')
        print('-'*55)
    case 1:
      print(f'{pipedo.show()}')
    case 0:
      print('Volte sempre!')
      break