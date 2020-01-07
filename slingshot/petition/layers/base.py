"""
This module has the base layers for the petition models
The layers, on petitions, must inherit from the PetitionLayer in order for us to be sure they work
They must have a title, a priority (for the Petition.compile() method) and a request.
The ._add method Must be implmented on the specific layer, as they may hava different text lists to extract from
With those base layers we can create the ones that have actual content and can be used in chain to generate modular petitions
"""


class PetitionLayer():

    """
    This is our base model, and we treat it as an abstract class
    """
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
    """
    The part layer is also an abstract one (as has no ._add)
    its constructor receives name and address, so it can be from both the sued corporation or the author of the petiton
    It also has a parraf attribute, that is where we state the participation of the part on the process
    """
    def __init__(self, name, address):
        super(Part, self).__init__()
        self.layer_type = None
        self.petition = None
        self.name = name
        self.address = address
        self.parraf = []

class Context(PetitionLayer):
    """
    Context layers helps us in, on the start of the facts, set a start to the story
    For example, using a context layer we can state that the process happens in the context of a telephone plan
    Here we see that the ._add method sets our facts and has a very high priority.
    """
    def __init__(self):
        super(PetitionLayer, self).__init__()
        self.layer_type = "Contexto"
        self.fact = []
        self.priority = 100000
        self.value = None

    def _add(self):
        self.petition.facts.extend(self.fact)
        self.petition.main_req_type = self.pet_type
        self.petition.pet_type = self.pet_type

class Preliminary(PetitionLayer):
    """
    The preliminary petitions are used to set some requests on how the process will be judged
    They have also very high priority and a specific list of text for their request.
    They extend the preiliminars and request list of hte petition where it belongs
    """
    def __init__(self):
        super(Preliminary, self).__init__()
        self.layer_type = "Preliminar"
        self.preliminary_request = []
        self.priority = 1000
        self.value = None
    
    def _add(self):
        self.petition.preliminars.extend(self.preliminary_request)
        self.petition.requests.extend(self.request)

class Request(PetitionLayer):
    """
    The request layers extend the value of the cause and moral damage from the petition
    They also extend the the_law, requests, facts and docs list from the petition.
    """
    def __init__(self):
        super(Request, self).__init__()
        self.layer_type = "Pedido"
        self.fact = []
        self.law = []
        self.docs = []
        
    def _add(self):
        """
        this method puts all the text that the layers generate for the petition on its right places 
            for later printing and saving
        """
        self.petition.value_of_cause += self.value
        self.petition.dano_moral += self.dano_moral
        self.petition.facts.extend(self.fact)
        self.petition.the_law.extend(self.law)
        self.petition.requests.extend(self.request)
        self.petition.docs.extend(self.docs)


