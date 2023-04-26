"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""


sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
out = float(19849.53)
total = float(sp + rj + mg + es + out)
print('Total de venda na distribuidora foi R$ {:.2f}'.format(total))
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((out/total)*100)

print('Porcentagem de SP {:.2f}%'.format(psp))
print('Porcentagem de RJ {:.2f}%'.format(prj))
print('Porcentagem de MG {:.2f}%'.format(pmg))
print('Porcentagem de ES {:.2f}%'.format(pes))
print('Porcentagem de OUT {:.2f}%'.format(pout))