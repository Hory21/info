assume cs: code, ds: data
data segment
  m   db 4
  h   db 191
  yy  db 95
  d   db 1
  rez dw 0
data ends
code segment
start:
  mov ax, data
  mov ds, ax
  
  mov al, h
  mov ah, 0
  add ax, 128
  mov rez, ax

  mov dl, yy
  mov dh, 0
  mov bl, m
  mov bh, 0
  add dx, bx
  mov bl, d
  mov bh, 0
  add dx, bx

  add ax, dx
  mov rez, ax

  mov ax, 4c00h
  int 21h
code ends
end start
