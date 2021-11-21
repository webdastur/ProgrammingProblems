package CodeForces;

import java.util.Scanner;

// A. Magnets
public class Cf344a {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[] magnets = new int[n];

        for (int i = 0; i < n; i++) {
            magnets[i] = scanner.nextInt();
        }

        int groupsCount = 1;

        for (int i = 0; i < n-1; i++) {
            if (magnets[i] != magnets[i + 1]) {
                ++groupsCount;
            }
        }
        System.out.println(groupsCount);
    }
}
