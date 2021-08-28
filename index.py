#Este código foi criado para auxiliar na contagem das horas das reuniões do método Scrum
#Criado por Jonatan Magrão
 
#Regra de negócio: Scrum

#É recomendado que:
#as Sprints tenham entre 1 e 4 semanas;
#cada Sprint Planning tenha 2 horas por cada semana de Sprint;
#o tempo da Sprint Daily seja de no máximo 15 minutos;
#cada semana de Sprint seja 1 hora de Review Meeting;
#a Sprint Retrospective seja de 45 minutos por semana de Sprint.  


import math

def min(week):
    tim = int(math.floor(45*week))
    hor = '0'+ str(math.floor(tim/60))
    min = tim%60
    min = f'0{min}' if min < 10 else min
    return f'{hor}h{min} min'

def planning():
    sprint = int(input('Qual é o tempo da Spring em semanas? '))
    if sprint < 1:
        print('\nAlgo de errado que não está certo!\nA Sprint precisa ter entre 1 e 4 semanas.\n')
    else:
        plural = 's' if sprint > 1 else ''       
        print(f'''
        O tempo da Sprint é de {sprint} semana{plural}.
        O tempo da Daily Meeting é sempre de 15 minutos.
        O tempo do Planning Meeting é de {sprint*2} horas.
        O tempo da Sprint Review é de {sprint} hora{plural}.
        O tempo da Sprint Retrospective é de {min(sprint)}.\n'''
        )

planning()