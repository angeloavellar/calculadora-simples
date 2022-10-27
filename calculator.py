def welcome():
    print('''Bem-vindo a calculadora'''
    )

#Defina a função
def calculate():
    operation = input('''
Por favor, digite o símbolo da operação que quer realizar
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('coloque o primeiro número: '))
    number_2 = int(input('coloque o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
    #Subtraction
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
    #Multiplication
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
    #Division
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não inseriu uma operação válida, por favor, execute o programa novamente')
    again()


#Definir função again() para perguntar se o usuário quer calcular novamente
def again():

    #Pedir input do usuário
    calc_again = input('''
Você quer calcular novamente?
Digite S para SIM ou N para NÃO.
''')

    #Se o usuário digitar S, rodar a função calculate()    
    if calc_again == 'S':
        calculate()

    #Se dititar N, se despedir e encerrar o programa
    elif calc_again == 'N':
        print('Obrigado e até logo!')

    #Se o usuário inserir outra letra, rodar a função novamente
    else:
        again()

#Rodar calculadora fora da função
welcome()
calculate()