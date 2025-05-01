def helloWorld():
    print("hello world")    
    print("hello world2")  
    olaOtavio() 

def oleGerson():
    print("ola gerson")
    
    number = 200
    number2 = 100
    
    print(number >= 200 or number2 < 100)
    if number >= 300 or number2 < 100:
        print("verdadeiro ")
    else: 
        print("false")



def olaOtavio():
    print("ola otavio")
    isTrue = "verdadeiro"
    
    print(isTrue == "verdadeiro1")
    if isTrue == "verdadeiro1":
        print("Verdadeiro")
        print("Verdadeiro")
        print("Verdadeiro")
        print("Verdadeiro")
        print("Verdadeiro")
    else:
        print("Falso")
        print("Falso")
        print("Falso")
        print("Falso")
        
    print("Fora dos if e else")
        
def pessoa(nome, altura, idade, vivo=True):
    print(nome, altura, idade, vivo)


def somaDeDuasVariaveis(num1, num2=200):
    resultado = num1 + num2
    print(resultado)
    
    return 100


def connectSwitch(telnet_ssh):
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    
    try:
        if telnet_ssh == "cisco_ios_telnet":
            print("Connecta no SSH")
        else:
            raise ValueError("Erro em python aleatorio")
    except:
        connectSwitch('cisco_ios_telnet')
    
    
    
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    print("Execulta outros codigos")
    
def expArray():
    varArr = [1, 2, 3, 4, 5, 6, 7] # array de numeros
    frutas = ["abacate", "uva", "laranja", "maçã"]
    varArrMix = ["otavio", 23, True, 3.4978]
    
    # [1, 2, 3, 4, 5, 6, 7] = [0, 1, 2, 3, 4, 5, 6]
    print(varArr[2])
    # len(frutas) : tamanho da array (len(arr))
    print(len(frutas))
    frutas.append("banana")
    frutas.remove("banana")
    frutas.pop(3)
    
    print(frutas)
    
def lacoRepeticao():
    frutas = ["abacate", "uva", "laranja", "maçã"]
    # fruta in frutas
    for f in frutas:
        print(f)


    
def lacoRepeticao2():
    for i in range(5):
        print(i)
    
    i = 0
    while i < 10:
        print(i) 
        i += 1
    
def dicionarioPyton():
    # pessoa = {
    #     "nome": "Gerson",
    #     "idade": 23,
    #     "altura": 1.70,
    #     "vivo": True
    # }

    # print(pessoa["nome"], pessoa["vivo"])
    # cisco_881 = {
    #     'device_type': "telnet_ssh",
    #     'ip': "ip_switch",
    #     'username': 'netadmins',
    #     'password': 'n&w@pnI2d2R',
    # } 
    
    {
        "nome": "Gerson",
        "idade": 23,
        "altura": 1.70,
        "vivo": True
    } 
    
    pessoas = [
        {
            "nome": "Gerson",
            "idade": 23,
            "altura": 1.70,
            "vivo": True
        },
        {
            "nome": "Gerson1",
            "idade": 23,
            "altura": 1.70,
            "vivo": True
        },
        {
            "nome": "Gerson2",
            "idade": 23,
            "altura": 1.70,
            "vivo": True
        },
        {
            "nome": "otavgio",
            "idade": 10,
            "altura": 1.76,
            "vivo": False
        }
    ]
    
    print(pessoas[1]["nome"])
        

def senhas():
    
    senhas = [
        {
            "usuario": "toor",
            "senha": "R2d2"
            
        },
        {
            "usuario": "netadmins",
            "senha": "n@w"    
        }
    ]
    
    for s in senhas:
        print(s["usuario"])



# Retornar esse dicionario
Valores = [
    {
        "portas" = 24,
        "portas_em_uso" = 32
        "novo"

    }
    
    
    
]



    # print(senhas[1]["senha"])
# connectSwitch('cisco_ios')
    

pessoa("gerson", 1.70, 23)
# helloWorld()
# olaOtavio()
# oleGerson()

# retTest = somaDeDuasVariaveis(2)

# print(retTest)

# expArray()
# lacoRepeticao()

