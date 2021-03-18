import java.util.Scanner;

public class Cf486a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        long n;

        n = scanner.nextLong();
        f(n);
    }

    public static void f(long n) {
        if (n % 2 == 0) {
            System.out.println(n/2);
        } else {
            System.out.println((n-1)/2-n);
        }
    }
}