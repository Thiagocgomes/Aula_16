from datetime import datetime, timedelta


#1 - Peça ao usuário que insira seu ano de nascimento e calcule sua idade.


data  = input("Digite sua data de nascimento (ano-mes-dia):")
dat  = datetime.strptime(data, "%Y-%m-%d")

data_atual  = datetime.now()

age  =  data_atual.year - dat.year - ((data_atual.month, data_atual.day) < (dat.month, dat.day))

print(age)


#2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.

data_atual = datetime.now()
data_atual = data_atual + timedelta(days=7)
print(data_atual)

#3 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).

data_atual = datetime.now()
print(data_atual.strftime(("%d/%m/%y %H:%M:%S")))