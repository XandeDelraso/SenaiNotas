def calcular_media(notas):
    pesos = {'av1': 0.25, 'av2': 0.25, 'av3': 0.3, 'edag': 0.2}
    media = sum(notas[n] * pesos[n] for n in notas)
    return media

def nota_necessaria(notas, meta=7.0):
    pesos = {'av1': 0.25, 'av2': 0.25, 'av3': 0.3, 'edag': 0.2}
    peso_total = sum(pesos[n] for n in pesos if n not in notas)
    nota_atual = calcular_media(notas)
    restante = meta - nota_atual

    if peso_total == 0:
        return None  

    nota_necessaria = restante / peso_total
    return nota_necessaria

def entrada_notas():
    notas = {}
    for av in ['av1', 'av2', 'av3', 'edag']:
        resp = input(f"Você já tem a nota da {av.upper()}? (s/n): ").strip().lower()
        if resp == 's':
            nota = float(input(f"Digite a nota da {av.upper()}: "))
            notas[av] = nota
    return notas

def salvar_em_arquivo(resultados, nome_arquivo="resultados.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for linha in resultados:
            f.write(linha + "\n")
    print(f"\n📁 Resultados salvos em: {nome_arquivo}")

def main():
    historico_resultados = []

    while True:
        print("\n--- CALCULADORA DE MÉDIA ---")
        print("1 - Calcular média com todas as notas")
        print("2 - Simular quanto preciso para passar")
        print("0 - Sair e salvar resultados")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            materia = input("\nDigite o nome da matéria: ").strip().title()
            print("Digite todas as notas:")
            notas = {}
            for av in ['av1', 'av2', 'av3', 'edag']:
                notas[av] = float(input(f"{av.upper()}: "))
            media = calcular_media(notas)
            status = "✅ Aprovado" if media >= 7 else "❌ Reprovado"
            resultado = f"{materia}: Média final {media:.2f} - {status}"
            historico_resultados.append(resultado)
            print(f"\n📘 {resultado}")

        elif opcao == '2':
            materia = input("\nDigite o nome da matéria: ").strip().title()
            notas = entrada_notas()
            if len(notas) == 4:
                media = calcular_media(notas)
                status = "✅ Aprovado" if media >= 7 else "❌ Reprovado"
                resultado = f"{materia}: Média final {media:.2f} - {status}"
                historico_resultados.append(resultado)
                print(f"\n📘 {resultado}")
                continue

            nota_min = nota_necessaria(notas)
            if nota_min is None:
                resultado = f"{materia}: Todas as notas já foram inseridas."
            elif nota_min > 10:
                resultado = f"{materia}: ❌ Não é possível passar — precisaria tirar {nota_min:.2f}, maior que 10."
            else:
                resultado = f"{materia}: 📌 Precisa tirar {nota_min:.2f} nas avaliações restantes para passar."
            historico_resultados.append(resultado)
            print(f"\n📘 {resultado}")

        elif opcao == '0':
            salvar_em_arquivo(historico_resultados)
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
