from .base import *

class Author(Part):
    def __init__(self, name, address, cpf, profession):
        super(Author, self).__init__(name, address)
        self.layer_type = "Autor"
        self.CPF = cpf
        self.profession = profession
        self.priority = 1000000000
        self.create_parraf()
    
    def create_parraf(self):
        base = "{}, {}, domiciliado em {}, sob o CPF {} vem diante da Vossa Exa. ajuizar"
        base = base.format(self.name, self.profession, self.address, self.CPF)
        self.parraf.append(base)


    def _add(self):
        self.petition.author.extend(self.parraf)

class CounterPart(Part):
    def __init__(self, name, address, cnpj):
        super(CounterPart, self).__init__(name, address)
        self.layer_type = "Parte Re"
        self.CNPJ = cnpj
        self.priority = 1000000000 - 1
        self.create_parraf()
    
    def create_parraf(self):
        base = """Em face de {}, com sede em {}, sob o CNPJ {}, pelas razoes de fato e Direito aqui expostas:"""
        base = base.format(self.name, self.address, self.CNPJ)
        self.parraf.append(base)

    def _add(self):
        self.petition.counter_part.extend(self.parraf)


class InversaoOnusProva(Preliminary):
    def __init__(self):
        super(InversaoOnusProva, self).__init__()
        self.layer_type = "Preliminar - Inversao onus da prova"
        self.set_text()
    
    def set_text(self):
        self.set_request()
        self.set_preliminary()
    
    def set_preliminary(self):
        base = "Em virtude da nitida situacao de hipossuficiente da parte autora, " \
        "do art XXXX do CDC e art XXX do CPC e CC e dos julgados XXXX, faz-se necessaria" \
        "inversao do onus da prova em favor da parte autora neste processo."
        self.preliminary_request.append(base)
        
    def set_request(self):
        base = "Seja deferida a inversao do onus da prova em favor da parte autora."
        self.request.append(base)

class CobrancaIndevida(Request):
    def __init__(self, tarifas_cobradas, valor, docs):
        super(CobrancaIndevida, self).__init__()
        self.layer_type = "Cobranca indevida"
        self.value = valor
        self.tarifas = tarifas_cobradas
        self.docs = docs
        self.set_texts()
    
    def set_texts(self):
        self.set_facts()
        self.set_law()
        self.set_requests()
    
    def set_facts(self):
        docs = str(self.docs).replace("[", "").replace("]", "")
        tarifas = str(self.tarifas).replace("[", "").replace("]", "")
        base = "Conforme a documentacao anexa {}, a parte re cobrou indevidamente " \
        "da autora valores que perfazezm o montate de R$ {}, sob a invalida justificativa " \
        " de corresponderem a {}".format(docs, self.value, tarifas)
        t1 = "A parte autora ressalta que jamais anuiu com a cobranca desses valores, seja como prestacao de servicos adicionais" \ 
        ", reajuste no plano ou qualquer outro tipo de cobranca, de maneira que resta ilicita e incorreta a referida cobranca de valores."
        self.fact.append(base)
        self.fact.append(t1)
        
    def set_law(self):
        base = "De acordo com o Art XXX do CDC, quando houver cobranca indevida, o consumidor tem direito" \
        "a repeticao do indebito em dobro, que foi validado em jurisprudencia XXXX"
        self.law.append(base)
        
    def set_requests(self):
        base = "A repeticao do indebito em dobro, de acordo com o exposto e no valor de R$ {}"
        base.format(str(self.value * 2))
        self.request.append(base)

class ImpossivelCancelar(Request):
    def __init__(self, dano_moral, docs=False):
        super(ImpossivelCancelar, self).__init__()
        self.layer_type = "Impossivel cancelar plano"
        self.value = dano_moral
        self.dano_moral += dano_moral
        self.docs = docs
        self.set_texts()
    
    def set_texts(self):
        self.set_facts()
        self.set_law()
        self.set_requests()
    
    def set_facts(self):
        base = "Ocorre que a parte autora vem tentando, sem sucesso, cancelar seu plano e, depois " \
        "de varias tentativas, nao conseguiu ter sucesso. Isso se deu por conduta ativa e dolosa " \
        "da parte re que, desnecessariamente demora excessivamente e dificulta toda forma de comunicacao" \
        "no que diz respeito ao cancelamento do plano."
        t1 = "Vale dizer que a parte re sempre mostrou prontidao quando do momento da contratacao, mas " \
        "quando se quis proceder o cancelamento, passou a agir com essa conduta desrespeitosa que causou " \
        "grande desconforto e sentimento de humilhacao, traduzido em dano moral, para a parte autora."
        self.fact.append(base)
        self.fact.append(t1)
        if self.docs:
            docs = str(self.docs).replace("[", "").replace("]", "")
            t2 = "Isso encontra respaldo documental na documentacao anexa ({})".format(docs)
            self.fact.append(t2)
        
    def set_law(self):
        base = "Ademais do dano moral, cuja necessidade de ressarcimento tem resguardo legislativo" \
        "no Codigo Civil art XXXX, o mesmo, para esse tipo de caso do consumidor, encontra respaldo no" \
        "art XXXX do CDC"
        t1 = "Existe ainda respaldo jurisprudencial no sentido de entender a gravidade e a necessidade de " \
        "ressarcimento deste tipo de dano, como nos julgados XXXX"
        self.law.append(base)
        self.law.append(t1)
        
    def set_requests(self):
        base = "O cancelamento imediato de todos os servicos que a parte re se recusou a cancelar ou dificultou o cancelamento."
        self.request.append(base)


