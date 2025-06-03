# 🌐 CrypterraX - Site de Criptomoedas

Bem-vindo ao **CrypterraX**, um site completo desenvolvido com **Django**, **Python**, **HTML**, **CSS** e **JavaScript**, com foco em fornecer informações atualizadas sobre o mundo das criptomoedas. O projeto apresenta cotações em tempo real, gráficos interativos, um blog com notícias, depoimentos de usuários e muito mais.

## 🛠 Tecnologias Utilizadas

- **Django** (backend e gerenciamento de rotas e views)
- **Python** (lógica de servidor)
- **HTML5** (estrutura do site)
- **CSS3** (estilização e responsividade)
- **JavaScript** (funcionalidades dinâmicas e gráficos)
- **Chart.js** ou **ApexCharts** (para gráficos de preço)
- **API de Criptomoedas** (como CoinGecko ou CoinMarketCap)

## ⚙️ Funcionalidades

- 📈 Cotação em tempo real de criptomoedas
- 📊 Gráficos de variação de preços
- 📰 Blog com notícias do mundo cripto
- 🧾 Página de FAQ
- 💬 Depoimentos de usuários
- 📬 Formulário de contato
- 📱 Design responsivo (funciona bem em dispositivos móveis)

## 🔧 Instalação e Execução

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/cryptoinfo.git
   cd cryptoinfo
   
2. Crie e ative um ambiente virtual:
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    Instale as dependências:

3. Instale as dependências:
    ```
    pip install -r requirements.txt
    
4. Execute as migrações:
    ```
    python manage.py migrate
    
5. Inicie o servidor:
    ```
    python manage.py runserver
    
6. Acesse no navegador:
    ```
    http://127.0.0.1:8000/
