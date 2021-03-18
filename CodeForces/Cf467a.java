import java.util.Scanner;

public class Cf467a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n, p, q, count = 0;
        n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            p = scanner.nextInt();
            q = scanner.nextInt();

            if (q - p >=2) {
                count++;
            }
        }

        System.out.println(count);

    }
}