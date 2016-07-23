@echo off
cls
set ECLIPSE_PATH="C:\Devlit\eclipse\cpp-neon\eclipse\"
set PROJECT_PATH="C:\Workspaces"
:: Comment
echo User: %UserName%
echo Eclipse Path: %ECLIPSE_PATH%
echo Project Path: %PROJECT_PATH%
%ECLIPSE_PATH%eclipsec.exe -nosplash -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data %PROJECT_PATH% -build Sample/Release 
echo .
pause