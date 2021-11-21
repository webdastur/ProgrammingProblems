package Algorithms;

public class BinarySearch {
    public static void main(String[] args) {
        int[] list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        System.out.println(binarySearch(list, 6));
        System.out.println(binarySearch(list, 11));
    }

    public static int binarySearch(int[] list, int item) {
        int low, high, mid, guess;
        low = 0;
        high = list.length - 1;
        while (low <= high) {
            mid = (low + high) / 2;
            guess = list[mid];
            if (guess == item)
                return mid;
            if (guess > item)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return -1;
    }
}
