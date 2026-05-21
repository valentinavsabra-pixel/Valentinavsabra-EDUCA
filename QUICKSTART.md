# 🚀 Guia de Início Rápido - Educa+

## ⚡ Instalação em 3 Passos

### Para Windows:
```batch
# 1. Execute o instalador
double-click install.bat

# Ou manualmente:
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Para Mac/Linux:
```bash
# 1. Execute o instalador
chmod +x install.sh
./install.sh

# Ou manualmente:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## ▶️ Executar a Aplicação

```bash
# 1. Ativar ambiente virtual (se não estiver ativo)

# Windows:
venv\Scripts\activate.bat

# Mac/Linux:
source venv/bin/activate

# 2. Iniciar servidor
python app.py

# 3. Abrir no navegador
http://localhost:5000
```

## 📝 Contas de Demo

### Aluno:
```
Email: aluno@educa.com
Senha: 123456
```

### Professor:
```
Email: professor@educa.com
Senha: 123456
```

## 🎯 O Que Você Pode Fazer

### Como Aluno:
- ✅ Ver dashboard com disciplinas
- ✅ Fazer quizzes e ganhar XP
- ✅ Visualizar progresso
- ✅ Desbloquear conquistas
- ✅ Conversar com assistente Edu

### Como Professor:
- ✅ Ver dashboard com ferramentas
- ✅ Usar ProfIA para gerar aulas
- ✅ Monitorar alunos
- ✅ Ver relatórios
- ✅ Gerenciar conteúdo

## 🆘 Solução de Problemas

### Erro: "Port 5000 already in use"
```bash
# Use outra porta
python app.py -p 5001
```

### Erro: "Python not found"
```bash
# Certifique-se de ter Python 3.8+ instalado
python --version
# ou
python3 --version
```

### Erro: "Module not found"
```bash
# Reinstale as dependências
pip install -r requirements.txt
```

## 📂 Estrutura do Projeto

```
Educa+/
├── app.py                    # Aplicação Flask
├── requirements.txt          # Dependências
├── README.md                 # Documentação completa
├── QUICKSTART.md            # Este arquivo
├── install.sh               # Script para Mac/Linux
├── install.bat              # Script para Windows
├── .env.example             # Variáveis de ambiente
├── .gitignore               # Ignorar arquivos
└── templates/               # Templates HTML
    ├── base.html            # Template base
    ├── index.html           # Homepage
    ├── login.html           # Login
    ├── signup.html          # Cadastro
    ├── student_dashboard.html
    ├── teacher_dashboard.html
    ├── quiz.html
    └── profile.html
```

## 🔧 Verificações Iniciais

Quando você acessa a aplicação:

- [ ] Homepage carrega com cores (laranja/roxo)
- [ ] Botões "Entrar" e "Cadastre-se" funcionam
- [ ] Consegue fazer login com dados de demo
- [ ] Dashboard carrega após login
- [ ] Quiz funciona e você consegue responder
- [ ] XP aumenta ao acertar questões

Se tudo funciona ✅ - **Parabéns! Está pronto para usar!**

## 💡 Dicas

1. **Primeiro Login**: Use a conta de demo para testar
2. **Ganhar XP**: Responda corretamente as questões
3. **Subir de Nível**: Continue respondendo para ganhar mais XP
4. **Explorar**: Teste todas as funcionalidades

## 📞 Precisando de Ajuda?

- Leia o README.md completo
- Verifique se Python está instalado
- Certifique-se de estar no diretório correto
- Reinstale as dependências

## 🎉 Pronto!

Você agora tem o Educa+ funcionando localmente! Divirta-se aprendendo! 🚀

---

**Feito com ❤️ para transformar a educação**
