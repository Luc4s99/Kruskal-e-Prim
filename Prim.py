"""

Classe que implementa o algoritmo de Prim

"""
# Classe que representa uma aresta
import Aresta


class Prim:

    def __init__(self):

        pass

    # Algoritmo de Prim simples, sem a implementação de uma fila de prioridades
    def prim_simples(self, grafo):

        # Verifica antes se existe alguma aresta
        if len(grafo.arestas) == 0:
            return -1

        # Lista que representa os pais de cada vértice
        # Apenas o vértice onde será iniciado o processo que se torna pai dele mesmo
        # Neste caso onde todos os vértices terão label começando de 0, o 0 sempre será o primeiro
        pais = [0]

        # Define os pais para cada um dos vértices, nenhum deles terá pai
        for vertice in grafo.adjacencias:

            pais.append(-1)

        # Lista para armazenar as ligações da árvore geradora mínima
        ligacoes_agm = []

        # Começa o loop principal
        # Enquanto ainda existirem arestas para serem colocadas na AGM o loop continua
        while len(ligacoes_agm) < grafo.qtd_vertices:

            # Auxiliares para encontrar o menor vizinho
            pai = ''
            menor_vizinho = ''
            menor_peso = 10000

            # Procura o menor vizinho dentre os vértices que já tem pai
            for vertice in grafo.adjacencias:

                # O vértice só pode ser analisado se ele já possuir um pai
                if pais[int(vertice.label)] != -1:

                    # Procura pela aresta de menor peso que faz parte das ligações desse vértice
                    for vizinho, peso in vertice.vizinhos.items():

                        # O vértice vizinho não pode ser um vértice com pai, para evitar loops
                        if pais[int(vizinho)] == -1:

                            if peso < menor_peso:

                                menor_vizinho = vizinho
                                menor_peso = peso
                                pai = vertice.label

            # Se tiver encontrado algo
            if pai != '':

                # Adiciona a aresta encontrada na AGM
                ligacoes_agm.append(Aresta.Aresta(pai, menor_vizinho, menor_peso))

                # Atualizando a lista de pais
                pais[int(menor_vizinho)] = pai
            else:

                break

        return ligacoes_agm
