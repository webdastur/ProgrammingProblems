package CodeForces;

import java.util.Scanner;

public class Cf617a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x, count = 5, totalMove = 0;

        x = scanner.nextInt();
        if (x == 0) {
            System.out.println(0);
        } else {
            while (x > 0) {
                if (x - count >= 0) {
                    totalMove += 1;
                    x -= count;
                } else {
                    count--;
                }
            }
        }

        System.out.println(totalMove);

    }
}