# lacoRepeticao2()
# senhas()



                    



""" WHILE """



def inpar():
    numero = 0
    while numero < 10:
        if numero % 2 != 0:
            print("numero: ", numero)    
        numero+=1


def cinquenta_while():
    numero = 0
    while numero < 50:
        print(numero, numero)
        
def test_scam():
    
    soma = 0
    
    while soma >= 50:
        soma = int(input("Digite o numero: "))
        print(soma)
        
def for10():
  
    for n in range(100):
        print(n)
    
def doisemdois():
    soma = 0
    # numero = [0]
    
    for n in range(5):
        soma+=2    
        print(soma)
        
def paresfor():
    
    pares = 0

        
    for p in range(10):
        print(p)
        print("p % 2 == 0: ", p % 2 == 0)
        print("p % 2: ", p % 2)
        
        if p % 2 == 0:
            print("PAR: ", p)
    
    
def inparfor():

    for p in range(10):
        if p % 2 !=0:
            print("Inpar: ", p)
    
    
# inparfor()

def ordemProcedencia():
    calc = 3 + ((3 - 4) * (11 / 29))
    print(calc)
    
# ordemProcedencia()

""" 1. Fazer um programa em C que pergunta um valor em metros e imprime o
correspondente em decímetros, centímetros e milímetros. """

""" 
    definir variavel metro
    definir variaveis 
    dec 
    cm  
    mm
    Perguntar o valor em metro
    converter para decimentro
    converter em centimetros
    converter em militros
    printar dec
    printar cm
    printar mm
"""
def converter_metros():
    metro = int(input("Digite o valor em metros: "))
    dec = metro * 10
    cm = metro * 100
    mm = metro * 1000
    
    print(dec)
    print(cm)
    print(mm)    
    
    
    
# converter_metros()

""" 2. Fazer um programa em C que imprime uma tabela com a tabuada de 1 a 9 """

""" 
    definir variavel resultado
    definir variavel n1
    definir variavle n2
    repetir calculo 
    printar calculo e resultado
    n1 + n2 =
     * 9
        
"""


def tabuada():
    
    for n1 in range(11):
        for n2 in range(10):
            # print("n1: ", n1)
            # print("n2: ", n2)
            print(n1 ,"+", n2, "=", n1 + n2)
        print("\n")
        
# tabuada()

"""  
4. Fazer um programa em "C" que pergunte um valor em graus Fahrenheit e
imprime no valor o correspondente em graus Celsius usando as fórmulas que
seguem.
"""
""" 
    pedir valor em fahrenheit
    converter valor fahrenheit para celsios
    printar celsios
"""


def celcios():
    
    fahr = int(input("Insira valor em Fahrenheit: "))
    celc = (fahr - 32) * 5/9  
    
    print(celc,"º")

# celcios()

""" 
Peça ao usuário dois números e exiba a soma.

"""

def pedir_soma():
    
    pri = int(input("Insira o primeiro numero: "))
    seg = int(input("Insira o segundo numero: "))
    print("resultado = ", pri + seg)
    
# pedir_soma()

""" 

Calcule o dobro, triplo e a raiz quadrada de um número.

"""

def dobro_triplo_quadra():
    num = int(input("Insira o numero que deseja calcular: "))
    dobro = num * 2 
    triplo = num * 3
    quadra = num * num            

    print("\n",dobro,"\n",triplo,"\n",quadra)


# dobro_triplo_quadra()

""" 

Converta metros para centímetros e milímetros.

"""


def convert_metros():
    metros = int(input("Insira o valor Metros: "))
    cm = metros * 100
    mm = metros * 1000
    print(cm,"cm")
    print(mm, "mm")

# convert_metros()


"""

Calcule a média de duas notas.

"""


# criar array e ler o tamanho dela
# print(len(frutas))

""" 
Interface Speed Local pair Pair length        Remote pair Pair status
--------- ----- ---------- ------------------ ----------- --------------------
Fa0/11    auto  Pair A     1    +/- 1  meters N/A         Open
                Pair B     0    +/- 1  meters N/A         Short
                Pair C     N/A                N/A         Not Supported
                Pair D     N/A                N/A         Not Supported
"""


