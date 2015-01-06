;13. Dandu-se un sir de octeti si un subsir al sau, sa se elimine din primul
;sir toate aparitiile subsirului
assume cs:code, ds:data
data segment
  s db 1, 2, 3, 3, 2, 1, 1, 1, 2, 3, 3
    db 4, 3, 4, 3, 1, 2, 3, 1, 0, 0
  l = $ - s
  sb db 1, 2, 3
  lsb = $ - sb
  i dw 0
  j dw 0
data ends
code segment
start:
	mov ax, data
	mov ds, ax
	mov si, 0
	mov di, 0
	mov cl, 0
	repeat1:
		mov al, s[di]
 		mov ah, sb[si]
		cmp al, ah
		jne els
		repeat2:
			inc si
			mov bx, di
			add bx, si
			cmp bx, l
			jge els
			mov al, s[bx]
			cmp al, sb[si]
			jne els
			cmp si, lsb - 1
		jl repeat2
		mov i, di
		repeat3:
			mov bx, i
			mov dl, s[bx + lsb]
			mov s[bx], dl
			inc i
			cmp i, l - lsb
		jl repeat3
		;l = l - lsb
		inc cl
		sub di, 1
		els:
		mov si, 0
		inc di
		mov al, cl
		mov dx, lsb
		mul dl
		neg ax
		add ax, l
		cmp di, ax
	jle repeat1
	mov ax, 4c00h
	int 21h
code ends
end start
