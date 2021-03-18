import java.util.Scanner;

public class Cf791a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a, b, count = 0;

        a = scanner.nextInt();
        b = scanner.nextInt();

        while (true) {
            count++;
            a = a * 3;
            b = b * 2;
            if (a > b) {
                System.out.println(count);
                break;
            }
        }
    }
}