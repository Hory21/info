data segment
a db 5, b[0]
b dw 55, c[1]
c dd 1, 2, 3
data ends
code segment
start:
mov ax, 4c00h
int 21h
code ends
end start
