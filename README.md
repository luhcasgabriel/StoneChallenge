
<h1 align="center">Desafio Stone</h1>

<p align="center">🚀 Desenvolvimento de uma função que tenha como parâmetro de entrada duas listas, uma lista de produtos e uma lista de emails, e que o retorno dessa função seja um map/dicionario com o valor dividido entre os usuários da lista email do total de itens da lista de produtos</p>

<h1 align="center">
    <a href="https://pt-br.reactjs.org/">🔗 Python</a>
</h1>




## Sumário 


   * [Instalação](#Instalação)
   * [Pré requisitos](#Pré-requisitos)
   * [Execução](#Execução)
   * [Descrição da solução](#Descrição-da-solução)
   * [Testes](#Plano-de-testes)
      * [Testes lista de emails](#Testes-lista-de-emails)
      * [Cenário 1 - Lista vazia](#Testes-lista-de-emails)
      * [Cenário 2 - Email sem '@' e '.com'](#Testes-lista-de-emails)
      * [Cenário 3 - Email vazio](#Testes-lista-de-emails)
      * [Cenário 4 - Lista com itens inválidos](#Testes-lista-de-emails)
      * [Cenário 5 - Email duplicado](#Testes-lista-de-emails)
   * [Testes lista de produtos](#Testes-lista-de-produtos)
      * [Cenário 6 - Lista vazia](#Testes-lista-de-produtos)
      * [Cenário 7 - Tipo de item da lista incorreto](#Testes-lista-de-produtos)
      * [Cenário 8 - Tipo de atributo do objeto Product() incorreto](#Testes-lista-de-produtos)
<!--te-->



## Instalação

Baixe o arquivo .zip e descompacte ele, dentro da pasta há um arquivo com as funções. 

É necessário que se tenha uma versão de python, preferenciamente a mais atual para executar o arquivo.


É possível fazer o clone dele também no meu github pessoal 

    https://github.com/luhcasgabriel/StoneChallenge


## Pré requisitos 

É necessário que se tenha uma versão de python, preferenciamente a mais atual para executar o arquivo. 

## Execução

O arquivo pode ser executado por linha de comando, através da linha de comando abra a pasta descompactada. 
```bash
cd ./DesafioStone
```
E execute o arquivo stone_challenge.py. Obs. verifique qual sistema operacional é o seu e qual nomenclatura  utilizar para executar um arquivo python.
  
Windows
```bash
python stone_challenge.py
```

Exemplo de outras distribuições 
```bash
python3 stone_challenge.py
```

## Descrição da solução

Foi realizada uma solução para o teste da Stone, que desafiava o candidado a criar uma função com dois parâmetros de entrada (umas lista de emails e uma lista de produtos(itens)) e que retornasse um map/dicionário com a lista de usuários com email e o valor que cada um pagaria pela divisão do total dos itens do carrinho. Foi proposta a seguinte solução :

Criação de um objeto para produtos, com um construtor e com os seguintes atributos: 

```python
# class products
class Product:
    
    def __init__(self, item='', amount=0, price=0):
        self.item = item     # descrição do produto
        self.amount = amount # quantidade de itens
        self.price = price   # preço do item
```

Lista de produtos, e seus itens são uma instância da classe produtos:
```python
# products list   
produts_list = [
    Product( 'leite', 2, 319 ) ,
    Product( 'macarrão', 5, 220 ) ,
    Product( 'batata', 5, 500 ) ,
    Product( 'queijo', 1, 670 ) ,
    Product( 'mortandela', 1, 780 ) ,
    Product( 'pão', 5, 280 ) 
]
```

Lista de emails do usuário:
```python
# emails list
emails_list = [
    'thomasShelby@gmail.com',
    'bijornIronSide@gmail.com',
    'god@gmail.com',
    'barneyStinson@gmail.com',
    'harryPotter@gmail.com',
    'daenerysTargaryen@gmail.com',
    'reiDaNoite.@gmail',
]
```

Função pai que checa os dados de entrada, chama duas funções que checam as duas listas e retornam uma mensagem caso tenha algo incorreto:
```python
# method that checks whether the lists are correct
def checkData(emails_list, produts_list):
```

Função filha que checa os dados de entrada da lista de emails e retornam uma mensagem caso tenha algo incorreto:
```python
# method that checks if the email list is correct
def checkEmails(emails_list):
```

Função filha que checa os dados de entrada da lista de produtos e retornam uma mensagem caso tenha algo incorreto:
```python
# method that checks if the product list is correct
def checkProducts(produts_list):
```

Função principal que calcula o valor de cada itegrante da lista de emails irá pagar e retorna um dicionário caso esteja tudo ok, ou retorna uma mensagem de erro caso tenha dados incorretos:
```python
# function to return dictionary with emails and agreed payment amount
def dicionaryEmailsList(emails_list, produts_list):
```

No final do arquivo há uma chamada do método principal (dicionaryEmailsList) com um print de saída do retorno.
```python
# print method return
print(dicionaryEmailsList(emails_list, produts_list))
```


_____________________
<h1 align="center">Testes</h1>

Para testar os arquivos é necessário alterar as duas listas diretamente no arquivo e verificar o resultado:



## Plano de testes
<!--ts-->
   * [Testes lista de emails](#Testes-lista-de-emails)
      * [Cenário 1 - Lista vazia](#Testes-lista-de-emails)
      * [Cenário 2 - Email sem '@' e '.com'](#Testes-lista-de-emails)
      * [Cenário 3 - Email vazio](#Testes-lista-de-emails)
      * [Cenário 4 - Lista com itens inválidos](#Testes-lista-de-emails)
      * [Cenário 5 - Email duplicado](#Testes-lista-de-emails)
   * [Testes lista de produtos](#Testes-lista-de-produtos)
      * [Cenário 6 - Lista vazia](#Testes-lista-de-produtos)
      * [Cenário 7 - Tipo de item da lista incorreto](#Testes-lista-de-produtos)
      * [Cenário 8 - Tipo de atributo do objeto Product() incorreto](#Testes-lista-de-produtos)



   

# Testes lista de emails




<h2 align="center">Cenário 1 - Lista vazia</h1>


Altere a lista atual (linha 20) para uma lista vazia
```python
emails_list = []
```
Resultado:
```bash
Empty emails list 
```
------------------
<h2 align="center">Cenário 2 - Email sem '@' e '.com'</h1>


Altere a lista de emails atual (linha 20) e retire o '@' ou '.com'
```python
emails_list = [
    'thomasShelbygmail.com',
    'thomasShelbygmail@',
]
```
Resultado:
```bash
Invalid email
```
<h2 align="center">Cenário 3 - Email vazio</h1>


Altere a lista de emails atual (linha 20) e adicione um email vazio com item da lista ('')
```python
emails_list = [
    '',
]
```
Resultado:
```bash
Invalid email
```

<h2 align="center">Cenário 4 - Lista com itens inválidos</h1>


Altere a lista de emails atual (linha 20) e adicione item diferente do tipo texto(str)
```python
emails_list = [
    0,
    'lucas@gmail.com'
]
```
Resultado:
```bash
one of the emails is invalid
```

<h2 align="center">Cenário 5 - Email duplicado</h1>


Altere a lista de emails atual (linha 20) e adicione um email já existente
```python
emails_list = [
    'lucas@gmail.com',
    'lucas@gmail.com'
]
```
Resultado:
```bash
duplicate emails in the email list, please check
```


# Testes lista de produtos


<h2 align="center">Cenário 6 - Lista vazia</h1>


Altere a lista de produtos atual (linha 10) para uma lista vazia


```python
produts_list = []
```
Resultado:
```bash
Empty product list
```

<h2 align="center">Cenário 7 - Tipo de item da lista incorreto</h1>


Altere a lista de produtos atual (linha 10) e adicione um item diferente do tipo Product()


```python
produts_list = [
    '' ,
    0 ,
    Product( 'batata', 5, 500 ) ,
    Product( 'queijo', 1, 670 ) ,
    Product( 'mortandela', 1, 780 ) ,
    Product( 'pão', 5, 280 ) 
]
```
Resultado:
```bash
one of the list items is not a valid data type
```

<h2 align="center">Cenário 8 - Tipo de atributo do objeto Product() incorreto</h1>


Altere a lista de produtos atual (linha 10) e adicione um atributo diferente do esperado para a classe Product()


```python
produts_list = [
    Product( 0, 5, 500 ) ,           # sequência correta de tipagem dos atributos (TEXTO,INTEIRO,INTEIRO)
    Product( 'queijo', '', 670 ) ,   # sequência correta de tipagem dos atributos (TEXTO,INTEIRO,INTEIRO)
    Product( 'mortandela', 1, '') ,  # sequência correta de tipagem dos atributos (TEXTO,INTEIRO,INTEIRO)
    Product( 'pão', 5, 280 )         # sequência correta de tipagem dos atributos (TEXTO,INTEIRO,INTEIRO)
]
```
Resultado:
```bash
the price of one of the items in the product list is incorrect, please enter a whole number
```
```bash
the name of one of the items in the product list is incorrect or empty, please enter a text value
```
```bash
the quantity of one of the items in the product list is incorrect, please enter a whole number
```