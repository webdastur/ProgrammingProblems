package CodeForces;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

// A. Twins
public class CF160A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        byte n = scanner.nextByte();
        short sum = 0;
        short count = 0;
        short twinSum = 0;
        ArrayList<Byte> a = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            a.add(scanner.nextByte());
            sum += a.get(a.size() - 1);
        }
        a.sort(Collections.reverseOrder());
        for (Byte aByte : a) {
            twinSum += aByte;
            count++;
            if ((sum / 2) < twinSum) {
                break;
            }
        }
        System.out.println(count);
    }
}
