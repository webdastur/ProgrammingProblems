import java.util.Scanner;

public class Cf59a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input;

        int countCapitalLetter = 0, countLowerCaseLetter = 0;

        input = scanner.nextLine();

        for (int i = 0; i < input.length(); i++) {
            if ((int)input.charAt(i) >= 65 && (int)input.charAt(i) <= 90) {
                countCapitalLetter++;
            } else {
                countLowerCaseLetter++;
            }
        }

        if (countCapitalLetter > countLowerCaseLetter) {
            System.out.println(input.toUpperCase());
        } else {
            System.out.println(input.toLowerCase());
        }
    }
}