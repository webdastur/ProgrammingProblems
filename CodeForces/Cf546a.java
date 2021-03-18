import java.util.Scanner;

public class Cf546a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int k, n, w, totalPrice = 0;

        k = scanner.nextInt();
        n = scanner.nextInt();
        w = scanner.nextInt();

        for (int i = 1; i <= w; i++) {
            totalPrice += k * i;
        }

        if (n - totalPrice > 0) {
            System.out.println(0);
        } else {
            System.out.println(totalPrice - n);
        }

    }
}