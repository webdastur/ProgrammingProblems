package Algorithms;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SelectionSort {
    public static void main(String[] args) {
        System.out.println(selectionSort(new ArrayList<>(Arrays.asList(10, 5, 9, 7, 3, 8, 4, 1, 6, 2))));
    }

    public static List<Integer> selectionSort(List<Integer> array) {
        List<Integer> sortedArray = new ArrayList<>();
        int index;
        int size = array.size();
        for (int i = 0; i < size; i++) {
            index = findSmallest(array);
            sortedArray.add(array.get(index));
            array.remove(index);
        }
        return sortedArray;
    }

    public static int findSmallest(List<Integer> array) {
        int smallest = array.get(0);
        int smallestIndex = 0;
        for (int i = 0; i < array.size(); i++) {
            if (array.get(i) < smallest) {
                smallestIndex = i;
                smallest = array.get(smallestIndex);
            }
        }
        return smallestIndex;
    }
}
