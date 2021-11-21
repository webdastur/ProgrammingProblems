package CodeForces;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Cf158a {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n, k, count = 0;
        n = scanner.nextInt();
        k = scanner.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(scanner.nextInt());
        }
        for (int i = 0; i < n; i++) {
            if (list.get(i) > 0 && list.get(i) >= list.get(k - 1))
                count++;
        }
        System.out.println(count);
    }
}
