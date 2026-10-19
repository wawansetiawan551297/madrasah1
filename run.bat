@echo off
cd /d "%~dp0"
py -m pip install -r requirements.txt
if errorlevel 1 (echo Gagal memasang Flask. Pastikan Python sudah terpasang. & pause & exit /b 1)
py app.py
pause
