
# Desafio Técnico - Intuitive Care (API + Frontend)

[![Testes Automatizados](https://github.com/Caarlos7x/teste_api-intuitive_care/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Caarlos7x/teste_api-intuitive_care/actions)

Este repositório contém a implementação da segunda etapa do desafio técnico da Intuitive Care. O objetivo foi desenvolver uma API em Flask que permite buscas por operadoras de saúde registradas na ANS, além de um frontend em Vue 3 para interface de consulta.

---

## 📦 Estrutura do Projeto

```
.
├── api_operadoras/          # Backend com Flask
│   ├── app.py               # Servidor e lógica de busca
│   ├── requirements.txt     # Dependências do backend
│   ├── tests/               # Testes automatizados com pytest
│   └── postman/             # Collection Postman para validação manual
├── frontend_vue/            # Frontend Vue 3 (Vite)
│   └── App.vue              # Componente principal
├── Projeto_API_Operadoras_ANS.docx  # Documento explicativo
├── .github/workflows/       # CI com GitHub Actions
├── README.md                # Este arquivo
```

---

## 🚀 Como executar o projeto localmente

### Backend (API Flask)
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

---

## 🧠 Funcionalidades

- 🔍 Busca textual por nome fantasia ou razão social
- ✅ Retorna até 10 resultados relevantes
- 🛡️ Trata dados ausentes (`NaN` → `null`)
- 🔁 Atualização automática dos dados enquanto o usuário digita

---

## 🧪 Testes Automatizados

- Implementados com `pytest`
- Cobertura de:
  - Erros de entrada (sem parâmetro)
  - Buscas válidas e inválidas
  - Limite de registros retornados
  - Performance (< 1s)
  - Suporte a caracteres acentuados

> Os testes são executados automaticamente no GitHub Actions a cada `push` ou `pull request`.

---

## 📬 Testes com Postman

Uma collection Postman com exemplos de uso da API está disponível em:

📁 `api_operadoras/postman/Operadoras_ANS_IntuitiveCare.postman_collection.json`

Inclui requisições para:

- ✅ Busca válida (`/operadoras?q=amil`)
- ⚠️ Busca sem parâmetro (`/operadoras`)
- ❌ Busca sem resultados (`/operadoras?q=naoencontrada123`)

---

## 📄 Dados utilizados

- Origem: ANS - Agência Nacional de Saúde Suplementar
- Arquivo: `operadoras.csv` (item 3.2 do teste)
- Localização: pasta `api_operadoras`

---

## ☁️ Deploy

- Frontend publicado na Vercel (Vue + Vite)
- API pronta para deploy em serviços como Render, Railway ou uso com `ngrok` para testes locais

---

## ✍️ Autor

Desenvolvido por **Carlos Augusto**  
🔗 Portfólio: [https://devside.com.br](https://devside.com.br)

---

✅ Projeto testado, versionado, documentado e pronto para produção.