package CodeForces;

import java.util.Scanner;

public class Cf271a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a, b, c, d;
        int year;
        year = scanner.nextInt();
        while (true) {
            year++;
            a = year / 1000;
            b = year / 100 % 10;
            c = year / 10 % 10;
            d = year % 10;
            if (a != b && a != c && a != d && b != c && b != d && c != d) {
                break;
            }
        }
        System.out.println(year);
    }
}