class Forum:
    id = 0
    def __init__(self, nom, description = "")
        self.id = Forum.id
        Forum.id += 1
        self.nom = nom
        self.description = description
        self.publications = []