package CodeForces;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

// A. Chat room
public class CF58A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> s = new ArrayList<>(Arrays.asList(scanner.next().split("")));
        ArrayList<String> words = new ArrayList<>(Arrays.asList("hello".split("")));
        StringBuilder result = new StringBuilder();
        for (String value : s) {
            if (words.isEmpty())
                break;
            if (words.get(0).equals(value)) {
                words.remove(value);
                result.append(value);
            }
        }
        System.out.println(result.toString().equals("hello") ? "YES" : "NO");
    }
}
