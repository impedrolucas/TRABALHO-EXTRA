print("CALCULADORA DO ÍNDICE DE MASSA CORPORAL(IMC)")

p = input("Informe seu peso\n")
a = input("Informe sua altura\n")

at = (float (a)*float(a))
imc = (float(p)/(at))

if imc <= 18.5:
    print("MAGRO OU ABAIXO DO PESO")
    print("RISCO DE DOENÇA: NORMAL OU ELEVADO")

if imc >= 18.6:
    print(imc)
    print("NORMAL OU EUTRÓFICO")
    print("RISCO DE DOENÇA: POUCO ELEVADO")

if imc >= 25:
    print(imc)
    print("SOBRE PESO OU PRÉ-OBESO")
    print("ESTÁ NORMAL")

if imc >= 30:
    print(imc)
    print("OBESIDADE I")
    print("RISCO DE DOENÇA: ELEVADO")

if imc >= 35:
    print(imc)
    print("OBESIDADE II")
    print("RISCO DE DOENÇA: MUITO ELEVADO")

if imc >= 40: 
    print(imc)
    print("OBESIDADE III")
    print("RISCO DE DOENÇA: MUITO ELEVADO")
    

