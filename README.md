# Educa+ - Plataforma Educacional Gamificada

## 🎓 Sobre o Projeto

Educa+ é uma plataforma educacional gamificada construída com **Python + Flask** que transforma o aprendizado em uma experiência divertida e envolvente.

## ✨ Recursos Principais

- 🎮 **Gamificação Completa** - XP, níveis, conquistas e ranking
- 🤖 **Assistente Edu** - IA para ajudar nos estudos
- 📚 **Múltiplas Disciplinas** - Português, Matemática, Inglês, História
- 📊 **Dashboard Inteligente** - Acompanhamento de progresso
- 👨‍🏫 **Ferramentas para Professores** - ProfIA, monitoramento e relatórios
- 🎯 **Exercícios Interativos** - Questões, caça-palavras, jogo da memória
- 📱 **Responsivo** - Funciona em desktop, tablet e mobile
- 🎨 **Design Moderno** - Tema Sunset Blaze (laranja e roxo)

## 🚀 Como Executar

### 1. Pré-requisitos

```bash
# Certifique-se de ter Python 3.8+ instalado
python --version
```

### 2. Clonar o Repositório

```bash
git clone https://github.com/valentinavsabra-pixel/Valentinavsabra-EDUCA.git
cd Valentinavsabra-EDUCA
```

### 3. Criar Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a Aplicação

```bash
python app.py
```

O servidor iniciará em: **http://localhost:5000**

## 👤 Contas de Demo

### Aluno
```
Email: aluno@educa.com
Senha: 123456
```

### Professor
```
Email: professor@educa.com
Senha: 123456
```

## 📁 Estrutura do Projeto

```
Educa+/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
└── templates/            # Templates HTML
    ├── base.html         # Template base
    ├── index.html        # Homepage
    ├── login.html        # Página de login
    ├── signup.html       # Página de cadastro
    ├── student_dashboard.html    # Dashboard do aluno
    ├── teacher_dashboard.html    # Dashboard do professor
    ├── quiz.html         # Página de quiz
    └── profile.html      # Página de perfil
```

## 🎮 Como Usar a Plataforma

### Para Alunos

1. **Login/Cadastro** - Crie sua conta como aluno
2. **Dashboard** - Veja suas disciplinas e progresso
3. **Fazer Quiz** - Responda questões e ganhe XP
4. **Ganhar Conquistas** - Desbloqueie badges ao atingir metas
5. **Usar Assistente Edu** - Converse com a IA para tirar dúvidas

### Para Professores

1. **Login/Cadastro** - Crie sua conta como professor
2. **Dashboard** - Acesse ferramentas e gerenciamento
3. **ProfIA** - Use IA para gerar aulas automaticamente
4. **Monitorar Alunos** - Acompanhe progresso dos seus alunos
5. **Criar Conteúdo** - Adicione disciplinas e exercícios

## 🎯 Sistema de XP e Gamificação

### Ganho de XP

| Ação | XP |
|------|----|
| Acertar questão fácil | 10 |
| Acertar questão média | 20 |
| Acertar questão difícil | 30 |
| Ganhar streak (5+ acertos) | +50 |
| Completar disciplina | 100 |

### Níveis

- 🥇 Nível 1: 0-499 XP
- 🥈 Nível 2: 500-999 XP
- 🥉 Nível 3: 1000-1499 XP
- 👑 Nível 4+: 1500+ XP

## 🏆 Conquistas

- **Iniciante** - 100 XP
- **Aprendiz** - 500 XP
- **Mestre** - 1000 XP
- **Campeão** - 5000 XP

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Autenticação:** Werkzeug (hash de senhas)
- **Templates:** Jinja2
- **Storage:** Memória (simuldado)

## 📝 Rotas da API

```
Páblicas:
GET  /                      - Homepage
GET  /login                 - Página de login
POST /login                 - Fazer login
GET  /signup                - Página de cadastro
POST /signup                - Criar conta

Protegidas (autenticado):
GET  /student/dashboard     - Dashboard do aluno
GET  /teacher/dashboard     - Dashboard do professor
GET  /quiz/<discipline>     - Página de quiz
POST /quiz/<discipline>     - Submeter resposta
GET  /profile               - Página de perfil
GET  /logout                - Fazer logout

API:
GET  /api/questions/<discipline>  - Obter questões
GET  /api/user              - Obter dados do usuário
```

## 🚀 Próximas Implementações

- [ ] Integração com banco de dados (PostgreSQL/MySQL)
- [ ] Sistema de IA real (OpenAI/Claude)
- [ ] Certificados digitais
- [ ] Competições entre turmas
- [ ] Sistema de recomendações
- [ ] Análise de estilos de aprendizado
- [ ] Integração com redes sociais
- [ ] Sistema de notificações
- [ ] Mais tipos de exercícios
- [ ] Relatórios avançados

## 🤝 Contribuindo

Sugestões e contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.

## 📄 Licença

Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## 👨‍💻 Autor

Criado por **Valentina Sabra**

## 📞 Contato

- Email: valentinavsabra@gmail.com
- GitHub: [@valentinavsabra-pixel](https://github.com/valentinavsabra-pixel)

---

**Feito com ❤️ para transformar a educação** 🎓✨