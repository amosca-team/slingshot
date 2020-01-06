"""
On this module we show some example implementations of the petition layers implementation
With these layers, you can create a petition to sue a Telecom corporation for some damage they brought you
"""


from .base import *

class ContratoServicos(Context):
    def __init__(self, service, docs):
        super(ContratoServicos, self).__init__()
        self.layer_type = "Contexto - Prestacao de servicos"
        self.pet_type = "Acao condenatoria com base no CDC"
        self.service = service
        self.docs = docs
        self.priority = 10000000
        self.set_text()
        
    def set_text(self):
        self.set_fact()
        
    def set_fact(self):
        docs = str(self.docs).replace("[", "").replace("]", "")
        base = "Conforme da documentacao anexa ({}) parte autora firmou com a parte requerida " \
        "contrato de prestacao de servicos, mais especificamente por meio de {}. Ocorre que, durante " \
        "a execucao do contrato, a re teve uma serie de condutas que passaram a prejudicar a autora."
        base = base.format(docs, self.service)
        t1 = "Ainda conforme a documentacao, a parte autora tentou de todos os meios amigaveis possiveis" \
        "para a solucao dos problemas que seguem, tornando esta acao a unica solucao possivel."
        self.fact.append(base)
        self.fact.append(t1)

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
        "e do art 6o, inciso VIII do CDC e, faz-se necessaria" \
        "inversao do onus da prova em favor da parte autora neste processo."
        base = base + "\n" \
        + """* *Art. 6°. São direitos básicos do consumidor:* \n* *(...) VIII – a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, no processo civil, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiências (...).*"""


        self.preliminary_request.append(base)
        
    def set_request(self):
        base = "Seja deferida a inversao do onus da prova em favor da parte autora."
        self.request.append(base)

