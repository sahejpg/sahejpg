import java.util.ArrayList;
import java.util.NoSuchElementException;

/**
 * Your implementation of a MinHeap.
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
public class MinHeap<T extends Comparable<? super T>> {

    /**
     * The initial capacity of the MinHeap when created with the default
     * constructor.
     *
     * DO NOT MODIFY THIS VARIABLE!
     */
    public static final int INITIAL_CAPACITY = 13;

    // Do not add new instance variables or modify existing ones.
    private T[] backingArray;
    private int size;

    /**
     * Constructs a new MinHeap.
     *
     * The backing array should have an initial capacity of INITIAL_CAPACITY.
     */
    public MinHeap() {
        backingArray = (T[]) (new Comparable[INITIAL_CAPACITY]);
    }

    /**
     * Creates a properly ordered heap from a set of initial values.
     *
     * You must use the BuildHeap algorithm that was taught in lecture! Simply
     * adding the data one by one using the add method will not get any credit.
     * As a reminder, this is the algorithm that involves building the heap
     * from the bottom up by repeated use of downHeap operations.
     *
     * Before doing the algorithm, first copy over the data from the
     * ArrayList to the backingArray (leaving index 0 of the backingArray
     * empty). The data in the backingArray should be in the same order as it
     * appears in the passed in ArrayList before you start the BuildHeap
     * algorithm.
     *
     * The backingArray should have capacity 2n + 1 where n is the
     * number of data in the passed in ArrayList (not INITIAL_CAPACITY).
     * Index 0 should remain empty, indices 1 to n should contain the data in
     * proper order, and the rest of the indices should be empty.
     *
     * @param data a list of data to initialize the heap with
     * @throws java.lang.IllegalArgumentException if data or any element in data
     *                                            is null
     */
    public MinHeap(ArrayList<T> data) {
        if (data == null) {
            throw new IllegalArgumentException("The data of passed arraylist is null");
        }
        backingArray = (T[]) (new Comparable[data.size() * 2 + 1]);
        int counter = 1;
        for (int i = 0; i < data.size(); i++) {
            if (data.get(i) == null) {
                throw new IllegalArgumentException("data value at" + i + "was null");
            }
            backingArray[counter] = data.get(i);
            counter++;
            size++;
        }
        for (int loc = size / 2; loc > 0; loc--) {
            downHeap(loc);
        }
    }

    /**
     * The BuildHeap algorithm to add items to heap.
     *
     * @param loc the location
     */
    private void downHeap(int loc) {
        if (loc * 2 <= size) {
            int cL = loc * 2;
            int cR = loc * 2 + 1;
            if (loc <= size / 2) {
                if (backingArray[cL] != null && backingArray[cR] != null) {
                    if (backingArray[cL].compareTo(backingArray[cR]) > 0) {
                        if (backingArray[loc].compareTo(backingArray[cR]) > 0) {
                            T temp = backingArray[cR];
                            backingArray[cR] = backingArray[loc];
                            backingArray[loc] = temp;
                            downHeap(cR);
                        }
                    } else if (backingArray[cL].compareTo(backingArray[cR]) < 0) {
                        if (backingArray[loc].compareTo(backingArray[cL]) > 0) {
                            T temp = backingArray[cL];
                            backingArray[cL] = backingArray[loc];
                            backingArray[loc] = temp;
                            downHeap(cL);
                        }
                    }
                } else {
                    if (backingArray[cL] != null) {
                        if (backingArray[loc].compareTo(backingArray[cL]) > 0) {
                            T temp = backingArray[cL];
                            backingArray[cL] = backingArray[loc];
                            backingArray[loc] = temp;
                            downHeap(cL);
                        }
                    }
                }
            }
        }
    }

    /**
     * Adds an item to the heap. If the backing array is full (except for
     * index 0) and you're trying to add a new item, then double its capacity.
     * The order property of the heap must be maintained after adding.
     * 
     * @param data the data to add
     * @throws java.lang.IllegalArgumentException if data is null
     */
    public void add(T data) {
        if (data == null) {
            throw new IllegalArgumentException("data passed in is equal to null"
                    + "and cannot be added to the heap");
        }
        if (size == backingArray.length - 1) {
            resize();
        }
        if (size == 0) {
            backingArray[1] = data;
        } else {
            backingArray[size + 1] = data;
            int loc = size + 1;
            heapify(loc);
        }
        size++;
    }

    /**
     * Helper method to add new data in order.
     *
     * @param loc the starting point
     */
    private void heapify(int loc) {
        int parent = loc / 2;
        if (loc != 1) {
            if (backingArray[parent].compareTo(backingArray[loc]) > 0) {
                T temp = backingArray[loc];
                backingArray[loc] = backingArray[parent];
                backingArray[parent] = temp;
                heapify(parent);
            }
        }
    }

    /**
     * Resize helper method for when heap is out of space.
     *
     */
    private void resize() {
        T[] temp = (T[]) (new Comparable[backingArray.length * 2]);
        for (int i = 1; i < backingArray.length; i++) {
            temp[i] = backingArray[i];
        }
        backingArray = temp;
    }

    /**
     * Removes and returns the min item of the heap. As usual for array-backed
     * structures, be sure to null out spots as you remove. Do not decrease the
     * capacity of the backing array.
     * The order property of the heap must be maintained after adding.
     *
     * @return the data that was removed
     * @throws java.util.NoSuchElementException if the heap is empty
     */
    public T remove() {
        if (size == 0) {
            throw new NoSuchElementException("The heap is empty cannot remove anything");
        }
        T toReturn;
        if (size == 1) {
            toReturn = backingArray[1];
            backingArray[1] = null;
            size = 0;
        } else {
            toReturn = getMin();
            backingArray[1] = backingArray[size];
            backingArray[size] = null;
            downHeap(1);
            size--;
        }
        return toReturn;
    }

    /**
     * Returns the minimum element in the heap.
     *
     * @return the minimum element
     * @throws java.util.NoSuchElementException if the heap is empty
     */
    public T getMin() {
        if (size == 0) {
            throw new NoSuchElementException("heap is empty, there is no min element");
        }
        return backingArray[1];
    }

    /**
     * Returns whether or not the heap is empty.
     *
     * @return true if empty, false otherwise
     */
    public boolean isEmpty() {
        return (size == 0);
    }

    /**
     * Clears the heap.
     *
     * Resets the backing array to a new array of the initial capacity and
     * resets the size.
     */
    public void clear() {
        backingArray = (T[]) (new Comparable[INITIAL_CAPACITY]);
        size = 0;
    }

    /**
     * Returns the backing array of the heap.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the backing array of the list
     */
    public T[] getBackingArray() {
        // DO NOT MODIFY THIS METHOD!
        return backingArray;
    }

    /**
     * Returns the size of the heap.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the size of the list
     */
    public int size() {
        // DO NOT MODIFY THIS METHOD!
        return size;
    }
}
