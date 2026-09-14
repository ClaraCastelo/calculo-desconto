#entrada para indicar o valor da compra
valor = float(input("insira valor da compra do cliente:"))

#processamento para calcular o desconto
if valor < 200:
    desconto_5= 5/100*valor
    valor_5 = valor-desconto_5
    print (f"você ganhou desconto de 5%, valor a ser pago é de {valor_5:.2f} reais")
#utilizei elif porque sao condições na mesma linha de raciocio
#o elif menor que 300 já considera o 200 dentro da condicao sem precisar delimitar ele, ja que a primeira condiçao considera ate 199
elif valor < 300:
    desconto_10= 10/100*valor
    valor_10 = valor-desconto_10
    print (f"você ganhou desconto de 10%, valor a ser pago é de {valor_10:.2f} reais")
elif valor >= 300:   
    desconto_15 = 15/100*valor
    valor_15 = valor-desconto_15
    print (f"você ganhou desconto de 15%, valor a ser pago é de {valor_15:.2f} reais")
