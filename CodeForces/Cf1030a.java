package CodeForces;

import java.util.Scanner;

public class Cf1030a {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        byte n = scanner.nextByte();

        byte result = 0;

        for (int i = 0; i < n; i++) {
            if (scanner.nextByte() == 1) {
                result = 1;
                break;
            }
        }

        if (result == 1)
            System.out.println("HARD");
        else
            System.out.println("EASY");
    }
}
