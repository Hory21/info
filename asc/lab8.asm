;12. Sa se citeaca de la tastatura doua nume de fisiere. Sa se copieze primul
;fisier in cel de al doilea. Se va semnala orice situatie de eroare.
assume cs: code, ds: data
data segment
	s db 256 dup (?)
	len db 0
data ends
code segment
start:
	mov ax, data
	mov ds, ax
	
	mov ah, 0Ah
	lea dx, s
	mov s, 255
	int 21h ;am citit in s numele primului fisier
	mov ah, 3dh
	mov al, 0
	mov bx, dx
	mov di, bx[1]
	shl di, 8
	shr di, 8
	add di, bx
	mov [di + 2], "0"
	add dx, 2
	int 21h ;am deschis fisierul
	mov bx, ax
	mov cx, 250
	mov ah, 3fh
	int 21h ;am citit un buffer din fisier
	mov di, ax
	mov s[di + 2], '$'
	mov ah, 09h
	int 21h ;am afisat ce am citit

	mov ax, 4c00h
	int 21h
code ends
end start
