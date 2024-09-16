funcionario = int(input("Digite o número do funcionario: "))
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
va_p_hora = float(input("Digite o valor por hora: "))

salario = horas_trabalhadas * va_p_hora
print(f"funcinario: {funcionario}")
print(f"salario do funcionario: ${salario:.2f}")