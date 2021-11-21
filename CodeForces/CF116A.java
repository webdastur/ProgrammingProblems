package CodeForces;

import java.util.Scanner;

// A. Tram
public class CF116A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        short numberOfStops = scanner.nextShort();
        int maxCapacity = 0;
        int sum = 0;
        for (int i = 0; i < numberOfStops; i++) {
            short exits, enters;
            exits = scanner.nextShort();
            enters = scanner.nextShort();
            sum -= exits;
            sum += enters;
            if (maxCapacity < sum)
                maxCapacity = sum;
        }
        System.out.println(maxCapacity);
    }
}
