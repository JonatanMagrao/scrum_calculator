//Este código foi criado para auxiliar na contagem das horas das reuniões do método Scrum
//Criado por Jonatan Magrão

/* 
    Regra de negócio: Scrum

    É recomendado que:
    as Sprints tenham entre 1 e 4 semanas;
    cada Sprint Planning tenha 2 horas por cada semana de Sprint;
    o tempo da Sprint Daily seja de no máximo 15 minutos;
    cada semana de Sprint seja 1 hora de Review Meeting;
    a Sprint Retrospective seja de 45 minutos por semana de Sprint.   

*/

function min_tim(total){
    hor = `0${Math.floor(total * 45/60%60)}`
    min = `0${Math.floor(total * 45%60)}`    
    return `${hor.slice(-2)}h${min.slice(-2)} min`
}

function planning(sprint){
    if(sprint < 1 || sprint > 4){
        console.log('Algo de errado não está certo!\nA Sprint precisa ter entre 1 e 4 semanas.')
    } else {
        const plural = sprint > 1 ? 's' : ''
    console.log(
    `\n    O tempo da Sprint é de ${sprint} semana${plural}.
    O tempo da Sprint Planning é de ${sprint * 2} horas.
    O tempo da Daily Meeting é sempre de 15 minutos.
    O tempo da Sprint Review é de ${sprint} hora${plural}.
    O tempo da Sprint Retrospective é de ${min_tim(sprint)}.`
    )}
}

planning(1)