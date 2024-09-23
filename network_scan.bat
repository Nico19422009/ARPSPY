@echo off
echo Scanning the network...
for /L %%i in (1,1,254) do (
    ping -n 1 -w 100 192.168.1.%%i | find "Reply" >nul
    if not errorlevel 1 (
        echo 192.168.1.%%i is online
        arp -a 192.168.1.%%i
    )
)
pause
