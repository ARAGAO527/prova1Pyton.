#--Cotadora de Lanche
valor = float(input("Digite o valor total do lanche: R$ "))

if valor <= 10.00:
    print("Preço justo")
elif valor <= 20.00:
    print("Está ficando caro!")
else:
    print("Muito caro, melhor levar de casa!")