# 🤖 Wiki Bot Termux

Um assistente interativo que responde perguntas usando a **Wikipédia** diretamente no **Termux**.  
O bot também lê as respostas em voz alta usando o **Termux:API**.

---

## 🌟 Funcionalidades

- ✅ Perguntas direto para a Wikipédia em português.  
- ✅ Resposta em **versão curta** (resumo) ou **versão longa** (artigo em blocos).  
- ✅ Leitura em voz alta com `termux-tts-speak`.  
- ✅ Digite `sair` para encerrar.

---

## 🎬 Demonstração

![Demo do Wiki Bot no Termux](link-do-seu-gif-aqui.gif)  

> `link-do-https://imgur.com/a/4vI80Y6

---

## 📥 Instalação Rápida (Linha Única)

Cole esta linha no **Termux** para instalar tudo e rodar o bot:

```bash
pkg update && pkg upgrade -y && pkg install git python termux-api -y && pip install wikipedia && git clone https://github.com/snaidermadilus-debug/wiki-bot-termux.git && cd wiki-bot-termux && python wiki_bot.py

____________________________________________________________
____________________________________________________________

pkg update && pkg upgrade -y

pkg install git python termux-api -y

pip install wikipedia

pip install wikipedia

depois clonar o repositório

git clone https://github.com/snaidermadilus-debug/wiki-bot-termux.git
cd wiki-bot-termux

execute o bot

python wiki_bot.py

___________________

📝 Como usar

1️⃣ Faça uma pergunta em português:

Pergunte algo (ou digite 'sair'): o que é gpt

Resposta do Wikipédia (curta):
ChatGPT (do inglês: Chat Generative Pre-trained Transformer) é um chatbot desenvolvido pela OpenAI e lançado em 30 de novembro de 2022. O nome "ChatGPT" combina "Chat", referindo-se à sua funcionalidade de chatbot, e "GPT", que significa Generative Pre-trained Transformer (Transformador Pré-treinado Generativo, em tradução livre), um tipo de modelo de linguagem grande (Large Language Model, LLM, na sigla em inglês). Com base em um LLM, ele usa como contexto, prompts e respostas sucessivas para prever as palavras que seriam mais adequadas, de acordo com as ideias da empresa, para compor a nova resposta; o algoritmo para essa previsão resulta do seu treinamento.

2️⃣ Quer ouvir a versão longa? (s/n)

3️⃣ Para sair:
Pergunte algo (ou sair): sair
Encerrando o programa. Até mais!

📌 Observações

🔊 Certifique-se de que o Termux tem acesso à API de TTS (termux-tts-speak).

🌐 O bot funciona melhor em perguntas que têm páginas correspondentes na Wikipédia. tipo o que é ?

⚡ Dica: Use perguntas curtas e objetivas para obter melhores respostas.


🏷 Badges?


🌐 Siga-me nas redes sociais

Instagram: @gg__snaider


🔗 Links Úteis

Baixar Termux no F-Droid (Android)

Termux:API no F-Droid


👨‍💻 Autor

Criado por @snaidermadilus-debug 🚀


