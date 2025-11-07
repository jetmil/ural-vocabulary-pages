@echo off
chcp 65001 >nul
echo.
echo ════════════════════════════════════════════════════
echo   АВТОМАТИЧЕСКОЕ КОПИРОВАНИЕ КАРТИНОК И ПУБЛИКАЦИЯ
echo ════════════════════════════════════════════════════
echo.

cd /d "%~dp0"

echo Проверяю наличие картинок...
echo.

set "missing=0"

if not exist "images\veksha.jpg" (
    echo ❌ НЕТ: images\veksha.jpg
    set "missing=1"
)
if not exist "images\baskoj.jpg" (
    echo ❌ НЕТ: images\baskoj.jpg
    set "missing=1"
)
if not exist "images\malakhitnitsa.jpg" (
    echo ❌ НЕТ: images\malakhitnitsa.jpg
    set "missing=1"
)
if not exist "images\posikunchiki.jpg" (
    echo ❌ НЕТ: images\posikunchiki.jpg
    set "missing=1"
)
if not exist "images\khrenovina.jpg" (
    echo ❌ НЕТ: images\khrenovina.jpg
    set "missing=1"
)
if not exist "images\shanga.jpg" (
    echo ❌ НЕТ: images\shanga.jpg
    set "missing=1"
)
if not exist "images\hero-ural-mountains.jpg" (
    echo ❌ НЕТ: images\hero-ural-mountains.jpg
    set "missing=1"
)

if "%missing%"=="1" (
    echo.
    echo ════════════════════════════════════════════════════
    echo   ВНИМАНИЕ! Сначала добавьте картинки:
    echo ════════════════════════════════════════════════════
    echo.
    echo Положите файлы в папку: images\
    echo.
    echo Список нужных файлов:
    echo   1. veksha.jpg               (белка)
    echo   2. baskoj.jpg               (девушка в костюме)
    echo   3. malakhitnitsa.jpg        (малахитовая пещера)
    echo   4. posikunchiki.jpg         (пирожки)
    echo   5. khrenovina.jpg           (хреновина)
    echo   6. shanga.jpg               (шаньги)
    echo   7. hero-ural-mountains.jpg  (фон для hero)
    echo.
    pause
    exit /b 1
)

echo ✅ Все картинки найдены!
echo.
echo Публикую на GitHub...
echo.

git add .
git commit -m "Add project images and author signature - site complete"
git push origin main

echo.
echo ════════════════════════════════════════════════════
echo   ✅ ГОТОВО! Сайт обновлен
echo ════════════════════════════════════════════════════
echo.
echo Сайт будет доступен через 1-2 минуты:
echo https://jetmil.github.io/ural-vocabulary-pages/
echo.
pause
