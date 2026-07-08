# SenaiNotas 📘

Calculadora de médias para estudantes do **Senai Cimatec**, com interface web moderna e lógica de cálculo em Python.

---

## ✨ Funcionalidades

- **Calcular média final** — insira as 4 notas e obtenha a média ponderada instantaneamente
- **Simular nota necessária** — ative só as notas que você já tem e veja em tempo real o mínimo necessário nas avaliações restantes
- **Prévia ao vivo** — o resultado atualiza a cada tecla digitada, sem precisar clicar em nada
- **Histórico da sessão** — todos os cálculos ficam registrados durante o uso
- **Frontend + Backend** — a interface web consome a lógica do `backend.py` via API

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

1. Inicie o backend:
   ```bash
   python backend.py --modo server
   ```
2. Abra no navegador:
   ```
   http://127.0.0.1:8000
   ```

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
