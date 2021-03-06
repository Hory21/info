;15. Se dau cuvintele A si B. Se cere cuvantul C:
;- bitii 0-2 ai lui C au valoarea 0
;- bitii 3-5 ai lui C au valoarea 1
;- bitii 6-9 ai lui C coincid cu bitii 11-14 ai lui A
;- bitii 10-15 ai lui C coincid cu bitii 1-6 ai lui B

assume cs: code, ds: data
data segment
a dw 0110101001111111b
b dw 1111001011000100b
c dw ?
data ends
code segment
start:
mov ax, data
mov ds, ax
mov ax, 0 ; ax = 0 0 0 ...  0 0 0
or ax, 0038h; ax = 0 0 ... 0 1 1 1 0 0 0
mov bx, a; bx = a
mov cx, b; cx = b
ror bx, 5; bitii de pe pozitiile 11-14 din a sunt acum pe pozitiile 6-9 in bx
and bx, 03C0h; bx = 0 0 0 0 0 0 a14 a13 a12 a11 0 0 0 0 0 0
or ax, bx; ax = 0 0 0 0 0 0 a14 a13 a12 a11 1 1 1 0 0 0
rol cx, 9; bitii de pe pozitiile 1-6 din b sunt acum pe pozitiile 10-15 in cx
and cx, 0FC00h; cx = b6 b5 b4 b3 b2 b1 0 0 0 0 0 0 0 0 0 0
or ax, cx; ax = b6 b5 b4 b3 b2 b1 a14 a13 a12 a11 1 1 1 0 0 0
mov c, ax
mov ax, 4C00h
int 21h
code ends
end start
