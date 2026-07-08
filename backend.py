import argparse
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PESOS = {'av1': 0.25, 'av2': 0.25, 'av3': 0.3, 'edag': 0.2}
META = 7.0


def calcular_media(notas):
    media = sum(notas[n] * PESOS[n] for n in notas)
    return media


def nota_necessaria(notas, meta=META):
    peso_total = sum(PESOS[n] for n in PESOS if n not in notas)
    nota_atual = calcular_media(notas)
    restante = meta - nota_atual

    if peso_total == 0:
        return None  

    nota_minima = restante / peso_total
    return nota_minima


def normalizar_notas(notas, exigir_todas=False):
    if not isinstance(notas, dict):
        raise ValueError("Formato de notas inválido.")

    notas_normalizadas = {}
    for av, valor in notas.items():
        if av not in PESOS:
            raise ValueError(f"Avaliação inválida: {av}")
        nota = float(valor)
        if nota < 0 or nota > 10:
            raise ValueError(f"Nota fora do intervalo permitido (0-10): {av}")
        notas_normalizadas[av] = nota

    if exigir_todas and set(notas_normalizadas.keys()) != set(PESOS.keys()):
        raise ValueError("É necessário informar todas as 4 notas.")

    if not notas_normalizadas:
        raise ValueError("Informe pelo menos uma nota.")

    return notas_normalizadas


def processar_calculo_media(notas):
    notas_normalizadas = normalizar_notas(notas, exigir_todas=True)
    media = calcular_media(notas_normalizadas)
    return {
        "media": media,
        "status": "aprovado" if media >= META else "reprovado",
    }


def processar_simulacao(notas):
    notas_normalizadas = normalizar_notas(notas)

    if len(notas_normalizadas) == 4:
        media = calcular_media(notas_normalizadas)
        return {
            "tipo": "completo",
            "media": media,
            "status": "aprovado" if media >= META else "reprovado",
        }

    nota_minima = nota_necessaria(notas_normalizadas)
    return {
        "tipo": "simulacao",
        "nota_atual": calcular_media(notas_normalizadas),
        "nota_necessaria": nota_minima,
    }


class SenaiNotasHandler(SimpleHTTPRequestHandler):
    def _responder_json(self, payload, status=200):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path not in ("/api/calcular_media", "/api/simular_nota"):
            self._responder_json({"erro": "Endpoint não encontrado."}, status=404)
            return

        try:
            tamanho = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(tamanho).decode("utf-8") if tamanho else "{}"
            payload = json.loads(body)
            notas = payload.get("notas", {})

            if self.path == "/api/calcular_media":
                resultado = processar_calculo_media(notas)
            else:
                resultado = processar_simulacao(notas)

            self._responder_json(resultado)
        except ValueError as erro:
            self._responder_json({"erro": str(erro)}, status=400)
        except (json.JSONDecodeError, TypeError):
            self._responder_json({"erro": "JSON inválido."}, status=400)


def executar_servidor(host="127.0.0.1", port=8000):
    base_dir = Path(__file__).resolve().parent
    servidor = HTTPServer((host, port), SenaiNotasHandler)
    print(f"Servidor iniciado em http://{host}:{port}")
    print("Use Ctrl+C para parar.")
    try:
        import os
        os.chdir(base_dir)
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        servidor.server_close()

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
    parser = argparse.ArgumentParser(description="Calculadora de médias SenaiNotas")
    parser.add_argument(
        "--modo",
        choices=["cli", "server"],
        default="cli",
        help="Escolha entre modo terminal (cli) e modo servidor web (server).",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host do servidor web.")
    parser.add_argument("--port", type=int, default=8000, help="Porta do servidor web.")
    args = parser.parse_args()

    if args.modo == "server":
        executar_servidor(host=args.host, port=args.port)
    else:
        main()
