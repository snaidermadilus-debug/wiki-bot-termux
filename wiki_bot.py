import wikipedia
import os

wikipedia.set_lang("pt")  # Define a língua para português

def pesquisar_wikipedia():
    while True:
        pergunta = input("Pergunte algo (ou sair): ").strip()
        
        if pergunta.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            os.system('termux-tts-speak "Encerrando o programa. Até mais!"')
            break

        try:
            # Resumo curto (3 frases)
            resumo_curto = wikipedia.summary(pergunta, sentences=3)
            print("\nResposta do Wikipédia (curta):")
            print(resumo_curto)
            os.system(f'termux-tts-speak "{resumo_curto}"')

            # Pergunta se quer a versão longa
            opcao = input("\nQuer ouvir a versão longa? (s/n) ").strip().lower()
            if opcao == "s":
                resumo_longo = wikipedia.summary(pergunta, sentences=10)  # Mais detalhado
                print("\nVersão longa:")
                print(resumo_longo)
                os.system(f'termux-tts-speak "{resumo_longo}"')
            else:
                print("Continuando para a próxima pergunta...\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("\nSua pergunta pode se referir a várias coisas. Seja mais específico!")
            print("Sugestões:", e.options[:5])
            os.system('termux-tts-speak "Sua pergunta pode se referir a várias coisas. Seja mais específico."')

        except wikipedia.exceptions.PageError:
            print("\nNão encontrei nada no Wikipédia sobre isso.")
            os.system('termux-tts-speak "Não encontrei nada no Wikipédia sobre isso."')

pesquisar_wikipedia()
