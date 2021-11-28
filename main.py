from functions import *

### STATS:
    ### STRENGTH: A potência dos seus músculos
    ### AGILITY: Sua capacidade de se mover de forma complexa e ligeira.
    ### INTELLIGENCE: Seu potencial na arte de resolução de problemas práticos.
    ### WISDOM: Sua compreensão de conceitos abstratos (sentimentos, culturas, experiências).
    ### CHARISMA: Sua capacidade de convencer, enganar e fazer amizades.
    ### TOUGHNESS: O quão capaz é o seu corpo de suportar dano físico.
    ### PERCEPTION: Seu potencial em observar e ser alertado por detalhes sutis.
    ### WILLPOWER: Sua capacidade de suportar ataques mentais e de se manter coeso em meio à dor e caos.
    ### LUCK: Você é abençoado por boa fortuna, ou é muito bom em manipular as chances por debaixo dos panos.
    ### INSIGHT: Você sabe de acontecidos, entidades e fatos que ninguém deveria. Sem willpower equivalente, pode levar a loucura.

### GIFTED QUOTIENT:
    ### COMUM: 50 points
    ### INCOMUM: 75 points
    ### RARO: 100 points
    ### TALENTOSO: 125 points
    ### ÚNICO: 150 points
    ### LENDÁRIO: 200 points
    ### ABENÇOADO: 500 points
    ### XAMÃ: 1000 points

output = open('output.txt', 'a')
output.write(stat_ramdomizer(gq_randomizer()))
