# Perguntas
## 1) Você acha que este código está estruturado, legível e escalável?

Não está em uma estrutura convencional vistas em aplicações Django. Há problema de responsabilidade já que conexões com o banco, acessos a interface da aplicação e URLs são definidas em um único arquivo, o que é um equívoco de na responsabilidade como dito. Assim como a falta de camadas de escopo para separar modelos e serviços, o que não há, está tudo concentrado em um único local, facilitando acessos e quebras de segurança.
Também não há legibilidade clara, incongruências nas configurações de variáveis de ambiente; e uma falta grande de comentários para auxiliar em partes críticas do código também falta.
A escalabilidade é altamente problemática. Chamadas na persistência com Mongo não é estruturada para uma conexão construtiva com o banco, cada request necessário é gerada uma nova conexão com o banco,o que cria um grande gargalo. A falta de tratamento dos erros também é algo perceptivo tanto olhando para o código quanto ao rodá-lo, ocasionando em erros que podem ser evitados com tratamentos adequados. Paginação na consulta de animais pode ser considerado um problema de escalabilidade também ao decorrer que os dados forem escalonados. Validação de parâmetros e uso de DTOs podem ajudar a manter um código mais conciso e protegido de falhas no transporte de dados.
	A pasta __pycache__ não deveria está presente no repositório remoto, e deveria estar listada no .gitignore para não dar problemas futuros de compilação.

## 2) O que você mudaria nos arquivos e na estrutura de pastas para melhorá-lo nesse sentido?

A estrutura inicial conta com muitas misturas de responsabilidades. Por exemplo, o __init__.py em api/ está com views, urls e wsgi em um só lugar, o que deve ser separado. O wsgi.py está vazio e seu uso deve ser feito.

Primeiramente deixaria a estrutura como comumente é construída em Django e seguindo as documentações oficiais:

DjangoAPIMongoTest/
----- api/
---------- __init__.py		(só imports)
---------- settings.py		Mudança de segurança
---------- urls.py			Ajustes URLs principais
---------- wsgi.py			Utilizar WSGI
----- animals/			    Camada para Entidade
---------- __init__.py
---------- views.py		    views ficam aqui
---------- urls.py			URLs do app
---------- services.py		Lógica da persistência com MongoDB
----- .env			        Variáveis de ambiente
----- requirements.txt
----- manage.py
----- docker-compose.yml	Configs de uso do docker-compose

Dessa forma podemos ter:
Estrutura que centraliza responsabilidades, como a criação da pasta animals e de services views e urls para ele.
Criamos arquivos para centralizar variáveis de ambiente que devem ser protegidas e invisíveis em repositórios remotos e ajustadas posteriormente em um ambiente de produção; credenciais que não podem ficar diretamente no código.
Configuração para a separação de DEBUG a depender do ambiente;
Foi usado Self-Describing API para ajudar a usar a API desde a primeira roda;

## 3) Quanto a arquitetura API e sua conteinerização, liste as brechas de segurança que você identificou neste código? Como você as resolveria?

MongoDB sem autenticação no Docker
Secret keys hardcoded, (ainda continua por facilidade)
CORS não configurado
Sem rate limiting
Logs podem expor dados sensíveis
Sem HTTPS obrigatório

Para melhorias foi:
colocado .env para definir variáveis de ambiente;
DEBUG=False em produção
Variáveis de MongoDB agora organizadas
Alteração de senha simples para uma senha mais “forte”
Dados do MongoDB agora são persistidos com mong_data

