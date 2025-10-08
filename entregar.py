
qtdlanche= int(input("Quantidade de lanche"))
qtdsalgado= int(input("Quantidade de salgado"))
qtdrefri= int(input("Quantidade de refrigerante"))

total= (qtdlanche *15) + (qtdsalgado * 5) + (qtdrefri *6)

print(f" Valor total da conta :R$ {total: .2f}")