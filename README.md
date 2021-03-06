# Slingshot
Slingshot is a Python library bringed on by **A Mosca** team for creating reproducible procedural documents for Brazilian law-suits. It was created during the development of **A Mosca** web application in order to democratize access to justice in Brazil, but as the code became more complex, we set the project apart and started to develop both independently. 

## Installation

```
pip install slingshot-lawdocs
```

## Run an example
It will generate a simple clim (Petição) in your dir, using our lib.
```
python -m slingshot.procedural_document.examples.simple_claim
```

## Objective
Bringing to the community of law and technology students a open-source quality tool for creating procedural documents without having to lay on expensive and proprietary solutions bringed on by lawtechs for law suits. 

## Why should you use Slingshot
Slingshot creates procedural documents by chaining content blocks (Layers) in a way that is very alike to Keras high level Deep Learning framework, and let law-academic learn programming in a useful, rich and difunded language, Python. 

Also, not only it is very easy to learn (as Python itseld), but part the knowledge adquired on learning how to use it can be leveraged to use in other coding tasks, as Data Science activities, web-crawling and even web-development.

## Knowledge requirements
 * Python syntax
 * String manipulations
 * Python OOP basics (we already did the hard part for you)
 
 ## System requirements
  * Python >= 3.7
  * python-markdown
  * pandoc
  * pdfkit
  
 ## Slingshot basics
 Slingshot documents are built by chaineble-content blocks, **ContentLayer** class objects that are wrapped by **ProceduralDocument** class objects. Once all the content blocks are added and chained to the **ProceduralDocument**, it has built-in methods that generates and formats it in both **pdf**, **docx** and **html** format. 
 
 There are two main tasks that can be performed with Slingshot:
  * Creating new content block Layers
  * Elaborating procedural Documents by chaining content block Layers.
  
  ### ProceduralDocument
  This class consists of a wrapper with some text lists referring to the "facts", "law" and "requests" part of the ProceduralDocument, aside from the "parts" and some "preliminars". When the ProceduralDocument is compilied, it gathers from the ContentLayer its info and puts it into the right place, so the text can be fully generated and formatted.
  
  ### Example on creating a procedural document with layers
  
   
```python
# Here we import the used layers, parts and the core document
from slingshot.procedural_document.layers.models import ContratoServicos, InversaoOnusProva, PropagandaEnganosa
from slingshot.procedural_document.layers.models import CobrancaIndevida, ImpossivelCancelar, DanoMoral, RegistroSerasa
from slingshot.procedural_document.layers.parts import Author, Claro_SP_re
from slingshot.procedural_document.core import ProceduralDocument
```

```python
# We first have to instance the document
pet = ProceduralDocument()
```


```python
# We then add the layers chaining them to the document - alike to Keras
pet.add(Author(name="Equipe A Mosca"
               profession="nerds revoltados com computadores"
               address="Rua da Nossa Casinha 1000, casa 8",
               cpf="123.456.789-00"))

pet.add(ContratoServicos(service="adesão a plano de celular",
                        docs = ["contas pagas"]))

pet.add(Claro_SP_re)

pet.add(InversaoOnusProva())

pet.add(PropagandaEnganosa(prometido="plano de internet sem corte de dados",
                          real="plano de celular com corte de dados ao fim da franquia",
                          valor=1000,
                          docs="fotos e panfletos da operadora",
                          dano_ocorrido="usar o GPS na volta do trabalho, para não se atrasar para buscar o amigo",
                          deseja_prometido=True))

pet.add(CobrancaIndevida(tarifas_cobradas=["Dados a mais"],
                         valor=2000,
                         docs=["contas"]))

pet.add(RegistroSerasa(divida_registrada="Conta do celular (11) - 99999-8888",
                       valor=2000,
                        docs=["Conta do mês de setembro"]))

pet.add(ImpossivelCancelar(dano_moral=3000,
                           docs=["Pedido de cancelamento e email"]))

pet.add(DanoMoral(2000))
```

```python
# We then compile our document. Our engine distributes all the facts, law and requests on their specific fields to generate the document
# Here you just fill holes with the right info
pet.compile()
```

```python
# You can seek the summary if you want - very alike to Keras model
# See what it prints:
pet.summary()
```

