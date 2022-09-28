import java.util.Comparator;
import java.util.LinkedList;
import java.util.Random;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Your implementation of various sorting algorithms.
 *
 * @author Sahej Panag
 * @version 1.0
 * @userid spanag3
 * @GTID 903604843
 *
 * Collaborators: None
 *
 * Resources: None
 */
public class Sorting {

    /**
     * Implement insertion sort.
     * <p>
     * It should be:
     * in-place
     * stable
     * adaptive
     * <p>
     * Have a worst case running time of:
     * O(n^2)
     * <p>
     * And a best case running time of:
     * O(n)
     *
     * @param <T>        data type to sort
     * @param arr        the array that must be sorted after the method runs
     * @param comparator the Comparator used to compare the data in arr
     * @throws java.lang.IllegalArgumentException if the array or comparator is
     *                                            null
     */
    public static <T> void insertionSort(T[] arr, Comparator<T> comparator) {
        if (arr == null || comparator == null) {
            throw new IllegalArgumentException("Values passed in equal null");
        }
        for (int i = 1; i < arr.length; i++) {
            int innerLoop = i;
            while (innerLoop > 0 && comparator.compare(arr[innerLoop], arr[innerLoop - 1]) < 0) {
                T temp = arr[innerLoop];
                arr[innerLoop] = arr[innerLoop - 1];
                arr[innerLoop - 1] = temp;
                innerLoop--;
            }
        }
    }

    /**
     * Implement cocktail sort.
     * <p>
     * It should be:
     * in-place
     * stable
     * adaptive
     * <p>
     * Have a worst case running time of:
     * O(n^2)
     * <p>
     * And a best case running time of:
     * O(n)
     * <p>
     * NOTE: See pdf for last swapped optimization for cocktail sort. You
     * MUST implement cocktail sort with this optimization
     *
     * @param <T>        data type to sort
     * @param arr        the array that must be sorted after the method runs
     * @param comparator the Comparator used to compare the data in arr
     * @throws java.lang.IllegalArgumentException if the array or comparator is
     *                                            null
     */
    public static <T> void cocktailSort(T[] arr, Comparator<T> comparator) {
        if (arr == null || comparator == null) {
            throw new IllegalArgumentException("Values passed in equal null");
        }
        boolean toSort = true;
        int startInd = 0;
        int endInd = arr.length - 1;
        while (toSort) {
            toSort = false;
            int tempStart = startInd;
            int tempEnd = endInd;
            for (int i = tempStart; i < tempEnd; i++) {
                if (comparator.compare(arr[i], arr[i + 1]) > 0) {
                    T temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    toSort = true;
                    endInd = i;
                }
            }
            if (toSort) {
                toSort = false;
                tempStart = startInd;
                tempEnd = endInd;
                for (int i = tempEnd; i > tempStart; i--) {
                    if (comparator.compare(arr[i], arr[i - 1]) < 0) {
                        T temp = arr[i];
                        arr[i] = arr[i - 1];
                        arr[i - 1] = temp;
                        toSort = true;
                        startInd = i;
                    }
                }
            }
        }
    }

    /**
     * Implement merge sort.
     * <p>
     * It should be:
     * out-of-place
     * stable
     * not adaptive
     * <p>
     * Have a worst case running time of:
     * O(n log n)
     * <p>
     * And a best case running time of:
     * O(n log n)
     * <p>
     * You can create more arrays to run merge sort, but at the end, everything
     * should be merged back into the original T[] which was passed in.
     * <p>
     * When splitting the array, if there is an odd number of elements, put the
     * extra data on the right side.
     * <p>
     * Hint: If two data are equal when merging, think about which subarray
     * you should pull from first
     *
     * @param <T>        data type to sort
     * @param arr        the array to be sorted
     * @param comparator the Comparator used to compare the data in arr
     * @throws java.lang.IllegalArgumentException if the array or comparator is
     *                                            null
     */
    public static <T> void mergeSort(T[] arr, Comparator<T> comparator) {
        if (arr == null || comparator == null) {
            throw new IllegalArgumentException("Values passed in equal null");
        }
        if (arr.length == 1 || arr.length == 0) {
            return;
        }
        int middle = arr.length / 2;
        T[] left = (T[]) (new Object[middle]);
        T[] right = (T[]) (new Object[arr.length - left.length]);
        for (int i = 0; i < middle; i++) {
            left[i] = arr[i];
        }
        for (int i = middle; i < arr.length; i++) {
            right[i - middle] = arr[i];
        }
        mergeSort(left, comparator);
        mergeSort(right, comparator);
        int x = 0;
        int y = 0;
        while (x < left.length && y < right.length) {
            if (comparator.compare(left[x], right[y]) <= 0) {
                arr[x + y] = left[x];
                x++;
            } else {
                arr[x + y] = right[y];
                y++;
            }
        }
        while (x < left.length) {
            arr[x + y] = left[x];
            x++;
        }
        while (y < right.length) {
            arr[x + y] = right[y];
            y++;
        }
    }

