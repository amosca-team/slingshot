import markdown
import pdfkit
import pypandoc

class Petition():

    def __init__(self):
        """
        constructor of the Petition type.
        It has lists in order to archive the requests, authors, petition type, legal explanation of the requests and facts that hapenned
        To create it, you pass no parameters.

        You create your petition by instancing petition layers and introducing it with the .add method of the petition
        To organize your text, you use the .compile method, and then can visualize it with .print_text.

        Dano moral is a specific type of request that must be saved as an independent variable due to its importance on the requests

        The attributes are:
        :value of the cause and dano moral: values on which the judgement will be based
        :author -> text list that states the author of the petition
        :counter_part -> text list that states the counter_part of the petition
        :pet_type -> bureaucratic type of the petition (string)
        :perliminars -> text list that states requests about some rules on which the judgement will be based
        :the law -> text list that states the legal explanation of the requests of the petition
        :facts -> text list that states the facts that made the author to ask for his requests
        :requests -> text list that states what the author is actually asking for
        :docs -> the documents that proof that the author is telling the proof (text list)
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
        self.file_name = None
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
        print("### **EXMO SR JUIZ DE DIREITO DO JEC DO TJSP**", end="\n\n\n\n")
        for text in self.author:
            print(text)
        for text in self.counter_part:
            print(text, end="\n\n")
        if len(self.preliminars) > 0:
            print("#### **PRELIMINARES**")
            for text in self.preliminars:
                print("**" + str(idx) + "."+ "** " + text, end="\n\n")
                idx += 1
        print("\n#### **DOS FATOS**")
        for text in self.facts:
            print("**" + str(idx) + "."+ "** " + text, end="\n\n")
            idx += 1
        print("\n#### **DO DIREITO**")
        for text in self.the_law:
            print("**" + str(idx) + "."+ "** " + text, end="\n\n")
            idx += 1
        print("\n#### **DOS PEDIDOS**")
        p = 1
        for text in self.requests:
            print("**" + str(p) + "."+ "** " + text, end="\n\n")
            p += 1
        print("\nTermos em que pede deferimento")
        print(self.author_name)

    def _get_text(self):

        """
        Gets the whole petition as a very big string
        """
        idx = 1
        as_txt = ''
        as_txt = as_txt + ("### **EXMO SR JUIZ DE DIREITO DO JEC DO TJSP**" + "<br/><br/><br/><br/><br/><br/><br/><br/><br/>\n\n")
        for text in self.author:
            as_txt = as_txt + text + "\n\n"
        for text in self.counter_part:
            as_txt = as_txt + text + "\n\n"
        if len(self.preliminars) > 0:
            as_txt = as_txt + ("\n\n<br/><br/>\n#### **PRELIMINARES**\n\n")
            for text in self.preliminars:
                as_txt = as_txt + "\n\n" + ("**" + str(idx) + "."+ "** " + text + "\n\n")
                idx += 1
        as_txt = as_txt + ("\n\n<br/><br/>\n#### **DOS FATOS**\n\n")
        for text in self.facts:
            as_txt = as_txt + "\n\n" + ("**" + str(idx) + "."+ "** " + text + "\n\n")
            idx += 1
        as_txt = as_txt + ("\n\n<br/><br>\n#### **DO DIREITO**\n\n")
        for text in self.the_law:
            as_txt = as_txt + "\n\n" + ("**" + str(idx) + "."+ "** " + text + "\n\n")
            idx += 1
        as_txt = as_txt + "\n\n<br/><br/>\n#### **DOS PEDIDOS**\n\n"
        p = 1
        for text in self.requests:
            as_txt = as_txt + "\n\n" + ("**" + str(p) + "."+ "** " + text + "\n\n")
            p += 1
        as_txt = as_txt + ("\n<br/><br/>Termos em que pede deferimento\n\n")
        as_txt = as_txt + self.author_name
        as_txt = as_txt + "\n\n" + '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
        #as_txt = as_txt + '<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>\
         #   <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\
          #  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>'
        return as_txt

    def _save_as_html(self, path):
        "Saves as .html file centralized, uses bootstrap"
        txt = self._get_text()
        self.file_name = path
        html = markdown.markdown(txt)
        html = '<div class=container>' + html + '</div<'
        html = '<div class="text-justify">\n' + html + '</div>'
        html = '<main class="bd-masthead" id="content" role="main">' + html + '</main>'
        html = '<head><meta charset="utf-8"></head>' + html
        with open(path+'.html', "w") as file:
            file.write(html)
    
    def _save_as_pdf(self):
        "gathers converts the html saved file to pdf"
        assert self.file_name is not None, "The html must be generated first"
        pdfkit.from_file(self.file_name+'.html', self.file_name+'.pdf')

    def _save_as_docx(self):
        output = pypandoc.convert(source=self.file_name+'.html',
                          format='html',
                          to='docx',
                          outputfile=self.file_name+'.docx')

    def save_document(self, path, to_pdf=True, to_word=False):
        self._save_as_html(path)
        if to_pdf:
            self._save_as_pdf()
        if to_word:
            self._save_as_docx()