def mani_string():
    str_cmm = """          
    nada de interesse           
    
    PARAM_A        12         
    PARAM_B        n/a
    PARAM_C        0
    PARAM_D        78
    
    nada de intereçe          
    
    """
    
    # print(str_cmm[13:20])
    
    # print(str_cmm.find("PARAM_A") + 6)
    # paramA = str_cmm[str_cmm.find("PARAM_A"):str_cmm.find("PARAM_A") + 20]
    # valA = paramA.replace('PARAM_A','').strip()
    
    dicio = {
        'param_a': str_cmm[str_cmm.find("PARAM_A"):str_cmm.find("PARAM_A") + 20].replace('PARAM_A','').strip(),
        'param_b': str_cmm[str_cmm.find("PARAM_B"):str_cmm.find("PARAM_B") + 20].replace('PARAM_B','').strip(),
        'param_c': str_cmm[str_cmm.find("PARAM_C"):str_cmm.find("PARAM_C") + 20].replace('PARAM_C','').strip(),
        'param_d': str_cmm[str_cmm.find("PARAM_D"):str_cmm.find("PARAM_D") + 20].replace('PARAM_D','').strip()
    }
    
    print(dicio["param_a"])
    
        
    
    

    # print(dicio)
    
    # vall = ('Vall', [str_cmm.find('PARAM_A')])
    # vall1 = ['Vall', [str_cmm.find('PARAM_A')]]
    # print(vall[0])
    # print(vall1)
    
    # dicionario = {
        
    #     str_cmm[38:43]: str_cmm[54:55]
        
    # }
    
    
    # print(vall)
    # print(dicionario)    
    # print("STRING: ", str_cmm)
    # print("tipo: ", type(str_cmm))
    
    # print("FIND: ", str_cmm.find("int"))
    # print("FIND ins: ", str_cmm[str_cmm.find("int")])
    
    # # str_cmm.find("int") => 18
    # # len(str_cmm) => 89
    
    # # str_cmm[18:89]
    
    # # print(len(str_cmm))
    
    # print(str_cmm[str_cmm.find("int"):len(str_cmm)])
    # print(str_cmm[str_cmm.find("int"):len(str_cmm)].replace(" ", ""))
    
    # print("FIND tipo: ", type(str_cmm.find("int")))
    
    
# mani_string()


def dez_while():
    numero = 0

    while numero <= 10:
        print(numero)
        numero += 1

# dez_while()

def dez_for():
       
    for n in range(11):
        print(n)

# dez_for()

def cem_w():
    numero = 0
    while numero <= 100:
        print(numero)
        numero += 1
        
# cem_w()

def cem_f():
    
    for n in range(101):
        print(n)
    
# cem_f()

def cem_dois_w():
    numero = 0
    while numero <= 100:
        print(numero)
        numero += 2
        
# cem_dois_w()

def cem_dois_f():
    
    numero = [0]
    
    for n in numero:
        n += 2
        print(n)
        numero.append(n) 
        if n == 100:
            break   
    
    soma = 0
    
    for n in range(50):
        soma+=2
        print(soma)


# cem_dois_f()


def quinhentos_par_w():
    
    numero = 0
    
    while numero <= 500:
        numero +=1      
        if numero % 2 == 0:
            print(numero)
    
# quinhentos_par_w()


def quinhentos_par_f():
    
    for n in range(500):
        if n % 2 == 0 and n != 0:
            print(n)
        
# quinhentos_par_f()


def quinhentos_inp_w():
    
    numero = 0
    
    while numero <= 10:
        if numero % 2 == 1:
            print(numero)
        numero+=1
        
# quinhentos_inp_w()

def quinhentos_inp_f():
    
    for i in range(500):
        if i % 2 == 1 and i != 0:
            print(i)
    
# quinhentos_inp_f()

def calculadora_f(num):
    
    for r in range(10):
        print(r,'+',num,'=',r+num)
        
# calculadora_f(20)
    
def calculadora_w(num):
    
    numero = 0
    
    while numero <= 9:
        print(numero,'+',num,'=',numero+num)
        numero += 1 
        
calculadora_w(10)    

