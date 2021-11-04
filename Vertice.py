"""
Classe que define um vértice
"""


class Vertice:

    def __init__(self, label):

        # Cada vértice possui um label único que o identifica
        self.label = label

        # E uma lista de vizinhos
        self.vizinhos = {}
