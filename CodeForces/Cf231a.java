import java.util.ArrayList;
import java.util.Scanner;

public class Cf231a {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<ArrayList> list = new ArrayList<>();
        int rowCount = 0, counter = 0;
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            ArrayList<Integer> integers = new ArrayList<>();
            for (int j = 0; j < 3; j++) {
                integers.add(scanner.nextInt());
            }
            list.add(integers);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < list.get(i).size(); j++) {
                if ((int) list.get(i).get(j) == 1) {
                    counter++;
                }
            }
            if (counter >= 2) {
                rowCount++;
                counter = 0;
            } else {
                counter = 0;
            }
        }
        System.out.println(rowCount);

    }
}