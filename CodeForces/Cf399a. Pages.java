import java.util.Scanner;

public class Cf399a {
    public static void main(String[] args) {
        int n, p, k;
        String outputL = "";
        String outputR = "";
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        p = scanner.nextInt();
        k = scanner.nextInt();

        if ((n >= 3) && (n <= 100) && (p >= 1) && (p <= n) && (1 <= k && k <= n)) {
            if (p - k > 1) {
                outputL += "<< ";
                for (int i = p - k; i < p; i++) {
                    outputL = outputL + i + " ";
                }
            } else {
                for (int i = 1; i < p; i++) {
                    outputL = outputL + i + " ";
                }
            }
            if (p + k < n) {
                for (int i = p + 1; i <= p + k; i++) {
                    outputR = outputR + i + " ";
                }
                outputR += ">>";
            } else {
                for (int i = p + 1; i <= n; i++) {
                    outputR = outputR + i + " ";
                }
            }
            outputL = outputL + "(" + p + ") " + outputR;
        }
        if (!outputL.isEmpty()) System.out.println(outputL.trim());
    }
}
