# Desafio Técnico - Intuitive Care (API + Frontend)

Este repositório contém a implementação da segunda etapa do desafio técnico da Intuitive Care, onde foi solicitado o desenvolvimento de uma API e uma interface web que permitissem a busca por operadoras ativas da ANS.

## 📦 Estrutura do Projeto

```
.
├── api_operadoras/        # Backend Flask
│   ├── app.py             # Servidor com rota /operadoras
│   └── requirements.txt   # Dependências da API
├── frontend_vue/          # Frontend Vue 3 (Vite)
│   └── App.vue            # Componente com input e listagem
├── Projeto_API_Operadoras_ANS.docx  # Documento técnico explicativo
├── README.md              # Este arquivo
```

## 🚀 Como executar

### Backend (Flask)
```bash
cd api_operadoras
pip install -r requirements.txt
python app.py
```
> A API estará disponível em: http://localhost:5000/operadoras?q=termo

### Frontend (Vue 3 + Vite)
```bash
cd frontend_vue
npm install
npm run dev
```
> O frontend será iniciado em: http://localhost:5173

## 🧠 Funcionalidades

- 🔍 Busca textual por nome fantasia ou razão social da operadora
- ✅ Retorna até 10 resultados relevantes
- 🛡️ Trata dados ausentes (`NaN` → `null`) para evitar erros no frontend
- 🔄 Respostas em tempo real conforme o usuário digita

## 📄 Dados utilizados

Utiliza o arquivo CSV de operadoras ativas da ANS (item 3.2 do teste). O arquivo deve estar nomeado como `operadoras.csv` e posicionado na pasta `api_operadoras`.

## ✍️ Autor

Desenvolvido por **Carlos Augusto**  
Portfólio: [https://devside.com.br](https://devside.com.br)

---

✅ Projeto testado e funcionando.