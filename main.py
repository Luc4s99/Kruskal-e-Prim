"""
Trabalho 1 da disciplina de Tópicos em Grafos
Desenvolvido por: Lucas Mateus Menezes Silva; RA: 0035334

"""

# Biblioteca com funcionalidades do sistema operacional
import sys

# Importação da classe que define um Grafo
import Grafo

# Importação da classe que implementa as versões do algoritmo de Kruskal
import Kruskal

# Importação da classe que implementa o algoritmo de Prim
import Prim


# Função para leitura do arquivo de entrada
def le_arquivo_entrada(caminho_arquivo):

    qtd_vertices = int(caminho_arquivo.readline())
    qtd_arestas = int(caminho_arquivo.readline())

    ligacoes = caminho_arquivo.read().splitlines()

    # Instancia e monta um grafo
    grafo = Grafo.Grafo(qtd_vertices, qtd_arestas, ligacoes)

    # Fecha o arquivo que estava sendo lido
    caminho_arquivo.close()

    # Retorna o grafo montado
    return grafo


# Escreve o resultado em um arquivo de saída especificado pelo usuário
def escreve_resultados(arestas, algoritmo, arquivo):

    # Verifica qual algoritmo foi utilizado
    nome_algoritmo = ""

    if algoritmo == '1':

        nome_algoritmo = "Kruskal ingênuo"

    elif algoritmo == '7':

        nome_algoritmo = "Prim sem lista de prioridades"

    # Calcula o custo da AGM
    custo = 0

    # Informações para serem escritas no arquivo de saida
    info_arestas = ""

    for aresta in arestas:

        custo += aresta.peso
        info_arestas += str(aresta.vertice_i) + " " + str(aresta.vertice_f) + " " + str(aresta.peso) + "\n"

    # Escreve os dados no arquivo
    saida = open(arquivo, 'w')
    saida.write("Custo da Árvore Geradora Mínima com {}: {}".format(nome_algoritmo, str(custo)))
    saida.write("\n\nArestas:\n")
    saida.write(info_arestas)
    saida.close()


if __name__ == '__main__':

    # Devem ser passados exatamente 3 parâmetros para o programa mais o parâmetro do nome do arquivo para ser executado
    if len(sys.argv) != 4:

        print("Devem ser passados 3 parâmetros: \n")
        print("x(1 ou 2); indica qual algoritmo deve ser utilizado")
        print("arq-in; Caminho par ao arquivo com a instância de entrada")
        print("arq-out; Caminho para o arquivo que será gerado pelo programa\n\n")
    else:

        # Lendo e validando os argumentos passados via linha de comando
        if int(sys.argv[1]) != 1 and int(sys.argv[1]) != 2:
            print("Parâmetro 1 inválido, deve ser informado um número: 1 ou 2")

        # Tenta ler o arquivo de entrada e obter todas as informações
        # Caso não consiga lança uma excessão
        try:

            with open(sys.argv[2], 'r') as arquivo_entrada:

                grafo_montado = le_arquivo_entrada(arquivo_entrada)
        except IOError:

            print("Arquivo {} não encontrado.".format(sys.argv[2]))

        # Instanciamento da classe que representa o algoritmo de Kruskal
        kruskal = Kruskal.Kruskal()

        # Instanciamento da classe que implementa o algoritmo de Prim
        prim = Prim.Prim()

        # Lista de arestas que contém a representação da AGM
        arestas_agm = []

        # Verifica qual algoritmo o usuário selecionou
        # Apenas a versão mais recente do python proporciona uma estrutura switch case, mas ainda não tenho essa versão
        if sys.argv[1] == '1':

            arestas_agm = kruskal.kruskal_ingenuo(grafo_montado)
        elif sys.argv[1] == '2':

            arestas_agm = prim.prim_simples(grafo_montado)

        # Verifica se durante a geração dos resultados ocorreu algum erro
        if arestas_agm == -1:

            print("Ocorreu um erro durante a geração da Árvore Geradora Mínima")
        else:

            escreve_resultados(arestas_agm, sys.argv[1], sys.argv[3])
            print("Arquivo de saída gerado com sucesso!")