    /**
     * Implement quick sort.
     * <p>
     * Use the provided random object to select your pivots. For example if you
     * need a pivot between a (inclusive) and b (exclusive) where b > a, use
     * the following code:
     * <p>
     * int pivotIndex = rand.nextInt(b - a) + a;
     * <p>
     * If your recursion uses an inclusive b instead of an exclusive one,
     * the formula changes by adding 1 to the nextInt() call:
     * <p>
     * int pivotIndex = rand.nextInt(b - a + 1) + a;
     * <p>
     * It should be:
     * in-place
     * unstable
     * not adaptive
     * <p>
     * Have a worst case running time of:
     * O(n^2)
     * <p>
     * And a best case running time of:
     * O(n log n)
     * <p>
     * Make sure you code the algorithm as you have been taught it in class.
     * There are several versions of this algorithm and you may not receive
     * credit if you do not use the one we have taught you!
     *
     * @param <T>        data type to sort
     * @param arr        the array that must be sorted after the method runs
     * @param comparator the Comparator used to compare the data in arr
     * @param rand       the Random object used to select pivots
     * @throws java.lang.IllegalArgumentException if the array or comparator or
     *                                            rand is null
     */
    public static <T> void quickSort(T[] arr, Comparator<T> comparator,
                                     Random rand) {
        if (arr == null || comparator == null || rand == null) {
            throw new IllegalArgumentException("Values passed in equal null");
        }
        quickSortHelper(arr, 0, arr.length, comparator, rand);
    }

    /**
     * Helper method to recursively sort.
     *
     * @param <T>        data type to sort
     * @param arr        the array to be sorted
     * @param start      the index to start sorting from
     * @param end        the index to end at
     * @param comparator to compare values
     * @param rand       the pivot val
     */
    private static <T> void quickSortHelper(T[] arr, int start, int end, Comparator<T> comparator,
                                            Random rand) {
        if ((end - start) < 1) {
            return;
        }
        int pivotIndex = rand.nextInt(end - start) + start;
        T pivot = arr[pivotIndex];
        arr[pivotIndex] = arr[start];
        arr[start] = pivot;
        int i = start + 1;
        int j = end - 1;
        while (i <= j) {
            while (i <= j && comparator.compare(pivot, arr[i]) >= 0) {
                i++;
            }
            while (i <= j && comparator.compare(pivot, arr[j]) <= 0) {
                j--;
            }
            if (i <= j) {
                T temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
        T temp = arr[j];
        arr[j] = arr[start];
        arr[start] = temp;
        quickSortHelper(arr, start, j, comparator, rand);
        quickSortHelper(arr, j + 1, end, comparator, rand);
    }

    /**
     * Implement LSD (least significant digit) radix sort.
     * <p>
     * Make sure you code the algorithm as you have been taught it in class.
     * There are several versions of this algorithm and you may not get full
     * credit if you do not implement the one we have taught you!
     * <p>
     * Remember you CANNOT convert the ints to strings at any point in your
     * code! Doing so may result in a 0 for the implementation.
     * <p>
     * It should be:
     * out-of-place
     * stable
     * not adaptive
     * <p>
     * Have a worst case running time of:
     * O(kn)
     * <p>
     * And a best case running time of:
     * O(kn)
     * <p>
     * You are allowed to make an initial O(n) passthrough of the array to
     * determine the number of iterations you need. The number of iterations
     * can be determined using the number with the largest magnitude.
     * <p>
     * At no point should you find yourself needing a way to exponentiate a
     * number; any such method would be non-O(1). Think about how how you can
     * get each power of BASE naturally and efficiently as the algorithm
     * progresses through each digit.
     * <p>
     * Refer to the PDF for more information on LSD Radix Sort.
     * <p>
     * You may use ArrayList or LinkedList if you wish, but it may only be
     * used inside radix sort and any radix sort helpers. Do NOT use these
     * classes with other sorts. However, be sure the List implementation you
     * choose allows for stability while being as efficient as possible.
     * <p>
     * Do NOT use anything from the Math class except Math.abs().
     *
     * @param arr the array to be sorted
     * @throws java.lang.IllegalArgumentException if the array is null
     */
    public static void lsdRadixSort(int[] arr) {
        if (arr == null) {
            throw new IllegalArgumentException("Array passed in is null");
        }
        LinkedList<Integer>[] buckets = (LinkedList<Integer>[]) new LinkedList[19];
        int k = 1;
        boolean toSort = true;
        while (toSort) {
            toSort = false;
            for (int i = 0; i < arr.length; i++) {
                int currDigit = arr[i] / k;
                if (currDigit / 10 != 0) {
                    toSort = true;
                }
                if (buckets[currDigit % 10 + 9] == null) {
                    buckets[currDigit % 10 + 9] = new LinkedList<Integer>();
                }
                buckets[currDigit % 10 + 9].add(arr[i]);
            }
            int index = 0;
            for (LinkedList<Integer> bucket : buckets) {
                if (bucket != null) {
                    while (bucket.size() != 0) {
                        arr[index] = bucket.removeFirst();
                        index++;
                    }
                }
            }
            k = k * 10;
        }
    }

    /**
     * Implement heap sort.
     * <p>
     * It should be:
     * out-of-place
     * unstable
     * not adaptive
     * <p>
     * Have a worst case running time of:
     * O(n log n)
     * <p>
     * And a best case running time of:
     * O(n log n)
     * <p>
     * Use java.util.PriorityQueue as the heap. Note that in this
     * PriorityQueue implementation, elements are removed from smallest
     * element to largest element.
     * <p>
     * Initialize the PriorityQueue using its build heap constructor (look at
     * the different constructors of java.util.PriorityQueue).
     * <p>
     * Return an int array with a capacity equal to the size of the list. The
     * returned array should have the elements in the list in sorted order.
     *
     * @param data the data to sort
     * @return the array with length equal to the size of the input list that
     * holds the elements from the list is sorted order
     * @throws java.lang.IllegalArgumentException if the data is null
     */
    public static int[] heapSort(List<Integer> data) {
        if (data == null) {
            throw new IllegalArgumentException("Data passed in is null");
        }
        PriorityQueue<Integer> backingArray = new PriorityQueue<>(data);
        int[] toReturn = new int[data.size()];
        for (int i = 0; i < toReturn.length; i++) {
            toReturn[i] = backingArray.remove();
        }
        return toReturn;
    }
}