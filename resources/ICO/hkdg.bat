@echo off&mode con cols=100 lines=80&color 02
set m=1&set v=1
set code==^^^&%%%^:!$#^>^<:=~*()@"'`;\|-_+?,.ghijklmnopqrstuvwxyz0123456789abcdef
setlocal enabledelayedexpansion
:begin
set /a num=%random%%%40+1,num1=num,num=200/num
title ??????????????%num1%
:lp
set /a a=%random%%%63,b=%random%%%%num%
set a=!code:~%a%,1!
if %b% equ 0 (set "b=!a!") else (set "b= ") 
set str%m%=!str%m%!!b!
set /a n+=1
if %n% lss 40 goto lp
set /a x+=1,w+=1
if %x% equ 40 call :lop
cls&for /l %%i in (%m%,-1,%v%) do echo.!str%%i!
set /a m+=1
if %m% geq 20 set /a v+=1
if %w% equ 100 (set w=0&goto begin) else (set n=0&goto lp)
:lop
set /a a=%random%%%15+1
set a=!code:~-%a%,1!
color 0!a!&set x=0

