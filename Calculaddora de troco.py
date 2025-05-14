Conta = float(input(f"Digite o valor da conta: "))
Entregue = float(input(f"Digite o valor entregue: "))
Carteira = [200,100,50,25,10,5,1,0.5,0.25,0.1]

Troco = Conta - Entregue

if Entregue > Conta:
    Troco = Troco * -1
    print(f"Valor entregado maior do que a conta, o caixa te deve:R${Troco:.2F}")
else:
     print(f"Voce deve R${Troco:.2f} para o caixa")

for Valor in Carteira:
    qtd = int(Troco//Valor)
    if qtd > 0:
        print(f"Serão {qtd} x R${Valor:2F}")
        Troco -= qtd * Valor
        Troco = round(Troco,2)