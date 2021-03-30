import java.util.Scanner;

// A. Nearly Lucky Number
public class CF110A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String n = scanner.next();
        int count = 0;
        for (int i = 0; i < n.length(); i++)
            if (n.charAt(i) == '4' || n.charAt(i) == '7')
                count++;
        if (count == 7 || count == 4)
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}
