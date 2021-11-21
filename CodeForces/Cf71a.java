package CodeForces;

import java.util.ArrayList;
import java.util.Scanner;

public class Cf71a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> wordList = new ArrayList<>();
        int n = scanner.nextInt();
        for (int i = 0; i <= n; i++) {
            wordList.add(scanner.nextLine());
        }
        for (int i = 1; i <= n; i++) {
            if (wordList.get(i).length()>10) {
                String start = wordList.get(i).substring(0, 1);
                String end = wordList.get(i).substring(wordList.get(i).length() - 1, wordList.get(i).length());
                System.out.println(start + String.valueOf(wordList.get(i).length() - 2) + end);
            } else {
                System.out.println(wordList.get(i));
            }
        }
    }
}