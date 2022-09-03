# py3-std
<h1>ESTUDO AMPLO</h1>
<br>
<p>Entendendo suas mecânicas e funcionalidades. Envolvendo ideias e projetos criados com o intuito de aprofundar meus conhecimentos sobre a linguagem. 
 Aprendendo também sobre Banco de Dados Relacioanis e Não-Relacioanis. Master Branch</P>
 
<h4>ESTUDOS EM:</h4>
 
```sh

 - PL/SQL
 - MYSQL
 - ORACLE 
 - SQL SERVER

```
 
 <h1>FUNÇÕES</h1>
 <p>JAVA</p>
 
 ```sh

 Representam um processamento que possui um significado
 Math.sqrt(double)
 System.out.println(string)
 Principais vantagens: modularização, delegação e reaproveitamento
 Dados de entrada e saída
 Funções podem receber dados de entrada (parâmetros ou argumentos)
 Funções podem ou não retornar uma saída
 Em orientação a objetos, funções em classes recebem o nome de
 "métodos"

```


 
 > Useful resources for working with [Java](https://docs.oracle.com/en/java/javase/11/)
 >  - [I. Development](#i-development)
    - [1. Common frameworks and libraries](#1-common-frameworks-and-libraries)
    - [2. Web development](#2-web-development)
    - [3. GUI](#3-gui)
    - [4. Business](#4-business)


 
 
<h1>SQL</h1>
Hoje em dia todos os bancos relacionais adotam o padrão SQL. Utilizado para criação, consulta de dados, alteração, manipulação da estrutura do banco de dados. 
A forma como interage com a segurança. 
Algumas vantagens:
- Aprendizado. - Portabilidade (Facilidade em migrar sistemas). - Longevidade (Garantia que funcionarão por muitos anos) 
- Comunicação (Permite que os sistemas se comuniquem entre si). - LIberdade de Escolha. 
<h3>Comandos</h3>

- DDL: Linguagem de definição de Dados. Perimite a manipulação das estruturas dos bancos de dados. Criação de banco, tabela, alterar índice...

- DML: Linguagem de Manipulação de Dados. Tem como objetivo gerenciar os dados. Incluir, alterar e excluir informações. Além de consultas.
 
- DCL: Linguagem de controle de dados. Permite adm o banco de dados, no controle de acesso, gerenciar usuário, a nível de estrutura. 

<h1>MySQL</h1>

- Banco de Dados, possui com entidade principal a Tabela (No momento que é criado uma tabela, já é aplicado certas definições que a mesma terá, ouy seja, dizendo quantos campos ela vai ter e o tipo). Existe um limite máximo de campos, sempre tendo o mesmo tipo. Já registro ou linhas, pode-se ter uma quantidade infinita. 
- View -> Comporta-se como uma tabela, embora já possua uma consulta, agrupando informações e etc. Consultas que podem conter várias tabelas. 
- Procedures -> Programas para manipular dados do banco.
- Trigger -> alerta programada caso aconteça alguma coisa. 
SELECT * FROM CITY (Selecionando todo mundo da tabela city) 
* -> Todo Mundo 
<h1><strong>CREATE DATABASE Syntax</strong></h1>

![syntaxmysql](https://user-images.githubusercontent.com/101754313/182714455-35199b61-36d9-4532-9c29-64f44b2e42a2.png)

`OBS:`Arquivo my.ini é um arquivo de inicialização do mysql. Dentro dele possui uma série de variáveis de ambiente. Inclusive o diretório criado vai para os arquivos. <br>
`OBS:` Para apagar usar o comando DROP {DATABASE | SCHEMA} [IF EXIST] db_name. DELETE usado para dados dentro das columns. 

<h1>STRINGS</h1>
<h4>Atributos dos campos númericos</h4> 
Signed ou Unsigned: vai possuir ou não sinal no número. 
Zerofill - preenche com zeros os espaços.
auto_increment - sequência auto incrementada. (Ex: 1, 2, 3...)
<br>

`OBS:` ERROS DE AUTO OF RANGE vão ocorrer quando os valores estourarem os limites. 
<h4>STRINGS</h4>
CHAR - Cadeia de caracteres com valor fixo (o a 255). <br>
VARCHAR - Cadeia de caracteres com valor variado (de 0 a 255). <br>
(EX: CHAR(4) - "aa" - "  aa" | Ou seja, o que faltar no valor do campo é preenchido com valores vazios.) <br>
(EX: VARCHAR (4) - "aa" - "aa" | Irá armazenar somente os caracteres indicados. Nesse caso apenas 2.) <br<
BINARY - Conceito semelhante dos indicados acima. A dff fica no quesito que não são os caracteres que são gravados, mas sim os bystes. <br>
VARBINARY - Mesma vibe. <br> 
BLOB - Binário longo. [TINYBLOB; BLOB; MEDIUMBLOB; LONGBLOB] <br>
TEXT - Texto longo. [TINYTEXT; TEXT; MEDIUMTEXT; LONGTEXT] <br> 
ENUM - Definidas opções. <br>
SET e COLLATE - Que tipo de conjunto de caracteres serão suportados. <br>

<h4>SPACIAL<h4> 
GEOMETRY; POINT; LINESTRING; POLYGON

<h4>CHEATTT</h4>
 
![mysqlchet](https://user-images.githubusercontent.com/101754313/183474880-e27d8559-ba5b-4cf5-9208-b48868a0109f.png)
 
 More about
 
 ![mysqlcheat2](https://user-images.githubusercontent.com/101754313/183475088-0ea3ed17-5fdf-45ad-86f1-2e396c62bc50.png)
 
 <br> 
 
 - comando para inserir dados: insert
 
 `obs:` DENTRO DE VALUES A ORDEM IMPORTA. SEGUINDO A RESPECTIVA SEQUÊNCIA. 
 <br>
 
 - quando inserir um dado que é uma string deve-se colocar aspas simples. 
 - já no caso de ser um número (float, por exemplo) não precisa colocar aspas. 
 - comando UPDATE altera dados da tabela. UPDATE nome_tabela SET os_campos = 'produto'. Logo em seguida usar WHERE deixando claro qual produto.
 
`obs:` Para modificar sem uso de chave primária -> WORKBENCH PREF - SQL EDITOR - SAFE UPDATES (DESMARCAR CAMPO).
 <br>
 
 - Incluir uma chave primária em uma tabela que já existe: ALTER TABLE (sinaliza que pode alterar uma propriedade de uma tabela que existe).
 - Criar uma nova coluna também pelo ALTER TABLE {NOMETABLE} ADD COLUMN {NOVACOLUNA};
 - Campo lógico e de Data: 0/1 | Data de nasc usa ''. (ex: '1999-08-04')
 
 `BIZU:` EXEMPLO > SELECT CPF, NOME FROM tbcliente LIMIT 5 < 
 <br>
 Indica as colunas p/ visualizar limitando em 5 o número de informações. 
<br>
 SELECT CPF, NOME FROM tbcliente;
 <br> 
 SELECT CPF AS CPF_CLIENTE, NOME AS NOME_CLIENTE FROM tbcliente;
 <br>
 Vale dizer também que a ordem de info não importa. 
 <br>
 SELECT * FROM tbcliente WHERE IDADE > 22 ||| SELECT * FROM tbcliente WHERE < 22 ||| <= / >= / <>(diferente no SQL)
 <br> 
 `BIZU:` Internamente o float é um ponto flutuante, dessa forma não consegue achar exatamente o resultado, utilizando o '=' <br>
 Pode-se achar como por exemplo: SELECT * FROM tbproduto WHERE PRECO_LISTA BETWEEN 16.007 AND 16.009; <br>
 `BIZU:` Porcentagem: 10% = 0.10 / 20% = 0.20 <br>
 SELECT * FROM tbcliente WHERE YEAR(DATA_NASCIMENTO) = 1995; SELECT * FROM tbcliente MONTH(DATA_NASCIMENTO) = 10;
 <br>
 <h4>CONSULTAS CONDICIONAIS</h4>
 X = A OR Y = B (SE UMA FOR VDD A EXPRESSÃO COMPLETA SERÁ)
 <br>
 X = A AND Y = B (SE TODAS AS EXPRESSÕES FOREM VDD A EXPRESSÃO COMPLETA SERÁ)
 <br>
 <h3>DISTINCT</h3>
 
 - Irá retornar somente linhas com valores diferentes.
 `ex:`SELECT DISTINCT * FROM TABELA 
 `ex:`Procurando quais são os bairros da cidade do rj que possuem clientes >>> SELECT DISTINCT BAIRRO FROM TABELA_CLIENTES WHERE CIDADE = 'RIO DE JANEIRO';
 <br>
 LIMIT fica smp no final da linha. (ex: LIMIT 2,3) OU SEJA A PARTIR DO 2 O BANCO PEGA OS PRÓXIMOS 3. 
 <h3>ORDER BY</h3>
 
 - Apresenta o resultado da consulta ordenado pelo campo determinado no ORDER BY. 
 - O comando ordena do menor para o maior. Podendo também determinar a direção da ordenação. DESC (Descendente).
 - Podendo também selecionar 2 campos como critério de selação. ORDER BY campo1, campo2.
 <br<
 <h3>AGRUPAR A RESPOSTA</h3> 
 
 - Juntar campos repetidos, no caso de campos numéricos, quando essa junção é feita, pode-se aplicar uma fórmula matemática (SOMA, MÉDIA, MAX, MIN...)
 - SELECT <campos> FROM TAB GROUP BY CAMPO
 - Apresenta o result agrupando valores numéricos por uma chave de critério. 
 `ex:`Queremos agrupar pelo campo x e somar os valores em y. dessa forma, SELECT X SUM(Y) FROM TAB GROUP BY X.
 `BIZU` SUM: SOMA || MAX || MIN || AVG: MÉDIA || COUNT: CONTA OCORRÊNCIAS, CONTA NÚMERO DE LINHAS 
 <br>
 <h3>HAVING</h3> 
 
 - É um filtro, mas se aplica não sobre o SELECT mas sobre o result de um SELECT que é agrupado. 
 - SELECT X, SUM(Y) FROM TAB GROUP BY X HAVING SUM(Y) >= 6 (EXEMPLO)   
 
 <h3>CLASSIFICAR RESULTADOS (CASE)</h3>
 
 - Se acontesse determinada condição eu faço determinada coisa. 
 - Fazemos um teste em um ou mais campos e, dependendo do resultado, teremos outro valor.
 `ex:`CASE WHEN <COND1> THEN <VALOR1>...
 - Caso nenhuma cond funcione, ultiliza-se o 'ELSE', ou seja, ELSE valor ELSE.  
 
 ![image](https://user-images.githubusercontent.com/101754313/185488216-5a628d40-4126-4175-b645-14309f4b79ea.png)
 
 <br> 
 
 ![image](https://user-images.githubusercontent.com/101754313/185501854-01507417-1a7c-4e7a-8a1c-903779944cee.png)
 <br>
 
 classificando os nascidos antes de 1990 (velhos), entre 1990 e 1995 e acima de 1995. Listando nome e esta classficação. 
 ![image](https://user-images.githubusercontent.com/101754313/185505587-2c3db106-107e-45d8-8935-c5f920fabd8d.png)
 <br>
 
 ![image](https://user-images.githubusercontent.com/101754313/185514466-a0a80676-cf1c-4430-9f60-24ef2809e2e9.png)
 
 - Obtendo o faturamento anual da empresa, levando em consideração o valor das vendas consiste em mult quant pelo preço,
 
 ![image](https://user-images.githubusercontent.com/101754313/185636761-6ecd2560-3f0f-4e95-a7c6-c7a072c93c7f.png)

 <h3>UNION</h3>
 
 - Comando que junta duas consultas (duas ou mais tabelas).
 - Colunas parecidas e mesmos tipos de colunas para realizar.
 - UNION ALL não se aploca o DISTINCT (linhas com valores diferentes).
 - Pode-se simular um left um right com UNION no meio, para "aplicar" um 'FULL JOIN'.
 
 <h3>SUBCONSULTAS</h3>
 
 - Pode-se usar uma subconsulta dentro de uma consulta.
 - SELECT X, Y FROM TAB1 WHERE Y IN (1, 2)
 - Também trabalha com valores diferentes 
 
 ![image](https://user-images.githubusercontent.com/101754313/186309330-da5e1c05-ef18-4c7d-91e0-4da0970de5aa.png)

 <br>
 
 ![image](https://user-images.githubusercontent.com/101754313/186309880-c559e49e-3f72-4187-b2eb-20447af1205b.png)

 - abaixo segue a quantidade de cpf cadastrados no ano de 2016 que contenha mais de 2000 nf: 
 
 ![image](https://user-images.githubusercontent.com/101754313/186311901-72a2dc69-679e-418f-a9e9-64bfdc097db9.png)

 <h3>VISÂO</h3>
 
 - A view é uma tabela lógica, resultado de uma consulta, que pode ser usada depois de qualquer outra consulta. 
 - Úteis quando se quer compartilhar para alguém externo as informações (em parte) de nosso banco.
 - WorkB ou pelo assistente. (AULA 4) 

<h3>STRINGS</h3>

- Importante leitura de documentação. Abaixo um exemplo de uso: 

![image](https://user-images.githubusercontent.com/101754313/186976361-d5ddf489-7430-42d0-9ebb-357ca79c444d.png)
 
 - Retornando: 
 
 ![image](https://user-images.githubusercontent.com/101754313/186976478-70e45018-cf0f-4939-89ab-e8651d1a81c0.png)

 <h3>FUNÇÕES DE DATAS e MATEMÁTICAS</h3>
 
 ![image](https://user-images.githubusercontent.com/101754313/186978911-395814eb-2a37-453d-b7b8-e402c4b5cba4.png)

 - Resultando: 
 
 ![image](https://user-images.githubusercontent.com/101754313/186978971-7d3b5669-c12f-4214-bc90-34bd078ba218.png)
 
 - Valor do imposto pago no ano de 2016 arredondando para o menor inteiro: 
 
 ![image](https://user-images.githubusercontent.com/101754313/186982994-535d9860-b4bf-49b1-b2e3-6353e21c714c.png)

 <h3>CONVERÇÃO DE DADOS</h3>
 
 - Visualização de documentação. 
 - %m/%c/%y for example. gmail
 - Exemplo resultado de faruramento para cada cliente:
 
 ![image](https://user-images.githubusercontent.com/101754313/186984723-b05d8ba1-edbe-4bd8-9e93-4533a3a08b58.png)
 
 - Resultando: 
 
 ![image](https://user-images.githubusercontent.com/101754313/186984775-69806eb7-b1ba-49e9-b24d-e0bac58ddfd9.png)

- Exemplo: obtendo volume total de vendas para cada cliente dentro de 1 mês 
- Começamos agrupando as vendas, tendo início pelas datas. 
- Dessa forma, juntando os dados, uma vez que 1 cpf realizou diversas compras.
- SUM é o método usado para agrupamento. 

![image](https://user-images.githubusercontent.com/101754313/187100348-edacaa1c-e1db-4c69-bd13-dfcf9679e694.png)
 
 - Resultando em:
 
 ![image](https://user-images.githubusercontent.com/101754313/187100296-18df3e0f-0e95-448a-aec3-0381c983eda2.png)

 - Agora iremos comparar duas tabelas (VENDAS MENSAL POR CLIENTE E A DE LIMITE DE COMPRAS)
 - utlizando subqueries:
 
 ![image](https://user-images.githubusercontent.com/101754313/187101467-82061ed4-749d-43c0-a628-0f8389c9542a.png)
 
 - Resultando em: 
 
 ![image](https://user-images.githubusercontent.com/101754313/187101480-04a0c012-37de-4ae3-bc95-1de7996829e0.png)

- Próximo exemplo será a tabela de vendas por sabor: 
 
 `bizu`: juntar as 3 tabelas (prod, nf, inf)
 
 ![image](https://user-images.githubusercontent.com/101754313/187106593-f7010570-dfed-4449-9b41-326de9b54038.png)

 - resultado:
 
 ![image](https://user-images.githubusercontent.com/101754313/187106631-94dfc6bf-2e35-440d-812a-3604c40d5c4e.png)

