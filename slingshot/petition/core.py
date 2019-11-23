class Petition():

    def __init__(self):
        self.value_of_cause = 0
        self.dano_moral = 0
        self.pet_type = None
        self.author = []
        self.counter_part = []
        self.preliminars = []
        self.facts = []
        self.the_law = []
        self.requests = []
        self.docs = []

        self._request_obj_list = []
        self.compiled = False
        pass

    def summary(self):
        assert self.compiled == True, "Precisa compilar a peticao"
        
        print("{}".format(self.pet_type))
        for i in self._request_obj_list:
            print("{}:".format(i.layer_type), "Valor: R$ {}".format(i.value), sep="\t")
        print("Total: \t{}".format(self.value_of_cause))
        

    def add(self, request):
        request.petition = self
        self._request_obj_list.append(request)
        pass

    def compile(self):
        self._request_obj_list.sort(key= lambda i: i.priority, reversed=True)
        for request in self._request_obj_list:
            request._add()
        self.compiled = True
        if self.dano_moral:
            base = "A condenacao da parte re ao pagamento de um total de R$ {} a titulo de danos morais, em virtude do exposto"
            base = base.format(self.dano_moral)
        pass

    def save_txt(self):
        pass
