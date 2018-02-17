@ECHO OFF
CD /d %~dp0
chk_image_dup.exe -a -s %1

PAUSE
