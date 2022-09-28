;;=============================================================
;; CS 2110 - Fall 2021
;; Homework 6 - Factorial
;;=============================================================
;; Name: Sahej Panag
;;============================================================

;; In this file, you must implement the 'factorial' and "mult" subroutines.

;; Little reminder from your friendly neighborhood 2110 TA staff: don't run
;; this directly by pressing 'RUN' in complx, since there is nothing put at
;; address x3000. Instead, load it and use 'Debug' -> 'Simulate
;; Subroutine Call' and choose the 'factorial' or 'mult' label.

;; Pseudocode

;; Factorial

;;    factorial(int n) {
;;        int ret = 1;
;;        for (int x = 2; x < n+1; x++) {
;;            ret = mult(ret, x);
;;        }
;;        return ret;
;;    }

;; Multiply
         
;;    mult(int a, int b) {
;;        int ret = 0;
;;        int copyB = b;
;;        while (copyB > 0):
;;            ret += a;
;;            copyB--;
;;        return ret;
;;    }


.orig x3000
    ;; you do not need to write anything here
HALT

factorial   ;; please do not change the name of your subroutine
    ;; insert your implementation for factorial subroutine


    ADD R6, R6, -4              ; allocate space
    STR R7, R6, 2               ; store return address
    STR R5, R6, 1               ; store old frame pointer
    ADD R5, R6, 0               ; frame pointer set to stack pointer
    ADD R6, R6, -5              ; allocate space for registers
    STR R0, R6, 4
    STR R1, R6, 3
    STR R2, R6, 2
    STR R3, R6, 1
    STR R4, R6, 0

    LDR R0, R5, 4               ; R0 <- FIRST ARG = n

    AND R1, R1, 0               ; R1 = ret
    ADD R1, R1, 1

    AND R2, R2, 0               ; R2 = x
    ADD R2, R2, 1

FOR ADD R2, R2, 1
    ADD R3, R0, 1
    NOT R3, R3
    ADD R3, R3, 1               ; R3 = -(n+1)
    ADD R3, R2, R3
    BRzp ENDFOR
    
    ADD R6, R6, -1
    STR R2, R6, 0               ; push(x)
    ADD R6, R6, -1
    STR R1, R6, 0               ; push(ret)
    
    JSR mult
    
    ;; after mult returns
    LDR R1, R6, 0               ; R1 = rv from mult subroutine
    STR R1, R5, 0               ; local variable = ret
    ADD R6, R6, 3               ; pop(RV, x, ret)
    BR FOR

ENDFOR  NOP

TEARDOWN
    STR R1, R5, 3               ; RV = R1 = ret
    LDR R4, R5, -5              ; Restore R4
    LDR R3, R5, -4              ; Restore R3
    LDR R2, R5, -3              ; Restore R2
    LDR R1, R5, -2              ; Restore R1
    LDR R0, R5, -1              ; Restore R0

    ADD R6, R5, 0               ; restore stack pointer
    LDR R5, R6, 1               ; restore old frame pointer
    LDR R7, R6, 2               ; restore old return address
    ADD R6, R6, 3               ; pop(RA, FP, 1st local variable)
                                ; R6 points to return value

    RET
    
mult        ;; please do not change the name of your subroutine
    ;; insert your implementation for mult subroutine

    ADD R6, R6, -4              ; allocate space
    STR R7, R6, 2
    STR R5, R6, 1
    ADD R5, R6, 0
    ADD R6, R6, -5
    STR R0, R6, 4
    STR R1, R6, 3
    STR R2, R6, 2
    STR R3, R6, 1
    STR R4, R6, 0

    LDR R0, R5, 4               ; A <- R0
    LDR R1, R5, 5               ; B <- R1

    AND R2, R2, 0               ; R2 <- RET
    STR R2, R5, 0
    AND R3, R3, 0               ; R3 <- COPYB
    ADD R3, R1, 0

WLOOP   ADD R3, R3, 0
        BRnz ENDWHILE
        ADD R2, R2, R0
        ADD R3, R3, -1
        BR WLOOP

ENDWHILE   NOP

TEARDOWNN
    STR R2, R5, 3               ; RV = R2 = ret
    LDR R4, R5, -5              ; Restore R4
    LDR R3, R5, -4              ; Restore R3
    LDR R2, R5, -3              ; Restore R2
    LDR R1, R5, -2              ; Restore R1
    LDR R0, R5, -1              ; Restore R0

    ADD R6, R5, 0               ; restore stack pointer
    LDR R5, R6, 1               ; restore old frame pointer
    LDR R7, R6, 2               ; restore old return address
    ADD R6, R6, 3               ; pop(RA, FP, 1st local variable)
                                ; R6 points to return value

RET

STACK .fill xF000
.end
