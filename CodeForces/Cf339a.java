package CodeForces;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Cf339a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String outputString = "", inputString = scanner.nextLine();
        ArrayList<Character> numList = new ArrayList<>();
        if (inputString.length() > 1) {
            for (int i = 0; i < inputString.length(); i++) {
                if (i % 2 == 0) {
                    numList.add(inputString.charAt(i));
                }
            }
        } else {
            outputString = inputString;
        }
        Collections.sort(numList);
        for (Character character : numList) {
            outputString = outputString + "+" + character;
        }
        outputString = outputString.replaceFirst("\\+", "");
        System.out.println(outputString);
    }
}