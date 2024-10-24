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
    