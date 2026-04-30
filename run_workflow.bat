@echo off
echo Dang cai dat thu vien Pillow...
pip install Pillow
if %errorlevel% neq 0 (
    echo Khong the cai dat Pillow. Vui long kiem tra Python/pip.
    pause
    exit /b
)

echo Dang gop anh thanh PDF...
python merge_to_pdf.py
if %errorlevel% neq 0 (
    echo Loi khi gop anh.
    pause
    exit /b
)

echo Dang chuyen doi PDF sang Markdown...
call C:\tools\markitdown-0.1.5\run_markitdown.bat "%cd%\Tai_Lieu_Gop.pdf"

echo Da hoan thanh! Kiem tra file Tai_Lieu_Gop.md.
pause
