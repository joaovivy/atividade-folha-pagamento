def calcular_inss(salario_base):
    if salario_base <= 1100.00:
        inss = salario_base * 0.075
    elif salario_base <= 2203.48:
        inss = salario_base * 0.09
    elif salario_base <= 3305.22:
        inss = salario_base * 0.12
    elif salario_base <= 6433.57:
        inss = salario_base * 0.14
    else:
        inss = 854.36
    return inss

def calcular_irrf(salario_base, dependentes):
    deducao_dependente = 189.59 * dependentes
    base_irrf = salario_base - deducao_dependente
    
    if base_irrf <= 2259.20:
        irrf = 0
    elif base_irrf <= 2826.65:
        irrf = base_irrf * 0.075
    elif base_irrf <= 3751.05:
        irrf = base_irrf * 0.15
    elif base_irrf <= 4664.68:
        irrf = base_irrf * 0.225
    else:
        irrf = base_irrf * 0.275
    return irrf

def calcular_vale_transporte(salario_base, deseja_vale_transporte):
    if deseja_vale_transporte.lower() == 's':
        return salario_base * 0.06
    return 0

def calcular_vale_refeicao(valor_vale_refeicao):
    return valor_vale_refeicao * 0.20

def calcular_plano_saude(dependentes):
    return 150.00 * dependentes

def calcular_salario_liquido(salario_base, inss, irrf, vale_transporte, vale_refeicao, plano_saude):
    return salario_base - (inss + irrf + vale_transporte + vale_refeicao + plano_saude)
    
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
