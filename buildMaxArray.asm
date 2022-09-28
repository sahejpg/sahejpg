;;=============================================================
;; CS 2110 - Fall 2022
;; Homework 5 - buildMaxArray
;;=============================================================
;; Name: Sahej Panag
;;=============================================================


;; Pseudocode (see PDF for explanation)
;;
;;	int A[] = {1,2,3};
;;	int B[] = {-1, 7, 8};
;;	int C[3];
;;
;;	int i = 0;
;;
;;	while (i < A.length) {
;;		if (A[i] < B[i])
;;			C[i] = B[i];
;;		else
;;			C[i] = A[i];
;;
;;		i += 1;
;;	}


.orig x3000
AND R0, R0, 0				; R0 = i

WHILE	LD R1, LEN			; R1 = length OF A
		NOT R2, R0
		ADD R2, R2, 1		; R2 = -(i)
		ADD R2, R1, R2
		BRnz ENDWHILE

		LD R1, A
		ADD R1, R1, R0		; R1 = ADDRESS OF A[i]
		LDR R1, R1, 0		; R1 = A[i]
		LD R2, B
		ADD R2, R2, R0		; R2 = ADDRESS OF B[i]
		LDR R2, R2, 0		; R2 = B[i]

		NOT R3, R1
		ADD R3, R3, 1		; -A[i]
		ADD R3, R3, R2
		BRnz ELSE

		LD R3, C
		ADD R3, R3, R0		; R3 = ADDRESS OF C[i]
		STR R2, R3, 0		; C[i] = B[i]
		BR CONTINUE			

ELSE	LD R3, C
		ADD R3, R3, R0
		STR R1, R3, 0		; C[i] = A[i]
		
CONTINUE	ADD R0, R0, 1
			BR WHILE
ENDWHILE

HALT


A 	.fill x3200
B 	.fill x3300
C 	.fill x3400
LEN .fill 4

.end

.orig x3200
	.fill -1
	.fill 2
	.fill 7
	.fill -3
.end

.orig x3300
	.fill 3
	.fill 6
	.fill 0
	.fill 5
.end

.orig x3400
	.blkw 4
.end


