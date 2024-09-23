@echo off
title ARPSPY
:menu
cls
echo ================================
echo          ARPSPY TOOL
echo ================================
echo 1. Netzwerk scannen
echo 2. Exit
echo ================================
set /p choice=Bitte wähle eine Option: 

if "%choice%"=="1" (
    call python check_internet_and_scan.py
    if errorlevel 1 (
        echo Keine Internetverbindung. Abbruch...
        pause
        exit
    ) else (
        pause
        goto menu
    )
) else if "%choice%"=="2" (
    exit
) else (
    echo Ungueltige Option!
    pause
    goto menu
)
