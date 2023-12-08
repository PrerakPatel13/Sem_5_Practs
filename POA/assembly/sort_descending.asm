
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

DATA SEGMENT
    N1 DB 10h,14h,7h,8h,98h,19h,34h,5h  
    SIZE equ $ - N1 
ENDS

CODE SEGMENT
    START:
    MOV AX,DATA
    MOV DS,AX
    
    MOV CH,SIZE
    L1:
    LEA SI,N1
    MOV CL,SIZE
    
    L2:
    
    MOV AL, [SI] 
    MOV BL, [SI+1]
    CMP AL,BL
    JNC DOWN
    MOV DL,[SI+1]
    XCHG [SI],DL
    MOV [SI+1],DL
    
    DOWN:
    INC SI
    DEC CL
    JNZ L2
    
    DEC CH
    JNZ L1
    
CODE ENDS    
END START

ret




