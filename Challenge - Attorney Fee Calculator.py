valor_causa=float(input('Informe o valor da causa: R$'))
percentual_honorarios=float(input('Informe o percentual de honorários: '))
despesas=float(input('Informe o valor das despesas processuais: R$'))

honorários=valor_causa*(percentual_honorarios/100)
total=honorários+despesas

print(f'Considerando que a causa tem valor de R${valor_causa}')
print(f'Os honorários sucumbenciais foram fixados em {percentual_honorarios:.2f}%')
print(f'As despesas do processo foram R${despesas}')
print(f'Os honorários terão valor R${honorários}')
print(f'Por fim, o valor total a ser pago será de R${total}')
