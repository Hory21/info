;1. (a*a-b+7)/(2+a)
;a-byte b-doubleword
;interpretare CU semn
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
imul al ;ax = a*a
cwd; dx:ax = a*a
sub ax, word ptr b
sbb dx, word ptr b + 2 ; dx:ax = a*a-b
add ax, 7
adc dx, 0 ; dx:ax = a*a-b+7
mov bx, ax ; dx:bx = a*a-b+7
mov al, a
cbw ; ax = a
add ax, 2 ; ax = a+2
xchg ax, bx; dx:ax = a*a-b+7, bx = a+2
idiv bx; ax = (a*a-b+7)/(2+a)
mov rez, ax

mov ax, 4C00h
int 21h
code ends
end start
