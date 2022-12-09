# Classe Node para definiçao dos nodos

# Cada nodo tem um respetivo nome e ID

class Node:

    # Construtor do nodo
    def __init__(self, name, id=-1):
        self.m_id = id
        self.m_name = str(name)
        # posteriormente podera ser colocodo um objeto que armazena informação em cada nodo.....
        # {'(1,2)': (4,5)}

    def __str__(self):
        return "node " + self.m_name

    def __repr__(self):
        return "node " + self.m_name

    def setId(self, id):
        self.m_id = id

    def getId(self):
        return self.m_id

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name  # são iguais se nome igual, não usa o id

    def __hash__(self):
        return hash(self.m_name)
