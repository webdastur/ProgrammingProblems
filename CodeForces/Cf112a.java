import java.util.Scanner;

public class Cf112a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String firstString, secondString;
        int counter = 0;
        firstString = scanner.nextLine();
        secondString = scanner.nextLine();

        while (true) {
            if (firstString.toLowerCase().charAt(counter) < secondString.toLowerCase().charAt(counter)) {
                System.out.println(-1);
                break;
            } else if (firstString.toLowerCase().charAt(counter) > secondString.toLowerCase().charAt(counter)) {
                System.out.println(1);
                break;
            }
            if (counter == firstString.length()-1) {
                System.out.println(0);
                break;
            }
            counter++;
        }
    }
}