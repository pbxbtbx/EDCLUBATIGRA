@echo off
cd /d "%~dp0"
title ATIBOT Academy - Inicio local
where py >nul 2>&1
if not errorlevel 1 (
    py -3 iniciar.py
) else (
    where python >nul 2>&1
    if errorlevel 1 (
        echo No se encuentra Python. Instala Python 3.11 o superior desde python.org.
        echo Durante la instalacion, activa Add Python to PATH.
    ) else (
        python iniciar.py
    )
)
echo.
pause
