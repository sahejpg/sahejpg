;;=============================================================
;; CS 2110 - Fall 2022
;; Homework 5 - binaryStringToInt
;;=============================================================
;; Name: SAHEJ PANAG
;;=============================================================

;; Pseudocode (see PDF for explanation)
;;
;;    int result = x4000; (given memory address to save the converted value)
;;    String binaryString= "01000000"; (given binary string)
;;    int length = 8; (given length of the above binary string)
;;    int base = 1;
;;    int value = 0;
;;    while (length > 0) {
;;        int y = binaryString.charAt(length - 1) - 48;
;;        if (y == 1) {
;;            value += base;
;;        }     
;;            base += base;
;;            length--;
;;    }
;;    mem[result] = value;
.orig x3000
    
LD R0, length       ; R0 = length
AND R1, R1, 0       
ADD R1, R1, 1       ; R1 = BASE, BASE = 1
AND R2, R2, 0       ; R2 = VALUE = 0

WHILE   ADD R0, R0, 0
        BRnz ENDWHILE       ; branch if length =< 0

        ADD R3, R0, -1      ; R3 = length - 1
        LD R4, binaryString 
        ADD R4, R4, R3      ; R4 = ADDRESS OF CHARACTER
        LDR R3, R4, 0       ; R3 = ascii of char
        LD R4, val
        NOT R4, R4
        ADD R4, R4, 1
        ADD R3, R3, R4     ; R3 = y

IF      BRz ENDIF
        ADD R2, R2, R1

ENDIF   ADD R1, R1, R1
        ADD R0, R0, -1
        BR WHILE

ENDWHILE    STI R2, result

HALT

    binaryString .fill x5000
    length .fill 8
    result .fill x4000
    val .fill x0030
.end 

.orig x5000
    .stringz "010010100"
.end
