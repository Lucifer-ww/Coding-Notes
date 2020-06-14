main PROC
    mov eax, 5               ;将数字 5 送入 eax 寄存器
    add eax, 6               ;eax 寄存器加 6
    INVOKE ExitProcess, 0    ;程序结束
main ENDP