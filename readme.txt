O projeto tem APIs para cadastro e login de usuarios, para criar, deletar e filtrar salas, e tambem fazer, 
remover e filtrar agendamentos de uma sala. Também conta com um sistema de logs em uma tabela.

---

O que eu usei:

- Python 3.13
- Django 4.x
- SQLite
- Bruno (Cliente de API/HTTP)

---

📦 Como rodar o projeto localmente

1. Clone o repositório
2. entre em magazine_remake no cmd/bash
3. dê o comando "python manage.py runserver"
4. no seu http client navegue nas urls usando suas devidas funções

---

Como funciona:

LOGS:
O app logs serve para criar logs de todo o projeto,
contendo nele o logs que tem um dicionário global para que fique
tudo organizado e também mais prático de se fazer, e tambem todos
ficam iguais desse jeito, pra evitar ficar trocando
frases de sucesso/erro. A tabela logs(SQLite) mostra tudo que
entra nas logs, tudo de importante que acontece, contendo
criações e deletes que foram dados pelos usuários. Ele conta com
uma função ( import logger() ), para registrar.

AUTHENT:
O app authent que é um AUTH, serve para cuidar dos usuários,
ele trata os cadastros e logins, conta com uma chave que faz
o APP RESERVES serem herdados pelos usuários para que fique 
organizado e assim sabermos qual usuário criou
o quê na tabela de agendamentos, caso usuário ou sala seja
deletado, os agendamentos se vão com ele.

ROOM:
O app room trata das salas, faz criações delas, deleta e
também às filtra, cuida somente disso, tem uma chave
também com o app de reservas, assim como os usuários.

RESERVES:
O app reserves cuida de todos os agendamentos feitos
pelos usuarios, agendando as salas requisitadas,
ou, removendo agendamentos feitos na sala,
e tratando de mostrar a agenda de horário daquela
sala que, pode ser selecionada pela API de filtragem
do próprio app, que mostra apenas as reservas.

---