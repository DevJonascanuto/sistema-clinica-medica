from typing import List, Dict
import sys

def ler_inteiro(prompt: str, minimo: int = None, maximo: int = None) -> int:
    """Lê um número inteiro do usuário, validando."""
    while True:
        entrada = input(prompt).strip()
        if entrada == '':
            print('Entrada vazia — digite um número.')
            continue
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f'O valor deve ser >= {minimo}.')
                continue
            if maximo is not None and valor > maximo:
                print(f'O valor deve ser <= {maximo}.')
                continue
            return valor
        except ValueError:
            print('Entrada inválida — digite um número inteiro.')

def ler_texto(prompt: str, obrigatorio: bool = True) -> str:
    """Lê uma linha de texto, validando se é obrigatório."""
    while True:
        texto = input(prompt).strip()
        if obrigatorio and texto == '':
            print('Este campo é obrigatório. Digite novamente.')
            continue
        return texto

def cadastrar_paciente(pacientes: list[Dict]) -> None:
    """Cadastra um paciente (nome, idade, telefone)."""
    print('\n--- Cadastro de Paciente ---')
    nome = ler_texto('Nome do paciente: ')
    idade = ler_inteiro('Idade: ', minimo=0)
    telefone = ler_texto('Telefone (ou deixar em branco se não tiver): ', obrigatorio=False)
    paciente = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }
    pacientes.append(paciente)
    print('Paciente cadastrado com sucesso!\n')

def estatisticas(pacientes: list[Dict]) -> None:
    """Calcula e exibe estatísticas dos pacientes."""
    print('\n--- Estatísticas ---')
    total = len(pacientes)
    print(f'Número total de pacientes cadastrados: {total}')
    if total == 0:
        print('Nenhum paciente cadastrado. Não há estatísticas a mostrar.\n')
        return

    # Calcular média de idades
    soma_idades = sum(p['idade'] for p in pacientes)
    idade_media = soma_idades / total
    print(f'Idade média dos pacientes: {idade_media:.2f} anos')

    # Paciente mais novo e mais velho
    mais_novo = min(pacientes, key=lambda p: p['idade'])
    mais_velho = max(pacientes, key=lambda p: p['idade'])
    print(f"O paciente mais novo: {mais_novo['nome']} - {mais_novo['idade']} anos")
    print(f"O paciente mais velho: {mais_velho['nome']} - {mais_velho['idade']} anos\n")

def buscar_paciente(pacientes: List[Dict]) -> None:
    """Busca paciente(s) pelo nome (case-insensitive, busca parcial)."""
    print("\n--- Buscar Paciente ---")
    termo = ler_texto("Digite o nome (ou parte do nome) para buscar: ").lower()
    resultados = [p for p in pacientes if termo in p['nome'].lower()]
    if not resultados:
        print("Nenhum paciente encontrado com esse termo.\n")
        return
    print(f"{len(resultados)} paciente(s) encontrado(s):")
    for i, p in enumerate(resultados, start=1):
        print(f"{i}. Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")
    print()



def listar_pacientes(pacientes: List[Dict]) -> None:
    """Exibe todos os pacientes cadastrados de forma organizada."""
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    # Ordenar por nome para facilitar leitura (opcional)
    ordenados = sorted(pacientes, key=lambda p: p['nome'].lower())
    largura_nome = max(len(p['nome']) for p in ordenados) if ordenados else 10
    # Cabeçalho
    print(f"{'Nº':>3}  {'Nome':{largura_nome}}  {'Idade':>5}  Telefone")
    print("-" * (6 + largura_nome + 12))
    for i, p in enumerate(ordenados, start=1):
        tel = p['telefone'] if p['telefone'] else "-"
        print(f"{i:>3}  {p['nome']:{largura_nome}}  {p['idade']:>5}  {tel}")
    print()


def menu() -> None: # menu principal do sistema
     pacientes: List[Dict] = []
     while True:
        print('==== sistema clinica vida + ====')
        print(' 1. cadastrar paciente ')
        print(' 2.  ver estatísticas ')
        print(' 3. buscar paciente')
        print(' 4. listar todos os pacientes')
        print(' 5. sair')
        escolha =  ler_texto('escolha uma opção: ')
        if escolha == '1':
           cadastrar_paciente(pacientes)
        elif escolha == '2':
           estatisticas(pacientes)
        elif escolha == '3':
           buscar_paciente(pacientes)
        elif escolha == '4':
            listar_pacientes(pacientes)
        elif escolha == '5':
            print('encerrando o sistema . até logo!')
            break
        else:
            print ('opção invalida, selecione uma opção valida e tente novamente.\n')

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário. Saindo...')
        sys.exit(0)
