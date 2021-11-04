"""
Classe que define um grafo
"""

# Importa a classe que define as propriedades de um vértice
import Vertice

# Classe que representa uma aresta
import Aresta


class Grafo:

    # Construtor com todos os parâmetros necessários para montar a classe
    def __init__(self, qtd_vertices, qtd_arestas, ligacoes):

        self.qtd_vertices = qtd_vertices

        self.qtd_arestas = qtd_arestas

        self.ligacoes = ligacoes

        # Lista com as adjacências
        self.adjacencias = []

        # Lista que representa as arestas
        # Essa lista é utilizada para uma representação e ordenação mais fácil das arestas
        self.arestas = []

        self.monta_grafo()

        self.inclui_arestas()

    # Monta a representação do grafo utilizando lista de adjacências
    def monta_grafo(self):

        # Monta cada um dos vértices do grafo
        for i in range(self.qtd_vertices):

            # Instancia um vértice, já com seu label
            vertice = Vertice.Vertice(str(i))

            # Percorre todas as ligações
            for ligacao in self.ligacoes:

                # Adiciona as adjacencias do vertice
                if ligacao[0] == vertice.label:

                    vertice.vizinhos[ligacao[2]] = float(ligacao[4:])

            # Insere o vértice criado na lista de adjacências
            self.adjacencias.append(vertice)

    # Monta a representação das arestas a partir da lista de adjacências
    def inclui_arestas(self):

        for vertice in self.adjacencias:

            for vizinho, peso in vertice.vizinhos.items():

                self.arestas.append(Aresta.Aresta(vertice.label, vizinho, peso))
