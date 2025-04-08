# 🚚 Previsão de Taxa de Entrega - Flask App

Este projeto é uma aplicação web feita com Flask que utiliza um modelo de **regressão treinado em Python** (com Pandas, Scikit-learn, etc.) para **estimar o valor da taxa de entrega** de um pedido com base em algumas variáveis de entrada.

## 🔍 Objetivo

Permitir que usuários possam prever o custo de entrega considerando:

- Distância
- Horário do pedido
- Valor do pedido
- Número de pedidos simultâneos
- Severidade do clima
- Severidade do congestionamento

## 💡 Como funciona

1. O usuário acessa a página inicial e preenche os dados no formulário.
2. O back-end em Flask trata os dados e os envia para um modelo `.pkl` previamente treinado.
3. A previsão é exibida de forma amigável diretamente na tela.

## 🧪 Tecnologias Utilizadas

- Python
- Flask
- Pandas / NumPy
- Scikit-learn (para o modelo de regressão)
- HTML/CSS
- Bootstrap (opcional, para estilização)

## 🚀 Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/Matheus-Farias86/Taxa-de-Entrega
cd Taxa-de-entrega
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Rode a aplicação:

```bash
python app.py
```

5. Acesse via navegador

```bash
http://localhost:3000
```
