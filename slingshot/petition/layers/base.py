class PetitionLayer():
    def __init__(self):
        self.title = None
        self.petition = None
        self.priority = 0
        self.layer_type = None
        self.value = None
        self.dano_moral = 0
        self.request = []

    def _add(self):
        raise NotImplementedError("This is an abstract method")

class Part(PetitionLayer):
    def __init__(self, name, address):
        super(Part, self).__init__()
        self.layer_type = None
        self.petition = None
        self.name = name
        self.address = address
        self.parraf = []

class Context(PetitionLayer):
    def __init__(self):
        super(PetitionLayer, self).__init__()
        self.layer_type = "Contexto"
        self.fact = []
        self.priority = 100000
        self.value = 0.

    def _add(self):
        self.petition.facts.extend(self.fact)
        self.petition.pet_type = self.pet_type
        self.petition.author.append(self.pet_type)

class Preliminary(PetitionLayer):
    def __init__(self):
        super(Preliminary, self).__init__()
        self.layer_type = "Preliminar"
        self.preliminary_request = []
        self.priority = 1000
        self.value = 0.
    
    def _add(self):
        self.petition.preliminars.extend(self.preliminary_request)
        self.petition.requests.extend(self.request)

class Request(PetitionLayer):
    def __init__(self):
        super(Request, self).__init__()
        self.layer_type = "Pedido"
        self.fact = []
        self.law = []
        self.docs = []
        
    def _add(self):
        self.petition.value_of_cause += self.value
        self.petition.dano_moral += self.dano_moral
        self.petition.facts.extend(self.fact)
        self.petition.the_law.extend(self.law)
        self.petition.requests.extend(self.request)
        self.petition.docs.extend(self.docs)


