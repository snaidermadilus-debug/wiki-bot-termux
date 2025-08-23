# 🤖 Wiki Bot Termux

Um assistente que responde perguntas usando a **Wikipédia** diretamente no **Termux**.  
O bot também lê as respostas em voz alta usando o **Termux:API**.

---

## 💡 Funcionalidades

- Faz perguntas direto para a Wikipédia em português.  
- Resposta em **versão curta** (resumo) e **versão longa** (artigo em blocos).  
- Fala as respostas usando `termux-tts-speak`.  
- Digite `sair` para encerrar.

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

