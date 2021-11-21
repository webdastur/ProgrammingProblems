package CodeForces;

import java.util.Scanner;

public class Cf263a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int r = 0, c = 0;
        int[][] num = new int[5][5];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                num[i][j] = scanner.nextInt();
            }
        }
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (num[i][j] == 1) {
                    r = i + 1;
                    c = j + 1;
                    break;
                }
            }
        }
        System.out.println(Math.abs(3 - r) + Math.abs(3 - c));
    }
}