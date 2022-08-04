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
`OBS:` Para apagar usar o comando DROP {DATABASE | SCHEMA} [IF EXIST] db_name

<h1>STRINGS</h1>
<h4>Atributos dos campos númericos</h4> 
