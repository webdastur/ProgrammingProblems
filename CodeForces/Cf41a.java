import java.util.Scanner;

public class Cf41a {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String t, s, reverse = "";

        s = scanner.nextLine();
        t = scanner.nextLine();

        for (int i = 0; i < s.length(); i++) {
            reverse = s.substring(i, i+1) + reverse;
        }

        if (reverse.equals(t)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}