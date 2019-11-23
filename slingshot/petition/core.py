class Petition():

    def __init__(self):
        """
        constructor of the Petition type.
        It has lists in order to archive the requests, authors, petition type, legal explanation of the requests and facts that hapenned
        To create it, you pass no parameters.

        You create your petition by instancing petition layers and introducing it with the .add method of the petition
        To organize your text, you use the .compile method, and then can visualize it with .print_text.

        Dano moral is a specific type of request that must be saved as an independent variable due to its importance on the requests
        """
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
        """
        Returns none, prints to the screen
        As this lib is inspired in keras, our petition model object has a summary function
        It gives us an ordered list of the petition titles and the final value of the cause
        """
        assert self.compiled == True, "Precisa compilar a peticao"
        
        print("{}".format(self.pet_type))
        print("#############")
        print("CAMADAS DA PETICAO:")
        for i in self._request_obj_list:
            print("{}".format(i.layer_type))
        print("#############")
        print("Valor da causa: R$ {}".format(self.value_of_cause))
        

    def add(self, layer):
        """

        With this method, you add a layer to the petition model
        Returns none and sets the petition of the layer to be the one where it is being added
        It is important in order to add the requests to value of the cause and interact with other layers on the same pet_model
        """
        layer.petition = self
        self._request_obj_list.append(layer)
        pass

    def compile(self):

        """
        This is one of the most important methods of the core petition model
        It compiles the petition by organizing its texts
        It sorts the request_obj_list to the correct order (by putting the parts and preliminaries first)
        Then calls each layer on the list method ._add to introduce its text blocks on the correct list of the petition

        It also, it has alleged moral damage, creates an specific request to it.
        It also crates a request with the value of the cause, which is important on Brazilian law-processes
        """
        self._request_obj_list.sort(key= lambda i: -1 * i.priority)
        for request in self._request_obj_list:
            request._add()
        self.compiled = True
        if self.dano_moral:
            base = "A condenacao da parte re ao pagamento de um total de R$ {} a titulo de danos morais, em virtude do exposto"
            base = base.format(self.dano_moral)
            self.requests.append(base)
        t1 = "Da-se a causa o valor de R$ {}".format(self.value_of_cause)
        self.requests.append(t1)
        pass
    
    def print_text(self):

        """
        This method prints the petition text on the screen and indexes each parraf
        """
        idx = 1
        print("EXMO SR JUIZ DE DIREITO DO JEC DO TJSP", end="\n\n\n\n")
        for text in self.author:
            print(text)
        for text in self.counter_part:
            print(text, end="\n\n")
        if len(self.preliminars) > 0:
            print("PRELIMINARES")
            for text in self.preliminars:
                print(str(idx) + ". " + text)
                idx += 1
        print("\nDOS FATOS")
        for text in self.facts:
            print(str(idx) + ". " + text)
            idx += 1
        print("\nDOS DIREITO")
        for text in self.the_law:
            print(str(idx) + ". " + text)
            idx += 1
        print("\nDOS PEDIDOS")
        p = 1
        for text in self.requests:
            print(str(p) + ". " + text)
            p += 1
        print("\nTermos em que pede deferimento")
        print(self.author_name)

    def save_txt(self):
        pass
