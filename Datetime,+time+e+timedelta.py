import datetime
import time

# Módulo datetime

# Menor ano que pode se representado
print(datetime.MINYEAR)

# Maior ano que pode se representado
print(datetime.MAXYEAR)

# Classe date 
# Mostrar uma data
data = datetime.date(2022,12,21) # ano, mês e dia
print(data)
print(data.year, data.day, data.month)

# Que dia é hoje?
print(datetime.date.today())

# Menor data que pode se representada
print(datetime.date.min)

# Maior data que pode se representada
print(datetime.date.max)

# Classe datetime
# Que dia e hora são agora?
print(datetime.datetime.today())
#ou 
print(datetime.datetime.now())

# Data e hora com classe datetime
data_completa = datetime.datetime(2023, 11, 1, 13, 15, 55)
print(data_completa)
print(data_completa.month)
print(data_completa.hour)
print(data_completa.minute)

# Representar tempo com strings: strftime
agora = datetime.datetime.today()
print(agora.strftime("%d/%m/%Y"))
print(agora.strftime("%H:%M:%S"))

# Intervalos de tempo
hoje = datetime.datetime.now()
festa = datetime.datetime(2024,4,27,18,00) # usar 18h em vez de 00:00h
dias = festa - hoje
print(type(dias))
print(f'Faltam {dias.days} dias para a festa.\n')
# sem informação de hora precisa somar 1 a delta.days
print(f'Ou {dias.seconds} segundos.')

# Classe timedelta:  usada para representar diferenças de tempo, seja em dias, horas, minutos, segundos ou microssegundos.

from datetime import datetime, timedelta

# Exemplos:
# Criar um timedelta de 5 dias
delta_dias = timedelta(days=5)
# Acessar os atributos do timedelta
print(delta_dias.days)

# Criar um timedelta de 2 horas
delta_horas = timedelta(hours=2)

# Criar um timedelta de 30 minutos
delta_minutos = timedelta(minutes=30)

# Criar um timedelta de 1 semana e 3 dias
delta_semana_dias = timedelta(weeks=1, days=3)

# Operações com timedelta
# Obter a data e hora atuais
agora = datetime.now()

# Adicionar 42 dias à data atual ("o boleto vencerá em 42 dias, qua será esse dia?")
vencimento = agora + timedelta(days=42)
print(f'O boleto vence em {vencimento}')
# resultado formatado:
print(f'O boleto vence em {vencimento.strftime("%d/%m/%y")}.')

# Módulo time

# Descobrir epoch do sistema
print(time.gmtime(0))

# Timer: suspender a execuçao do script x segundos
print(f'Aguarde...')
time.sleep(3)
print(f'Aguardamos 3 segundos.')

# Hora formatada com strftime
hora = time.strftime("%H:%M:%S", time.localtime())
print(f'Agora são {hora} horas.')

# Número de segundos transcorridos desde epoch
print(time.time())
# Útil para armazenar tempo em bancos de dados, por ex.

# Converter x segundos desde epoch em string de data e hora
segundos = time.ctime(173637483)
print(f'Data: {segundos}')
print(f'Tempo atual: {time.ctime(time.time())}')







