def main():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    
    salario_base = float(input("Digite seu salário base (R$): "))
    dependentes = 2  # Considerando apenas um dependente conforme as instruções
    deseja_vale_transporte = input("Deseja receber vale transporte? (s/n): ")
    valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))

    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)
    vale_transporte = calcular_vale_transporte(salario_base, deseja_vale_transporte)
    vale_refeicao = calcular_vale_refeicao(valor_vale_refeicao)
    plano_saude = calcular_plano_saude(dependentes)
    salario_liquido = calcular_salario_liquido(salario_base, inss, irrf, vale_transporte, vale_refeicao, plano_saude)
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    print(f"\nResumo da Folha de Pagamento:")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto Vale Transporte: R$ {vale_transporte:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Acréscimo Vale Refeição: R$ {vale_refeicao:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()
