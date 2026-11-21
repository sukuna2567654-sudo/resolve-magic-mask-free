@echo off
set "DEST=C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Workflow Integration Plugins\MagicMaskFree"

echo Creating plugin directory...
mkdir "%DEST%" 2>nul
xcopy /E /I /Y "plugin\*" "%DEST%\"
copy /Y "requirements.txt" "%DEST%\"

echo Setting up Python virtual environment...
cd /d "%DEST%"
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

echo Done! Restart DaVinci Resolve and check Workspace ^> Workflow Integrations ^> Magic Mask Free.
pause
