Autor: Eduardo Brancher Urenha
Para executar o programa, basta fazer py py2.py no terminal. O programa fornecerá as instruções e
comandos implementados. Por enquanto é apenas possível testar se uma certa lista de itens (escrita
em um .txt externo) cabe na lista de veículos também descrita em um .txt externo. O formato dessas
listas está discutido na seção 2 (ver índice abaixo).


O problema pedido é uma versão do problema da mochila booleana generalizado para várias dimensões.
Esse problema é NP-difícil e não existe(por enquanto?) um algoritmo polinomial que resolva todos os casos. 
Assim sendo, escolhemos fazer uma heurística polinomial que fornece uma estimativa de empacotamento
conservadora. Explicaremos a ideia do algoritmo e os arquivos envolvidos na execução do programa nas
seções e subseções abaixo.

Índice
Sessão 1. Ideia do algoritmo
       1.1 Vantagens e desvantagens
Sessão 2. Arquivos
       2.1 Listas de itens
       2.2 Listas de veículos
Sessão 3. A fazer

=======================
1. Ideia do algoritmo
=======================

A ideia da nossa heuristica consiste em primeiramente checar se o peso total dos itens cabe na mochila.
Com esse detalhe fora do caminho, prosseguimos ao empacotamento propriamente dito, que é o verdadeiro desafio.
Para isso, escolhemos o item de maior volume e o colocamos em um dos cantos da mochila. Esse processo define 3
volumes paralelepipedais secundários, que são formados pelos espaços entre o item colocado e as paredes da 
mochila (diagrama abaixo):

------------------
|        |       |
|        |       |
|  Item  |   1   |
|        |       |
|________|______ |
|        |       |
|    2   |   3   |
------------------

Em que a altura dos 3 espaços secundarios corresponde à altura do Item. Então, percorremos a lista de itens 
(que foi ordenada por volume) e tentamos colocar o maior item possível em cada um dos espaços secundários. 
Uma vez tenhamos colocado 3 itens ou, conversamente, percorrido todos os itens, o volume livre remanescente na 
mochila é atualizado removendo o nível que acabamos de preencher do volume total e o processo é repetido, até 
que todos os itens tenham sido colocados ou que algum item não caiba.

----------------------------
1.1 Vantagens e desvantagens
----------------------------

O algoritmo descrito acima é conservador, no sentido de que ele deixa espaços vazios no empacotamento dele: 
A cada espaço secundário, colocamos um item que é um "best-fit", mas que não é um fit perfeito: De modo que o
conjunto de itens que cabe em um veículo quase certamente desperdiçará espaço. Além disso, outro problema é 
que o algoritmo não faz nenhum tipo de checagem sobre o peso dos itens durante o empacotamento; isso pode
fazer com que itens pesados fiquem em cima de itens leves, o que é potencialmente perigoso para a carga.
Felizmente isso pode ser resolvido facilmente adicionando um critério de fragilidade e ordenando os itens
de acordo com esse critério primeiro.

O método possui suas vantagens também, porém. O fato de ser conservador significa que ele nunca retorna um
resultado "falso-positivo": Ele nunca diz que uma carga caberia em um veículo e ela na realidade não cabe.
Esse seria o pior tipo de erro a ser cometido pelo algoritmo, pois causaria disrupção significativa no processo
de empacotamento: Um conjunto de itens potencialmente teria que ser enviado de volta ao estoque e reavaliado,
criando uma perturbação logística. Além disso, se o algoritmo diz que um conjunto de itens cabe no veículo,
sabemos também que o algoritmo construiu um empacotamento facil e intuitivo: 4 itens por nivel, subindo em 
sequencia. O algoritmo portanto pode ser facilmente adaptado para criar uma instrução visual sobre como os
itens devem ser empacotados no veículo, auxiliando o trabalho. Finalmente, embora isto não seja uma garantia,
os itens maiores tenderão a ficar nos níveis mais baixos, gerando uma facilidade de empacotamento nesse 
sentido também.

=================
2. Arquivos
=================
Para que o programa funcione, devem existir no diretório listas de itens que serão acessadas quando o usuário
digitar os comandos relevantes, e uma lista de veículos, que devem ser codificadas nos formatos abaixo.

--------------------
2.1 Listas de Itens
--------------------

Segue um exemplo de lista de itens. Os números são, respectivamente, o peso, largura, espessura e altura.

1 5 5 5
1 1 2 3
3 1 1 5
2 1 1 1
2 4 5 6
1 10 10 10
5 15 10 15

A lista deve terminar no último número. Não deve haver nenhuma linha abaixo da ultima linha de dados.

---------------------
2.2 Lista de veículos
---------------------

O programa também requer uma(e apenas uma!) lista de veículos no formato abaixo. 
Os números são, respectivamente, a largura, altura, espessura e peso máximos. Abaixo segue um exemplo:

Lala Moto 35 40 30 20
Lala Fiorino 188 133 108 500
Lala Carreto 300 180 200 1500
Ogi Moto 52 36 52 20
Ogi SUV 125 80 60 200

A lista deve terminar no último número. Não deve haver nenhuma linha abaixo da ultima linha de dados.
Os dois arquivos exemplo estão disponíveis no .git do problema.

=====================
3. A fazer
=====================

Nessa seção detalhamos as próximas tarefas que gostaríamos de executar:

1. Criar uma função que permita ao usuário atualizar a lista de veículos "de dentro" do programa.
O programa perguntaria as especificações e alteraria a lista correspondente, ou removeria um veículo dela.

2. Criar uma função que permita ao usuário gerar uma lista nova de itens "de dentro" do programa.
O programa perguntaria as especificações de cada item e geraria uma lista correspondente. 

As vantagens de ter esses métodos dentro do programa é que o usuário não precisa se preocupar com a sintaxe da 
lista.

3. Testar mais. Gerar um módulo automatizado de experimentos que testa um conjunto de dados salvo na pasta do
programa toda vez que é chamado. Estabelecer métricas (por exemplo, ocupação parcial do volume, ocupação 
parcial do peso, entre outras)

4. Implementar o critério de fragilidade.
