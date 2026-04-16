from random import randint

class Processo:
    def __init__(self, tempo_exec, tempo_chegada, prioridade):
        self.tempo_exec = tempo_exec
        self.tempo_chegada = tempo_chegada
        self.tempo_restante = tempo_exec
        self.prioridade = prioridade

def cria_processo_aleatorio():
    return Processo(randint(1, 12), randint(2, 15), randint(1, 20))

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
total_processos = 5

opcao = input('Os parâmetros serão aleatórios? (S/N): ').upper()

if opcao == 'S':
    for x in range(total_processos):
        lista_processos.append(cria_processo_aleatorio())
else:
    print("Insira os dados manualmente:")
    for i in range(total_processos):
        print(f"\nDados do Processo {i}:")
        t_exec = int(input("Tempo de execução: "))
        t_cheg = int(input("Tempo de chegada: "))
        prio = int(input("Prioridade: "))
        lista_processos.append(Processo(t_exec, t_cheg, prio))

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

    if opcao_2 == '7':
        mostrar_processos

    if opcao_2 =='8':
        opcao = input('Os parâmetros serão aleatórios? (S/N): ').upper()

        if opcao == 'S':
            
            lista_processos.clear()
            for x in range(total_processos):
                lista_processos.append(cria_processo_aleatorio())

       
        elif opcao == 'N':

            lista_processos.clear()
            print("Insira os dados manualmente:")
            for i in range(total_processos):
                print(f"\nDados do Processo {i}:")
                t_exec = int(input("Tempo de execução: "))
                t_cheg = int(input("Tempo de chegada: "))
                prio = int(input("Prioridade: "))
                lista_processos.append(Processo(t_exec, t_cheg, prio))
        
        mostrar_processos(lista_processos)
    
    if opcao_2 =='9':
        print('Saindo...')
        flag = False 


        


