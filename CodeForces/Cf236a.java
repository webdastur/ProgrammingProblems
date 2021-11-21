package CodeForces;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Cf236a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input;
        Set<Character> charList = new HashSet<>();
        input = scanner.nextLine();
        for (int i = 0; i < input.length(); i++) {
            charList.add(input.charAt(i));
        }
        if (charList.size()%2==0) {
            System.out.println("CHAT WITH HER!");
        } else {
            System.out.println("IGNORE HIM!");
        }
    }
}