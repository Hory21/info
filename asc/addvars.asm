assume cs:code, ds:data
data segment
    a db 5
    b db 7
    c db 0
data ends
code segment
start:
    mov ax, data
    mov ds, ax

    mov ah, a
    add ah, b
    mov c, ah

    mov ax, 4c00h
    int 21h
code ends
end start 
