import base64
import html


print('''  

{}  _                                                      {}
{} |  \   _           |  /  |  |  |  _               ___,  {}
{} ||| | |  \   |`))  |_/   |  |  | |  \   |`))    //      {}
{} ||| | |   \  | \   | \   |  |  | |   \  | \    ||====:  {}
{} |__/  |  _ \ |  \  |  \  |__|__| |  _ \ |  \     \___   {}
{}       |   `´ |                   |   `´ |            `  {}
{}       ;      ;                   ;      ;               {}
{}========================================================={}

''')

texto = input("Insira o texto: ")
opcao = int(input("Selecione a opção desejada:\n1 - Codificar em base64 \n2 - Decodificar de base64\n"))

if opcao == 1:
    texto_codificado = base64.b64encode(texto.encode("utf-8"))
    print("Texto codificado em base64:", texto_codificado.decode("utf-8"))
elif opcao == 2:
    texto_decodificado = base64.b64decode(texto).decode("utf-8")
    texto_decodificado = html.unescape(texto_decodificado)
    print("Texto decodificado:", texto_decodificado)
else:
    print("Opção inválida. Por favor, selecione 1 ou 2.")


#Python que codifica ou decodifica Base64. Só executar no Terminal.
