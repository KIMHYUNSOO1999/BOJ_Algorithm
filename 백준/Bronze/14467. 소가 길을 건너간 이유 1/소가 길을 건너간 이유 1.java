import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        Map<Integer, Integer> last = new HashMap<>();
        int result = 0;

        for (int i = 0; i < n; i++) {
            int cow = sc.nextInt();
            int pos = sc.nextInt();

            if (!last.containsKey(cow)) {
                last.put(cow, pos); 
            } else {
                if (last.get(cow) != pos) {
                    result++; 
                    last.put(cow, pos);
                }
            }
        }

        System.out.println(result);
    }
}