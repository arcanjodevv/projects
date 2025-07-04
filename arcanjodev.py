from datetime import datetime

def saudacao():
    agora = datetime.now()
    hora = agora.hour

    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def calculadora():
    print(saudacao())
    print("Calculadora Simples em Python")
    print("Operações: +  -  *  /")
    
    try:
        n1 = float(input("Digite o primeiro número: "))
        op = input("Escolha a operação: ")
        n2 = float(input("Digite o segundo número: "))

        if op == '+':
            resultado = n1 + n2
        elif op == '-':
            resultado = n1 - n2
        elif op == '*':
            resultado = n1 * n2
        elif op == '/':
            if n2 != 0:
                resultado = n1 / n2
            else:
                print("Erro: divisão por zero.")
                return
        else:
            print("Operação inválida.")
            return

        print(f"Resultado: {resultado}")
    except:
        print("Erro: entrada inválida.")

if __name__ == "__main__":
    calculadora()
