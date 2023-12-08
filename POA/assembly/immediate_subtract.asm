
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h


MOV AX,5656H
MOV BX,345FH
MOV CL,00h
SUB AX,BX
MOV DX,AX
JNC jump
INC CL
NOT AX
ADD AX,0001h
jump:
HLT

ret




