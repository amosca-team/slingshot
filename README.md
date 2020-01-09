# Slingshot
Slingshot is a Python library bringed on by **A Mosca** team for creating reproducible procedural documents for Brazilian law-suits. It was created during the development of **A Mosca** web application in order to democratize access to justice in Brazil, but as the code became more complex, we set the project apart and started to develop both independently. 

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
 Slingshot documents are built by chaineble-content blocks, **Layer** class objects that are wrapped by **Document** class objects. Once all the content blocks are added and chained to the **Document**, it has built-in methods that generates and formats it in both **pdf**, **docx** and **html** format. 
 
 There are two main tasks that can be performed with Slingshot:
  * Creating new content block Layers
  * Elaborating procedural Documents by chaining content block Layers.
  
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


  ## DISCLAIMER
  Slingshot is free to use, you can do whatever you want with it, just remember to cite "A Mosca" as the organization behind it. Also, we are not responsable for what you do with the code we've made.
  
