
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV AX,0ffffh
MOV BX,00099h
MOV CL,00h
ADD AX,BX
MOV DX,AX
JNC carry
INC CL
carry:  
mov [1006h], cl
HLT

ret




