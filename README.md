import random 
import copy

class Processo:
    def __init__(self, posicao, tempo_exec, tempo_chegada, prioridade):
        self.tempo_exec = tempo_exec
        self.tempo_chegada = tempo_chegada
        self.tempo_restante = tempo_exec
        self.prioridade = prioridade
        self.posicao = posicao

def cria_processo_aleatorio(posicao):
    return Processo(posicao, random.randint(1, 12), random.randint(2, 15), random.randint(1, 20))

def mostrar_processos(lista_processo): 
    print("\n--- Lista de Processos ---")
    for i, p in enumerate(lista_processo):
        print(f'Processo[{i}]: tempo_execução={p.tempo_exec} tempo_restante={p.tempo_restante} tempo_chegada={p.tempo_chegada} prioridade={p.prioridade}')
    print("--------------------------\n")

def formatar_media(media):
    formatado = f"{media:.8g}"
    if '.' not in formatado:
        return f'{media:.1f}'
    else:
        return formatado


lista_processos = []
total_processos = 3
posicao = 0

while len(lista_processos) != total_processos:

    opcao = input('Os parâmetros serão aleatórios? (S/N): ').upper()

    if opcao == 'S':
        for x in range(total_processos):
            lista_processos.append(cria_processo_aleatorio(posicao))
            posicao += 1
    elif opcao == 'N':
        print("Insira os dados manualmente:")
        for i in range(total_processos):
            print(f"\nDados do Processo {i}:")
            t_exec = int(input("Tempo de execução: "))
            t_cheg = int(input("Tempo de chegada: "))
            prio = int(input("Prioridade: "))
            lista_processos.append(Processo(posicao, t_exec, t_cheg, prio))
            posicao += 1 
    else:
        print(f'A escola e apenas de S ou N, define certo ai')

mostrar_processos(lista_processos)

flag = True
while flag:
    print('Escolha o algoritimo:')
    print('1 - FCFS')
    print('2 - SJF Preemptivo')
    print('3 - SJF Não preemptivo')
    print('4 - Prioridade Preemptivo')
    print('5 - Prioridade Não Preemptivo')
    print('6 - Round_Robin') 
    print('7 - Listar Processos')
    print('8 - Refazer processos')
    print('9 - Sair')
    
    
    opcao_2 = input()
    

    if opcao_2 == '1':
        lista_espera = []
        acumulador = 0
        for x in range(total_processos):
            lista_espera.append(acumulador)
            y = lista_processos[x]
            for c in range(y.tempo_exec):
                acumulador+= 1
                print(f'tempo: [{acumulador}] processo[{x}] restante:{y.tempo_restante-(c+1)}')
        print("")
        for a in range(len(lista_espera)):
            print(f'processo[{a}]: tempo_espera={lista_espera[a]}')
        soma = sum(lista_espera)
        media = soma/len(lista_espera)
        media = formatar_media(media)
        print(f'tempo restante média: {media}')
        print('--------------------------')

    if opcao_2 =='2':
        lista_copia = copy.deepcopy(lista_processos)
        tempo = 1
        lista_espera = []
        lista_espera_soma = []

        while lista_copia !=[]:
            disponivel = []
            for x in lista_copia:
                if x.tempo_chegada <= tempo:
                    disponivel.append(x)
            if disponivel == []:
                print(f'Tempo[{tempo}]:ainda não está pronto')
                tempo += 1
            else:
                disponivel.sort(key=lambda p: p.tempo_restante)
                processo = disponivel.pop(0)
                lista_copia.remove(processo)
                processo.tempo_restante -= 1
                print(f'tempo[{tempo}]: processo[{processo.posicao}] restante[{processo.tempo_restante}]')
                tempo += 1
                if processo.tempo_restante==0:
                    tempo_atual = tempo
                    tempo_retorno = tempo_atual - processo.tempo_chegada
                    tempo_espera = tempo_retorno - processo.tempo_exec
                    espera = (processo.posicao, tempo_espera)
                    lista_espera.append(espera)
                    lista_espera_soma.append(tempo_espera)
                else:
                    lista_copia.append(processo)
        print('--------------------------')
        lista_espera.sort()
        for e in range(len(lista_espera)):
            print(f'processo[{lista_espera[e][0]}]: tempo de espera = {lista_espera[e][1]}')
        print('--------------------------') 
        soma = sum(lista_espera_soma)
        if soma > 0:
            media = soma/len(lista_espera_soma)
            media = formatar_media(media)
            print(f'tempo restante média: {media}')
            print('--------------------------')   
        else:
            print(f'tempo restante média: {soma}')
            print('--------------------------') 
            



            
    
    if opcao_2 == '3':
        
        lista_copia = copy.deepcopy(lista_processos)
        tempo = 0
        tempo_simulado = 0
        lista_espera = []
        lista_espera_soma = []
        lista_organizada = []

        while lista_copia !=[]:
            disponivel = []
            for x in lista_copia:
                if x.tempo_chegada <= tempo_simulado:
                    disponivel.append(x)
            if disponivel == []:
                tempo_simulado += 1 
            else:
                disponivel.sort(key=lambda p: p.tempo_restante)
                processo = disponivel.pop(0)
                tempo_simulado += processo.tempo_exec
                lista_organizada.append(processo)
                lista_copia.remove(processo)

                tempo_atual = tempo_simulado
                tempo_retorno = tempo_atual - processo.tempo_chegada
                tempo_espera = tempo_retorno - processo.tempo_exec
                espera = (processo.posicao, tempo_espera)
                lista_espera.append(espera)
                lista_espera_soma.append(tempo_espera)
        
        for p in range(len(lista_organizada)):
            tempo_execucao = 0
            if lista_organizada[p].tempo_chegada > tempo:
                for t in range((lista_organizada[p].tempo_chegada - tempo)-1):
                    tempo += 1
                    print(f'tempo[{tempo}]: ainda não está pronto')
            for t in range(lista_organizada[p].tempo_exec):
                tempo += 1
                tempo_execucao += 1 
                print(f'tempo[{tempo}]: processo[{lista_organizada[p].posicao}] restante[{lista_organizada[p].tempo_restante - (tempo_execucao)}]')
        print('--------------------------')
        lista_espera.sort()
        for e in range(len(lista_espera)):
            print(f'processo[{lista_espera[e][0]}]: tempo de espera = {lista_espera[e][1]}')
        print('--------------------------') 
        soma = sum(lista_espera_soma)
        if soma > 0:
            media = soma/len(lista_espera_soma)
            media = formatar_media(media)
            print(f'tempo restante média: {media}')
            print('--------------------------')   
        else:
            print(f'tempo restante média: {soma}')
            print('--------------------------') 
                   
            
    

    
    if opcao_2 == '7':
        mostrar_processos

    if opcao_2 =='8':
        opcao = input('Os parâmetros serão aleatórios? (S/N): ').upper()
        posicao = 0
        if opcao == 'S':
            
            lista_processos.clear()
            for x in range(total_processos):
                lista_processos.append(cria_processo_aleatorio(posicao))
                posicao += 1 

       
        elif opcao == 'N':

            lista_processos.clear()
            print("Insira os dados manualmente:")
            for i in range(total_processos):
                print(f"\nDados do Processo {i}:")
                t_exec = int(input("Tempo de execução: "))
                t_cheg = int(input("Tempo de chegada: "))
                prio = int(input("Prioridade: "))
                lista_processos.append(Processo(posicao, t_exec, t_cheg, prio))
                posicao += 1
        
        mostrar_processos(lista_processos)
    
    if opcao_2 =='9':
        print('Saindo...')
        flag = False 


        


