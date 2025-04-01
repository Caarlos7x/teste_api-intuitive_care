# API de Busca de Operadoras ANS

Esta API desenvolvida em Python com Flask realiza buscas textuais em um CSV de operadoras da ANS, retornando resultados relevantes por nome fantasia ou razão social.

## 🚀 Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o servidor:
```bash
python app.py
```

3. Faça uma requisição GET para:
```
http://localhost:5000/operadoras?q=amil
```

## 📄 Estrutura esperada do CSV

- registro_ans
- cnpj
- razao_social
- nome_fantasia
- ...

## 🧠 Funcionalidades

- Busca textual por `nome_fantasia` ou `razao_social`
- Retorno dos 10 primeiros resultados
- Tratamento de valores ausentes (`NaN` → `null`)
- Compatível com frontend Vue.js

## 🗂 Estrutura do Projeto

```
api_vue_ans/
├── api_operadoras/
│   ├── app.py
│   └── requirements.txt
└── frontend_vue/
    └── App.vue
```

## ✍️ Autor

Carlos Augusto  
Portfólio: https://devside.com.br