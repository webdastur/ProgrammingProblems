import java.util.Scanner;

// B. Taxi
public class CF158B {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += input.nextInt();
        }
        int result = sum % 4 > 0 ? (sum / 4) + 1 : (sum / 4);
        System.out.println(result);
    }
}