```
Ação condenatória com base no CDC
#############
CAMADAS DA PETICAO:
Autor
Parte Re
Contexto - Prestação de serviços
Preliminar - Inversao ônus da prova
Propaganda enganosa
Cobranca indevida
Registro indevido no Serasa
Impossivel cancelar plano
Dano moral puro
#############
Valor da causa: R$ 12000
```

```python
# with this line, it generates your pdf, docx and html document
a = pet.save_document(path='my_procedural_document',
                      to_pdf=True,
                      to_word=True)
```

### Coding a simple ContentLayer for request

We will inherit from its parent class and decide the content and the holes to be filled with content. When handled by our wrapper, everything goes to its proper part and the ProceduralDocument text is generated.
```python

#see that it inherits from Request class. It has some aside features, as
#the layer name that appears on the summary,
#the value of hte request,
#the document that prove the allegations,
#the holes that are filled to give sense to the layer.


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
        base = "Conforme a documentação anexa ({}), a parte re registrou divida inexistente " \
        "da autora no valor o montate de R$ {}, nas empresas de score de crédito, a título de {}. " \
        "Ocorre que as referidas supostas dívidas nao existem e não justificam o cadastro nos bancos de score de crédito.".format(docs, self.value, self.suposta_divida)
        t1 = "A parte autora ainda ressalta não ser devedor contumaz, de forma que o registro indevido " \
        "do nome nas empresas de score de credito caracteriza dano moral."
        self.fact.append(base)
        self.fact.append(t1)
        
    def set_law(self):
        base = "De acordo com o Art 42, caput do CDC/CC, o consumidor não será exposto a ridículo quando da cobrança de dívidas. (*Art. 42. Na cobrança de débitos, o consumidor inadimplente não será exposto a ridículo, nem será submetido a qualquer tipo de constrangimento ou ameaça.*)"
        t1 = "Ocorre que, neste caso, isso aconteceu, tendo em vista que a inserção de seu nome indevidamente no cadastro de devedores " \
        "o expõe ao ridículo e abala a sua imagem, além de impedir que adquira crédito no mercado. Por isso, deve haver remoção imediata de seu nome dos respectivos cadastros "\
        "e compensacao pelo dano moral e à sua imagem. "
        t2 = "Esse entendimento foi validado em jurisprudencia, que, inclusive, reconhece a existência de dano moral "\
            "para esse tipo de caso de inclusão indevida no cadastro de devedores do Serasa:\n\n"\
            """ * PRESTAÇÃO DE SERVIÇOS DE TELEFONIA AÇÃO DE CANCELAMENTO DE COBRANÇA INDEVIDA E DE REGISTRO INDEVIDO JUNTO AO SERASA/SPCC/C REPARAÇÃO DE DANOS MORAIS COM PEDIDO DE TUTELA ANTECIPADA INEXIGIBILIDADE DOS DÉBITOS SERVIÇO CONTRATADO FUNCIONAMENTO NÃO COMPROVADO PESSOA JURÍDICA NEGATIVAÇÃO INDEVIDA DO NOME DA AUTORA EM ÓRGÃOS DE PROTEÇÃO AO CRÉDITO DANO MORALCARACTERIZADO SENTENÇA QUE ARBITROU QUANTIA EM CONFORMIDADE COMOS CRITÉRIOS DE PROPORCIONALIDADE E RAZOABILIDADE INDENIZAÇÃO DEVIDA FIXADA EM R$ 10.000,00 VALOR MANTIDO SENTENÇA MANTIDA. *TJSP- Apelação cível AC :  0058685-32.2012.8.26.0114 publicado em 24/01/2017*"""
        self.law.append(base)
        self.law.append(t1)
        self.law.append(t2)
```
  ## Contributing
  If you want to help us, pull request on models (or whatever built-in models archives there are when you want to do it) file new layer you make. With that, you help democratizing the access to justice in Brazil. Also, if you add new features, we are looking forward to see it.
  
  ## DISCLAIMER
  Slingshot is free to use, you can do whatever you want with it, just remember to cite "A Mosca" as the organization behind it. Also, we are not responsable for what you do with the code we've made.
  
