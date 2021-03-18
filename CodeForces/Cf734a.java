import java.util.Scanner;

public class Cf734a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int playNumber, dCount = 0, aCount = 0;
        String whoWon;

        playNumber = scanner.nextInt();
        whoWon = scanner.next();



        for (int i = 0; i < playNumber; i++) {
            if (whoWon.charAt(i) == 'A') {
                aCount++;
            } else {
                dCount++;
            }
        }

        if (aCount > dCount) {
            System.out.println("Anton");
        } else if (aCount == dCount) {
            System.out.println("Friendship");
        } else {
            System.out.println("Danik");
        }
    }
}