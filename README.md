# py3-std
<h1>ESTUDO AMPLO</h1>
<br>
<p>Entendendo suas mecânicas e funcionalidades. Envolvendo ideias e projetos criados com o intuito de aprofundar meus conhecimentos sobre a linguagem. 
 Aprendendo também sobre Banco de Daados Relacioanis e Não-Relacioanis. Master Branch</P>
 <img src="https://dev.mysql.com/doc/workbench/en/images/wb-home-screen-new.png"/>
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
 Indica as colunas p/ visualizar limitando em 5 o número de informações. 

