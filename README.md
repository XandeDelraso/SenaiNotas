# SenaiNotas 📘

Calculadora de médias para estudantes do **Senai Cimatec**, com interface web moderna e prévia em tempo real.

---

## ✨ Funcionalidades

- **Calcular média final** — insira as 4 notas e obtenha a média ponderada instantaneamente
- **Simular nota necessária** — ative só as notas que você já tem e veja em tempo real o mínimo necessário nas avaliações restantes
- **Prévia ao vivo** — o resultado atualiza a cada tecla digitada, sem precisar clicar em nada
- **Histórico da sessão** — todos os cálculos ficam registrados durante o uso
- **100% offline** — nenhuma dependência de servidor, funciona direto no navegador

---

## 🧮 Sistema de pesos

| Avaliação | Peso |
|-----------|------|
| AV1       | 25%  |
| AV2       | 25%  |
| AV3       | 30%  |
| EDAG      | 20%  |

> Média mínima para aprovação: **7.0**

---

## 🚀 Como usar

### Interface web (recomendado)

Abra o arquivo `index.html` direto no navegador — sem instalar nada.

```bash
# Ou, se preferir um servidor local:
python3 -m http.server 8000
# Acesse: http://localhost:8000
```

### Script Python (terminal)

```bash
python3 backend.py
```

---

## 📁 Estrutura do projeto

```
SenaiNotas/
├── index.html   # Interface web completa (frontend)
├── backend.py   # Script original em Python (terminal)
└── README.md
```

---

## Autor

**Alexandre Del Raso Filho**  
Senai Cimatec
