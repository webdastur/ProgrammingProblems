import java.util.Scanner;

public class Cf4a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int weight = scanner.nextInt();
        if (weight > 2 && weight % 2 == 0) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}