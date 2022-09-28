;;=============================================================
;; CS 2110 - Fall 2021
;; Homework 6 - Quick Sort
;;=============================================================
;; Name: Sahej Panag
;;============================================================

;; In this file, you must implement the 'quicksort' and 'partition' subroutines.

;; Little reminder from your friendly neighborhood 2110 TA staff: don't run
;; this directly by pressing 'RUN' in complx, since there is nothing put at
;; address x3000. Instead, load it and use 'Debug' -> 'Simulate
;; Subroutine Call' and choose the 'quicksort' or 'partition' label.


;; Pseudocode:

;; Partition

;;    partition(int[] arr, int low, int high) {
;;        int pivot = arr[high];
;;        int i = low - 1;
;;        for (j = low; j < high; j++) {
;;            if (arr[j] < pivot) {
;;                i++;
;;                int temp = arr[j];
;;                arr[j] = arr[i];
;;                arr[i] = temp;
;;            }
;;        }
;;        int temp = arr[high];
;;        arr[high] = arr[i + 1];
;;        arr[i + 1] = temp;
;;        return i + 1;
;;    }
        
;; Quicksort

;;    quicksort(int[] arr, int left, int right) {
;;        if (left < right) {
;;            int pi = partition(arr, left, right);
;;            quicksort(arr, left, pi - 1);
;;            quicksort(arr, pi + 1, right);
;;        }
;;    }


.orig x3000
    ;; you do not need to write anything here
HALT

partition   ;; please do not change the name of your subroutine
    
    ADD R6, R6, -4              ; allocate space
    STR R7, R6, 2               ; store return address
    STR R5, R6, 1               ; store old frame pointer
    ADD R5, R6, 0               ; frame pointer set to stack pointer
    ADD R6, R6, -8              ; allocate space for registers
    STR R0, R6, 4
    STR R1, R6, 3
    STR R2, R6, 2
    STR R3, R6, 1
    STR R4, R6, 0

    AND R0, R0, 0
    AND R1, R1, 0
    AND R2, R2, 0
    AND R3, R3, 0
    AND R4, R4, 0


    LDR R0, R5, 4               ; first arg = address of arr = R0
    LDR R1, R5, 5               ; int low = R1
    LDR R2, R5, 6               ; int high = R2

    ADD R4, R0, R2              ; R4 = address of (arr[high])
    LDR R4, R4, 0               ; R4 = arr[high] = pivot
    STR R4, R5, 0               ; store 1st local variable = pivot at R5 
    AND R3, R3, 0
    ADD R3, R1, -1              ; R3 = i = low - 1
    STR R3, R5, -1              ; store 2nd local variable = i at R5-1

    ADD R4, R1, 0               ; R4 = j
    STR R4, R5, -2              ; store 3rd local variable = j at R5-2

WHILE   LDR R4, R5, -2          ; R4 = j
        NOT R3, R4
        ADD R3, R3, 1           ; R3 = -j
        ADD R3, R2, R3           ; R3 = high - j
        BRnz ENDWHILE

        ADD R3, R0, R4          ; R3 = address of arr[j]
        LDR R3, R3, 0           ; R3 = arr[j]
        LDR R4, R5, 0           ; R4 = pivot
        NOT R3, R3
        ADD R3, R3, 1           ; R3 = -arr[j]
        ADD R4, R4, R3          ; R4 = pivot - arr[j]
        BRnz ENDIF

        IF  LDR R4, R5, -1      ; LOAD i into R4
            ADD R4, R4, 1       ; i++
            STR R4, R5, -1      ; store i at R5-1

            LDR R4, R5, -2      ; R4 = j
            ADD R4, R0, R4      ; R4 = address of arr[j]
            LDR R3, R4, 0       ; R3 = arr[j] = temp
            STR R3, R5, -3      ; store 4th local variable temp at R5-3

            LDR R3, R5, -1      ; R3 = i
            ADD R3, R0, R3      ; R3 = address of arr[i]
            LDR R3, R3, 0       ; R3 = arr[i]
            STR R3, R4, 0       ; arr[j] = arr[i]

            LDR R3, R5, -1      ; R3 = i
            ADD R3, R0, R3      ; R3 = address of arr[i]
            LDR R4, R5, -3      ; R4 = temp
            STR R4, R3, 0       ; arr[i] = temp

