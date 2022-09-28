;;=============================================================
;; CS 2110 - Fall 2022
;; Homework 5 - summation
;;=============================================================
;; Name: Sahej Panag
;;=============================================================

;; Pseudocode (see PDF for explanation)
;;
;;    int result; (to save the summation of x)
;;    int x= -9; (given integer)
;;    int answer = 0;
;;    while (x > 0) {
;;        answer += x;
;;        x--;
;;    }
;;    result = answer;
.orig x3000
    
LD R2, x
AND R3, R3, 0
LOOP    ADD R2, R2, 0
        BRnz END
        ADD R3, R3, R2
        ADD R2, R2, -1
        BR LOOP
END     ST R3, result
HALT

x .fill -9
result .blkw 1
.end