class CobrancaIndevida(Request):
    def __init__(self, tarifas_cobradas, valor, docs, conta_paga=False):
        super(CobrancaIndevida, self).__init__()
        self.layer_type = "Cobranca indevida"
        self.valor_cobrado = valor
        self.value = 2 * valor
        self.tarifas = tarifas_cobradas
        self.conta_paga = conta_paga
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
        " de corresponderem a {}".format(docs, self.valor_cobrado, self.tarifas)
        if self.conta_paga:
            base = base + ", cobrando inclusive valores que já foram pagos, como provam os anexos."
        else:
            base = base + "."
        t1 = "A parte autora ressalta que jamais anuiu com a cobranca indevida desses valores, seja como prestacao de servicos adicionais" \
        ", reajuste no plano ou qualquer outro tipo de cobranca, de maneira que resta ilicita e incorreta a referida cobranca de valores."
        self.fact.append(base)
        self.fact.append(t1)
        
    def set_law(self):
        base = "De acordo com o Art 42, Parágrafo Único, do CDC, quando houver cobranca indevida, o consumidor tem direito " \
        "a repeticao do indebito em dobro (*Parágrafo único. O consumidor cobrado em quantia indevida tem direito à repetição do indébito, por valor igual ao dobro do que pagou em excesso, acrescido de correção monetária e juros legais, salvo hipótese de engano justificável.*)"
        t1 = "O mesmo ainda é encontra base na jurisprudência, que reconhece, inclusive, a exitência de dano moral em caso de cobrança indevida - inclusive por causa da ocorrência de desvio produtivo do consumidor:" \
            "\n * PRESTAÇÃO DE SERVIÇOS INEXISTENTE - COBRANÇA INDEVIDA - RESTITUIÇÃO EM DOBRO E COMPENSAÇÃO" \
            "POR DANO MORAL – RECONHECIMENTO – FIXAÇÃO EM R$ 7.000,00 - PRETENSÃO DA AUTORA EM" \
            "MAJORAÇÃO – IMPERTINÊNCIA - RECURSO NÃO PROVIDO. - *Tribunal de Justiça de São Paulo TJ-SP - Apelação Cível : AC" \
            "1000854-52.2018.8.26.0161*"
        self.law.append(base)
        self.law.append(t1)
        
    def set_requests(self):
        base = "A repeticao do indebito em dobro, de acordo com o exposto e no valor de R$ {}."
        base = base.format(str(self.value))
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
        "no Codigo Civil art 186, 188 e 187, o mesmo, para esse tipo de caso do consumidor, encontra respaldo no" \
        "art 14, caput do CDC (*Art. 14. O fornecedor de serviços responde, independentemente da existência de culpa, pela reparação dos danos causados aos consumidores por defeitos relativos à prestação dos serviços, bem como por informações insuficientes ou inadequadas sobre sua fruição e riscos.*)"
        t1 = "Existe ainda respaldo jurisprudencial no sentido de entender a gravidade e a necessidade de " \
        "ressarcimento deste tipo de dano, inclusive por causa do desvio produtivo do consumidor, como ja foi reconhecido pelo STJ:"\
        """\n* PROCESSO CIVIL E DIREITO DO CONSUMIDOR. RECURSO ESPECIAL. AÇÃO CIVIL PÚBLICA. NEGATIVA DE PRESTAÇÃO JURISDICIONAL. AUSÊNCIA. JUNTADA DE DOCUMENTOS COM A APELAÇÃO. POSSIBILIDADE. VÍCIO DO PRODUTO. REPARAÇÃO EM 30 DIAS. RESPONSABILIDADE OBJETIVA DO COMERCIANTE.1. Ação civil pública ajuizada em 07/01/2013, de que foi extraído o presente recurso especial, interposto em 08/06/2015 e concluso ao Gabinete em 25/08/2016. Julgamento pelo CPC/73.2. Cinge-se a controvérsia a decidir sobre: (i) a negativa de prestação jurisdicional (art. 535, II, do CPC/73); (ii) a preclusão operada quanto à produção de prova (arts. 462 e 517 do CPC/73); (iii) a responsabilidade do comerciante no que tange à disponibilização e prestação de serviço de assistência técnica (art. 18, caput e § 1º, do CDC).3. Devidamente analisadas e discutidas as questões de mérito, e fundamentado o acórdão recorrido, de modo a esgotar a prestação jurisdicional, não há que se falar em violação do art. 535, II, do CPC/73.4. Esta Corte admite a juntada de documentos, que não apenas os produzidos após a inicial e a contestação, inclusive na via recursal, desde que observado o contraditório e ausente a má-fé. **5. À frustração do consumidor de adquirir o bem com vício, não é razoável que se acrescente o desgaste para tentar resolver o problema ao qual ele não deu causa, o que, por certo, pode ser evitado – ou, ao menos, atenuado – se o próprio comerciante participar ativamente do processo de reparo, intermediando a relação entre consumidor e fabricante, inclusive porque, juntamente com este, tem o dever legal de garantir a adequação do produto oferecido ao consumo. 6. À luz do princípio da boa-fé objetiva, se a inserção no mercado do produto com vício traz em si, inevitavelmente, um gasto adicional para a cadeia de consumo, esse gasto deve ser tido como ínsito ao risco da atividade, e não pode, em nenhuma hipótese, ser suportado pelo consumidor. Incidência dos princípios que regem a política nacional das relações de consumo, em especial o da vulnerabilidade do consumidor (art. 4º, I, do CDC) e o da garantia de adequação, a cargo do fornecedor (art. 4º, V, do CDC), e observância do direito do consumidor de receber a efetiva reparação de danos patrimoniais sofridos por ele (art. 6º, VI, do CDC).** 7. Como a defesa do consumidor foi erigida a princípio geral da atividade econômica pelo art. 170, V, da Constituição Federal, é ele – consumidor – quem deve escolher a alternativa que lhe parece menos onerosa ou embaraçosa para exercer seu direito de ter sanado o vício em 30 dias – levar o produto ao comerciante, à assistência técnica ou diretamente ao fabricante –, não cabendo ao fornecedor impor-lhe a opção que mais convém. 8. Recurso especial desprovido. *RESP - 1634851, Rel. Min. Nancy Andrighi*"""
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
        base = "De acordo com o Art 42, caput do CDC/CC, o consumidor não será exposto a ridículo quando da cobrança de dívidas. (*Art. 42. Na cobrança de débitos, o consumidor inadimplente não será exposto a ridículo, nem será submetido a qualquer tipo de constrangimento ou ameaça.*)"
        t1 = "Ocorre que, neste caso, isso aconteceu, tendo em vista que a inserção de seu nome indevidamente no cadastro de devedores " \
        "o expõe ao ridículo e abala a sua imagem, além de impedir que adquira crédito no mercado. Por isso, deve haver remoção imediata de seu nome dos respectivos cadastros "\
        "e compensacao pelo dano moral e à sua imagem. "
        t2 = "Esse entendimento foi validado em jurisprudencia, que, inclusive, reconhece a existência de dano moral "\
            "para esse tipo de caso de inclusão indevida no cadastro de devedores do Serasa:\n"\
            """ * PRESTAÇÃO DE SERVIÇOS DE TELEFONIA AÇÃO DE CANCELAMENTO DE COBRANÇA INDEVIDA E DE REGISTRO INDEVIDO JUNTO AO SERASA/SPCC/C REPARAÇÃO DE DANOS MORAIS COM PEDIDO DE TUTELA ANTECIPADA INEXIGIBILIDADE DOS DÉBITOS SERVIÇO CONTRATADO FUNCIONAMENTO NÃO COMPROVADO PESSOA JURÍDICA NEGATIVAÇÃO INDEVIDA DO NOME DA AUTORA EM ÓRGÃOS DE PROTEÇÃO AO CRÉDITO DANO MORALCARACTERIZADO SENTENÇA QUE ARBITROU QUANTIA EM CONFORMIDADE COMOS CRITÉRIOS DE PROPORCIONALIDADE E RAZOABILIDADE INDENIZAÇÃO DEVIDA FIXADA EM R$ 10.000,00 VALOR MANTIDO SENTENÇA MANTIDA. *TJSP- Apelação cível AC :  0058685-32.2012.8.26.0114 publicado em 24/01/2017*"""
        self.law.append(base)
        self.law.append(t1)
        self.law.append(t2)
        
    def set_requests(self):
        base = "A imediata retirada da anotacao nas empresas de Score de credito da alegada divida" \
        "indevidamente cobrada pela parte re"
        base.format(str(self.value * 2))
        self.request.append(base)



class DanoMoral(Request):
    def __init__(self, dano_moral):
        self.priority = -1
        super(DanoMoral, self).__init__()
        self.value = dano_moral
        self.dano_moral += dano_moral
        self.layer_type = "Dano moral puro"