class RegistroSerasa(Request):
    def __init__(self, divida_registrada, valor, docs):
        super(RegistroSerasa, self).__init__()
        self.layer_type = "Registro indevido no Serasa"
        self.value = valor
        self.suposta_divida = divida_registrada
        self.docs = docs
        self.set_texts()
    
    def set_texts(self):
        self.set_facts()
        self.set_law()
        self.set_requests()
    
    def set_facts(self):
        docs = str(self.docs).replace("[", "").replace("]", "")
        base = "Conforme a documentacao anexa ({}), a parte re registrou divida inexistente " \
        "da autora no valor o montate de R$ {}, nas empresas de score de credito, a titulo de {}. " \
        "Ocorre que as referidas dividas nao existem".format(docs, self.value, self.suposta_divida)
        t1 = "A parte autora ainda ressalta nao ser devedor contumaz, de forma que o registro indevido " \
        "do nome nas empresas de score de credito caracteriza dano moral."
        self.fact.append(base)
        self.fact.append(t1)
        
    def set_law(self):
        base = "De acordo com o Art XXX do CDC/CC, quando houver registro indevido de divida " \
        "em empresas de score de credito, o consumidor tem direito a retirada do nome do registro" \
        "e compensacao pelo dano moral a sua imagem. " \
        "Esse entendimento foi validado em jurisprudencia XXXX"
        self.law.append(base)
        
    def set_requests(self):
        base = "A imediata retirada da anotacao nas empresas de Score de credito da alegada divida" \
        "indevidamente cobrada pela parte re"
        base.format(str(self.value * 2))
        self.request.append(base)


class CobrancaContaPaga(Request):
    def __init__(self, divida_cobrada, valor, docs, dano_moral=1000):
        super(CobrancaContaPaga, self).__init__()
        self.layer_type = "Cobranca indevida"
        self.value = valor * 2 + dano_moral
        self.divida_cobrada = divida_cobrada
        self.dano_moral = dano_moral
        self.docs = docs
        self.set_texts()
    
    def set_texts(self):
        self.set_facts()
        self.set_law()
        self.set_requests()
    
    def set_facts(self):
        docs = str(self.docs).replace("[", "").replace("]", "")
        base = "Conforme a documentacao anexa {}, a parte re cobrou indevidamente " \
        "da autora valores que perfazezm o montate de R$ {}, a titulo de {}. " \
        "Ocorre que, como provam os documentos anexos, a conta ja foi paga."
        t1 = "Essa cobranca em duplicidade causou grande aborrecimento a parte autora, " \
        "que teve que perder tempo em provar que pagou tudo e ainda ajuizar acao judicial, de forma " \
        "que essa situacao lhe causou dano moral."
        base = base.format(docs, self.value, self.divida_cobrada)
        self.fact.append(base)
        
    def set_law(self):
        base = "De acordo com o Art XXX do CDC, quando houver cobranca indevida, o consumidor tem direito" \
        "a repeticao do indebito em dobro, que foi validado em jurisprudencia XXXX."
        t1 = "A lei CDC/CC art XXX e jurisprudencia XXXX tambem reconhecem a existencia de dano moral" \
        "nessa situacao de cobranca de divida paga" \
        ", de forma que resta necessaria compensacao por parte da parte re pelo " \
        "moral causado a autora."
        self.law.append(base)
        self.law.append(t1)
        
    def set_requests(self):
        base = "A repeticao do indebito da conta indevidamente cobrada pela segunda vez"\
        " em dobro, de acordo com o exposto e no valor de R$ {}"
        base = base.format(str(self.value * 2))
        self.request.append(base)

class DanoMoral(Request):
    def __init__(self, dano_moral):
        self.priority = -1
        super(DanoMoral, self).__init__()
        self.value = dano_moral
        self.dano_moral += dano_moral
        self.layer_type = "Dano moral puro"