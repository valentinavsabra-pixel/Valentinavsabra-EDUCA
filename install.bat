@echo off
REM Script de instalação para Educa+ (Windows)

echo ==========================================
echo 🎓 Educa+ - Instalação Rápida
echo ==========================================
echo.

REM Verificar Python
echo ✓ Verificando Python...
python --version

REM Criar ambiente virtual
echo.
echo ✓ Criando ambiente virtual...
python -m venv venv

REM Ativar ambiente virtual
echo ✓ Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Instalar dependências
echo ✓ Instalando dependências...
pip install -r requirements.txt

echo.
echo ==========================================
echo ✅ Instalação concluída com sucesso!
echo ==========================================
echo.
echo Para iniciar a aplicação, execute:
echo   venv\Scripts\activate.bat
echo   python app.py
echo.
echo Acesse: http://localhost:5000
echo.
pause
