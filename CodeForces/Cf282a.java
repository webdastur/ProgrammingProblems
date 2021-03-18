import java.util.ArrayList;
import java.util.Scanner;

public class Cf282a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        int n = scanner.nextInt(), x = 0;
        String input = "";
        for (int i = 0; i <= n; i++) {
            input = scanner.nextLine();
            if (input.equals("X++")) {
                x++;
            }
            if (input.equals("++X")) {
                x++;
            }
            if (input.equals("X--")) {
                x--;
            }
            if (input.equals("--X")) {
                x--;
            }
        }

        System.out.println(x);
    }
}