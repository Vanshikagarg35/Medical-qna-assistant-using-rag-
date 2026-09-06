@echo off
cd /d %~dp0
call backend\.venv\Scripts\activate
python scripts\build_index.py
pause
