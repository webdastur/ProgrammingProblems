import java.util.Scanner;

// A. Presents
public class CF136A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextByte();
        int[] friends = new int[n+1];
        for (int i = 1; i <= n; i++) {
            friends[scanner.nextByte()] = i;
        }
        StringBuilder result = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            result.append(friends[i]);
            result.append(" ");
        }
        System.out.println(result.toString().trim());
    }
}
