WikiBot Termux

Um bot simples em Python que busca respostas no Wikipédia em português e fala as respostas usando o Termux:API. Ele mostra um resumo curto da resposta e dá a opção de ouvir uma versão longa.

Funcionalidades

Busca informações diretamente no Wikipédia em português.

Mostra um resumo curto (3 frases).

Pergunta se você quer ouvir a versão longa (10 frases).

Fala a resposta usando o Termux TTS.

Permite digitar SAIR para encerrar o programa.


Requisitos

Para rodar este programa, você precisa ter:

Python 3 instalado no Termux ou PC.

Termux:API instalada no Termux:

pkg install termux-api

Biblioteca wikipedia do Python:

pip install wikipedia


Como usar

1. Clone ou baixe este repositório:

git clone https://github.com/SEU_USUARIO/wiki-bot-termux.git


2. Entre na pasta do projeto:

cd nome-do-repositorio


3. Execute o programa:

python wiki_bot.py


4. Digite qualquer pergunta. Exemplo:

Pergunte algo (ou SAIR): Minecraft


5. O bot vai mostrar o resumo curto e falar a resposta.


6. Ele perguntará se você quer ouvir a versão longa. Digite sim ou não.


7. Para sair, digite SAIR.



Observações

Funciona melhor no Termux por causa da integração com o TTS (termux-tts-speak).

Caso a pergunta seja ambígua, ele sugerirá algumas opções.

Se não encontrar resultados, ele avisará.
