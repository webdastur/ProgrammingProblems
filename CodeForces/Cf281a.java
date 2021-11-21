package CodeForces;

import java.util.Scanner;

public class Cf281a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine();
        char letter;
        if ((int) inputString.charAt(0) >= 65 && (int) inputString.charAt(0) <= 90) {
            System.out.println(inputString);
        } else {
            letter = inputString.charAt(0);
            inputString = inputString.replaceFirst(String.valueOf(letter), "");
            letter = (char) ((int) letter - 32);
            inputString = letter + inputString;
            System.out.println(inputString);
        }
    }
}