@echo off
cd /d %~dp0
where python >nul 2>nul || (echo Install Python 3.11.& pause & exit /b 1)
where npm >nul 2>nul || (echo Install Node.js LTS.& pause & exit /b 1)
python -m venv backend\.venv
call backend\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
python scripts\generate_evaluation.py
python scripts\build_index.py
cd frontend
call npm install
cd ..
if not exist .env copy .env.example .env
echo Setup complete. Add a free Gemini key to .env, then run start_project.bat.
pause
