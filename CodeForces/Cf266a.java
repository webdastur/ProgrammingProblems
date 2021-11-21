package CodeForces;

import java.util.Scanner;

public class Cf266a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String input = scanner.next();
        int counter = 0;
        char first = input.charAt(0);
        for (int i = 1; i < n; i++) {
            if (input.charAt(i) == first) counter++;
            else first = input.charAt(i);
        }
        System.out.println(counter);
    }
}