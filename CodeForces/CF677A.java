package CodeForces;

import java.util.Scanner;

// A. Vanya and Fence
public class CF677A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        short n, h, width = 0;
        n = scanner.nextShort();
        h = scanner.nextShort();
        for (int i = 0; i < n; i++) {
            short temp = scanner.nextShort();
            if (temp < h) {
                width += 1;
            } else if (temp > h) {
                width += 2;
            } else {
                width += 1;
            }
        }
        System.out.println(width);
    }
}
