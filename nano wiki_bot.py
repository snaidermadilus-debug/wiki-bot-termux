 import wikipedia
import os

wikipedia.set_lang("pt")  # Português

def pesquisar_wikipedia():
    while True:
        pergunta = input("Pergunte algo (ou digite 'sair' para encerrar): ").strip()
        
        if pergunta.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            os.system('termux-tts-speak "Encerrando o programa. Até mais!"')
            break

        try:
            # Resumo curto
            resumo_curto = wikipedia.summary(pergunta, sentences=3, auto_suggest=True, redirect=True)
            print("\nResposta do Wikipédia (curta):")
            print(resumo_curto)
            os.system(f'termux-tts-speak "{resumo_curto}"')

            # Perguntar se quer versão longa
            opcao = input("\nQuer ouvir a versão longa? (s/n) ").strip().lower()
            if opcao == "s":
                resumo_longo = wikipedia.summary(pergunta, sentences=15, auto_suggest=True, redirect=True)
                if resumo_longo != resumo_curto:  # evita repetir
                    print("\nVersão longa:")
                    print(resumo_longo)
                    os.system(f'termux-tts-speak "{resumo_longo}"')
                else:
                    print("\nA versão longa é igual à curta.")
                    os.system('termux-tts-speak "A versão longa é igual à curta."')

        except wikipedia.exceptions.DisambiguationError as e:
            print("\nSua pergunta pode se referir a várias coisas. Seja mais específico!")
            print("Sugestões:", e.options[:5])
            os.system('termux-tts-speak "Sua pergunta pode se referir a várias coisas. Seja mais específico."')

        except wikipedia.exceptions.PageError:
            print("\nNão encontrei nada no Wikipédia sobre isso.")
            os.system('termux-tts-speak "Não encontrei nada no Wikipédia sobre isso."')

            resultados = wikipedia.search(pergunta)
            if resultados:
                print("Talvez você esteja procurando por:")
                for item in resultados[:5]:
                    print("-", item)

pesquisar_wikipedia()