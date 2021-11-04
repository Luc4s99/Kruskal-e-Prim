"""
Classe que implementa o algoritmo de Kruskal e mais alguns métodos úteis para o mesmo

Esse código se inspira no artigo em: https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/kruskal.html#naive

A implementação do merge sort foi retirada em: https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/mergesort/
"""


class Kruskal:

    def __init__(self):
        pass

    # Implementação ingênua do algoritmo de Kruskal
    def kruskal_ingenuo(self, grafo):

        # Verifica antes se existe alguma aresta
        if len(grafo.arestas) == 0:
            return -1

        # Lista que indica os chefes
        chefes = []

        # Ordenando a lista de arestas do grafo
        self.mergesort(grafo.arestas, 0, len(grafo.arestas) - 1)

        # Define os chefes para cada componente conexa do grafo
        # Como inicialmente "não existe" nenhuma aresta, todos os vértices são seus próprios chefes
        for vertice in grafo.adjacencias:

            chefes.append(vertice.label)

        # Lista para armazenar as ligações da árvore geradora mínima
        ligacoes_agm = []

        # Percorre a lista de arestas já ordenada
        for aresta in grafo.arestas:

            # Verifica o número máximo de arestas, que é número de vértices - 1
            if len(ligacoes_agm) < grafo.qtd_vertices - 1:

                # Verifica se os chefes dos vértíces que compõe a aresta são diferentes
                if chefes[int(aresta.vertice_i)] != chefes[int(aresta.vertice_f)]:

                    # Armazena a ligação como uma ligação válida
                    ligacoes_agm.append(aresta)

                    # Atualiza os chefes, sempre dando prioridade para o chefe de menor valor
                    # Não necessariamente precisa ser o menor chefe, aqui é só para ser um padrão
                    menor_chefe = min(int(aresta.vertice_i), int(aresta.vertice_f))
                    chefe_anterior = max(int(aresta.vertice_i), int(aresta.vertice_f))

                    # Percorre a lista de chefes, trocando todas as ocorrências do chefe anterior pelo novo
                    for i in range(len(chefes)):

                        if chefes[i] == chefe_anterior:

                            chefes[i] = menor_chefe

        return ligacoes_agm

    # Método de ordenação escolhido: Merge Sort
    # Possui custo O(n log n) em todos os casos
    def merge(self, arestas, aux, esquerda, meio, direita):

        for k in range(esquerda, direita + 1):
            aux[k] = arestas[k]
        i = esquerda
        j = meio + 1
        for k in range(esquerda, direita + 1):
            if i > meio:
                arestas[k]= aux[j]
                j += 1
            elif j > direita:
                arestas[k] = aux[i]
                i += 1
            elif aux[j].peso < aux[i].peso:
                arestas[k] = aux[j]
                j += 1
            else:
                arestas[k] = aux[i]
                i += 1

    def mergesort(self, arestas, esquerda, direita):

        aux = [0] * len(arestas)

        if direita <= esquerda:
            return
        meio = (esquerda + direita) // 2

        # Ordena a primeira metade do arranjo.
        self.mergesort(arestas, esquerda, meio)

        # Ordena a segunda metade do arranjo.
        self.mergesort(arestas, meio + 1, direita)

        # Combina as duas metades ordenadas anteriormente.
        self.merge(arestas, aux, esquerda, meio, direita)