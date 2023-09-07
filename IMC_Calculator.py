import re

sexo = input("Digite seu sexo ('m' para masculino ou 'f' para feminino): ")

# Validação do sexo
while sexo.lower() not in ['m', 'f']:
    print("Sexo inválido. Por favor, digite 'm' para masculino ou 'f' para feminino.")
    sexo = input("Digite seu sexo (m para masculino ou f para feminino): ")

# Validação do peso
while True:
    pesoAtual = input('Digite seu peso em quilogramas (Exemplo: 82.5): ')
    if re.match(r'^\d+(\.\d{1})?$', pesoAtual):
        pesoAtual = float(pesoAtual)
        if 2.1 <= pesoAtual <= 600:
            break
    print("Valor inválido. Favor, insira um peso válido (entre 2.10 e 600) com o formato correto (exemplo: 82.50).")

# Validação da altura
while True:
    altura = input('Digite sua altura em metros (Exemplo: 1.71): ')
    if re.match(r'^\d(\.\d{2})?$', altura):
        altura = float(altura)
        if 0.50 <= altura <= 3.50:
            break
    print("Valor inválido. Favor, insira uma altura válida (entre 0.50 e 3.50) com o formato correto (exemplo: 1.71).")

# Inicializando a variavel pesoIdeal
pesoIdeal = ''

if sexo.lower() == 'm':
    pesoIdeal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    pesoIdeal = (62.1 * altura) - 44.7

imc = pesoAtual / (altura ** 2)

categoria = ''

if imc < 16:
    categoria = 'Magreza grave'
elif 16 <= imc < 17:
    categoria = 'Magreza moderada'
elif 17 <= imc < 18.5:
    categoria = 'Magreza leve'
elif 18.5 <= imc < 25:
    categoria = 'Saudável'
elif 25 <= imc < 30:
    categoria = 'Sobrepeso'
elif 30 <= imc < 35:
    categoria = 'Obesidade I'
elif 35 <= imc < 40:
    categoria = 'Obesidade II'
else:
    categoria = 'Obesidade III'

print(f'Seu IMC é: {imc:.1f}')
print('Sua categoria é:', categoria)
print(f'O peso ideal baseado na sua altura é de: {pesoIdeal:.2f}kg')

if pesoAtual > pesoIdeal:
    peso = pesoAtual - pesoIdeal
    print(f'Você precisa perder {peso:.2f}kg para atingir seu peso ideal')
elif pesoAtual < pesoIdeal:
    peso = pesoIdeal - pesoAtual
    print(f'Você precisa ganhar {peso:.2f}kg para atingir seu peso ideal')
else:
    print('Você já está no peso ideal!')