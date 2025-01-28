
# Super OrgContact - Back-End

Repositório do back-end da aplicação **Super OrgContact**, responsável por consumir os dados da API Google People e fornecer as informações necessárias ao front-end.

## Tecnologias Utilizadas
- Python 3.9
- Flask
- Flask-CORS
- Google API Client
- Google Cloud Run para hospedagem

## Funcionalidades
- Autenticação OAuth2 com o Google.
- Consumo da API Google People para obter contatos.
- API REST para comunicação com o front-end.

## Pré-requisitos
- Python 3.9 ou superior

## Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone <url-do-repo>
   cd back-end
   ```

2. Crie um ambiente virtual e instale as dependências:
 
    **No Linux/macOS:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   **No Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Execute o servidor localmente:
   ```bash
   python app.py
   ```

5. Acesse o back-end:
   - URL local: `http://localhost:5000`.

## URL do Deploy

O projeto foi implantado para acesso público, permitindo que você o utilize sem a necessidade de configuração local.

- **Front-End:** O front-end está hospedado no Firebase Hosting e pode ser acessado através do seguinte link:
  ```
    https://vue-teste-conecta.web.app/
  ```

- **Back-End:** O back-end está hospedado no Google Cloud Run e pode ser acessado através do seguinte link:
  ```
  https://sapient-fabric-322416.uc.r.appspot.com
  ```
