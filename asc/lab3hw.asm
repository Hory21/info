; enunt: (h+128)-(yy+m+d)

assume cs: code, ds: data
data segment
m db 4
h dw 185
yy dw 95
d db 1
rez dw 0
data ends
code segment
start:
mov ax, data
mov ds, ax

mov dx, h
add dx, 128 ; dx = h + 128 (acum, in dx se afla rezultatul primei paranteze)
mov rez, dx ; rez = h + 128
mov al, m
mov ah, 0
mov dx, ax ; dx = m
mov al, d
cbw
add dx, ax ; dx = m + d
add dx, yy ; dx = m + d + yy (acum, in dx se afla rezultatul celei de-a
		; doua paranteze)
sub rez, dx ; rez = (h + 128) - (m + d + yy)

mov ax, 4C00h
int 21h
code ends
end start
