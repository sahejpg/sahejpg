;;=============================================================
;; CS 2110 - Fall 2022
;; Homework 5 - fourCharacterStrings
;;=============================================================
;; Name: Sahej Panag
;;=============================================================


;; Pseudocode (see PDF for explanation)
;;
;; int count = 0;
;; int chars = 0;
;; int i = 0;
;;
;;  while(str[i] != '\0') {
;;      if (str[i] != ' ') 
;;          chars++;
;;      
;;      else {
;;          if (chars == 4) 
;;              count++;   
;;          chars = 0;
;;      }
;;      i++;
;;  }
;; ***IMPORTANT***
;; - Assume that all strings provided will end with a space (' ').
;; - Special characters do not have to be treated differently. For instance, strings like "it's" and "But," are considered 4 character strings.
;;

.orig x3000
AND R0, R0, 0		; R0 = count
AND R1, R1, 0		; R1 = chars
AND R2, R2, 0		; R2 = i
WHILE	LD R3, STRING
		ADD R3, R3, R2
		LDR R3, R3, 0		; R3 = str[i]
		BRz ENDWHILE

IF		LD R4, SPACE
		ADD R4, R3, R4
		BRz ELSE
		ADD R1, R1, 1
		BR CONT

ELSE	ADD R4, R1, -4
		BRnp SETCHAR
		ADD R0, R0, 1

SETCHAR	AND R1, R1, 0

CONT	ADD R2, R2, 1
		BR WHILE

ENDWHILE	ST R0, ANSWER

HALT


SPACE 	.fill #-32
STRING	.fill x4000
ANSWER .blkw 1

.end


.orig x4000

.stringz "I love CS 2110 and assembly is very fun! "

.end
