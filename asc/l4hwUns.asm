;1. (a*a-b+7)/(2+a)
;a-byte b-doubleword
;interpretare FARA semn
assume cs: code, ds: data
data segment
a db 3
b dd 4
rez dw 0
data ends
code segment
start:
mov ax, data
mov ds, ax

mov al, a
mul al ;ax = a*a
mov dx, 0 ; dx:ax = a*a
sub ax, word ptr b
sbb dx, word ptr b + 2 ; dx:ax = a*a-b
add ax, 7
adc dx, 0 ; dx:ax = a*a-b+7
mov bl, a
mov bh, 0 ; bx = a
add bx, 2 ; bx = a+2
div bx; ax = (a*a-b+7)/(2+a)
mov rez, ax

mov ax, 4C00h
int 21h
code ends
end start
