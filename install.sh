#!/bin/bash

# Script de instalação rápida para Educa+ (Mac/Linux)

echo "=========================================="
echo "🎓 Educa+ - Instalação Rápida"
echo "=========================================="
echo ""

# Verificar Python
echo "✓ Verificando Python..."
python3 --version

# Criar ambiente virtual
echo ""
echo "✓ Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
echo "✓ Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "✓ Instalando dependências..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "✅ Instalação concluída com sucesso!"
echo "=========================================="
echo ""
echo "Para iniciar a aplicação, execute:"
echo "  source venv/bin/activate"
echo "  python app.py"
echo ""
echo "Acesse: http://localhost:5000"
echo ""
