import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

// B. Queue at the School
public class CF266B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        short n, t;
        n = scanner.nextShort();
        t = scanner.nextShort();
        ArrayList<String> s = new ArrayList<>(Arrays.asList(scanner.next().split("")));
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < t; i++) {
            for (int j = 1; j < n; j++) {
                if (s.get(j - 1).equals("B") && s.get(j).equals("G")) {
                    Collections.swap(s, j - 1, j);
                    ++j;
                }
            }
        }
        s.forEach(result::append);
        System.out.println(result.toString());
    }
}