ENDIF   LDR R4, R5, -2      ; R4 = j
        ADD R4, R4, 1       ; j++
        STR R4, R5, -2

        BR WHILE
        
ENDWHILE    ADD R3, R0, R2      ; R3 = address of arr[high]
            LDR R3, R3, 0       ; R3 = arr[high]
            STR R3, R5, -3      ; temp = arr[high]

            ADD R3, R0, R2      ; address of arr[high]
            LDR R4, R5, -1      ; R4 = i
            ADD R4, R4, 1       ; R4 = i + 1
            ADD R4, R4, R0      ; R4 = address of arr[i + 1]
            LDR R4, R4, 0       ; R4 = arr[i + 1]
            STR R4, R3, 0       ; address of arr[high] = arr[i + 1]

            LDR R4, R5, -1      ; R4 = i
            ADD R4, R4, 1       ; R4 = i + 1
            ADD R4, R4, R0      ; R4 = address of arr[i + 1]
            LDR R3, R5, -3      ; R3 = temp
            STR R3, R4, 0       ; address of arr[i + 1] = temp

            LDR R4, R5, -1
            ADD R4, R4, 1
            STR R4, R5, 3       ; RV = i + 1

TEARDOWN    LDR R0, R6, 4       ; restore R0
            LDR R1, R6, 3       ; restore R1
            LDR R2, R6, 2
            LDR R3, R6, 1
            LDR R4, R6, 0

            ADD R6, R5, 0       ; restore stack pointer
            LDR R5, R6, 1       ; restore frame pointer
            LDR R7, R6, 2       ; restore return address
            ADD R6, R6, 3       ; pop RA, FP, local var


    RET

quicksort   ;; please do not change the name of your subroutine
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

    LDR R0, R5, 4               ; first arg = address of arr = R0
    LDR R1, R5, 5               ; int left = R1
    LDR R2, R5, 6               ; int right = R2

    EEF NOT R3, R1
        ADD R3, R3, 1           ; R3 = -left
        ADD R3, R3, R2          ; R3 = right - left
        BRnz END

        ADD R6, R6, -1
        STR R2, R6, 0
        ADD R6, R6, -1
        STR R1, R6, 0
        ADD R6, R6, -1
        STR R0, R6, 0

        JSR partition

        LDR R3, R6, 0           ; R3 = partition() = pi
        ADD R6, R6, 4           ; pop

        ADD R4, R3, -1          ; R4 = pi - 1

        ADD R6, R6, -1
        STR R4, R6, 0
        ADD R6, R6, -1
        STR R1, R6, 0
        ADD R6, R6, -1
        STR R0, R6, 0

        JSR quicksort

        ADD R6, R6, 4
        ADD R4, R3, 1           ; R4 = pi + 1

        ADD R6, R6, -1
        STR R2, R6, 0
        ADD R6, R6, -1
        STR R4, R6, 0
        ADD R6, R6, -1
        STR R0, R6, 0

        JSR quicksort

        ADD R6, R6, 4

END     NOP

TEAR        LDR R0, R6, 4       ; restore R0
            LDR R1, R6, 3       ; restore R1
            LDR R2, R6, 2
            LDR R3, R6, 1
            LDR R4, R6, 0

            ADD R6, R5, 0       ; restore stack pointer
            LDR R5, R6, 1       ; restore frame pointer
            LDR R7, R6, 2       ; restore return address
            ADD R6, R6, 3       ; pop RA, FP, local var        

    RET

STACK .fill xF000
.end


;; Assuming the array starts at address x4000, here's how the array [1,3,2,5] represents in memory
;; Memory address           Data
;; x4000                    1
;; x4001                    3
;; x4002                    2
;; x4003                    5
