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
    #não consegui formatar os minutos certinho quando zera, no caso, quando a sprint é de 4 semanas
    min = tim%60
    return '{}h{} min'.format(hor,min)

def planning():
    sprint = int(input('Qual é o tempo da Spring em semanas? '))
    if sprint < 1:
        print('\nAlgo de errado que não está certo!\nA Sprint precisa ter entre 1 e 4 semanas.\n')
    else:
        plural = 's' if sprint > 1 else ''
        planning = 'O tempo do Planning Meeting é de {} horas.'.format(sprint*2)
        review = 'O tempo da Sprint Review é de {} hora{}.'.format(sprint,plural)
        retrospective = 'O tempo da Sprint Retrospective é de {}.'.format(min(sprint))
        print(
            '\nO tempo da Sprint é de {} semana{}.\n'.format(sprint,plural) + 
            'O tempo da Daily Meeting é sempre de 15 minutos\n' + 
            '{}\n{}\n{}\n'.format(planning,review,retrospective)
        )        

planning()