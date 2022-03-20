#programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
ant = 0
pos = 1
result = 0

resp = int(input("Digite o numero que deseja verificar na sequência de Fibonacci:\n"))
while (result <= resp):
    result = ant + pos
    ant = pos
    pos = result

if ant == resp:
    print(f"O numero {resp} pertence a sequência!")
else:
    print(f"O numero {resp} não pertence a sequência!")