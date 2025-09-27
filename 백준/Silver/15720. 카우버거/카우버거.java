import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        Integer[] burger = new Integer[A];
        Integer[] side   = new Integer[B];
        Integer[] drink  = new Integer[C];

        String[] input = br.readLine().split(" ");
        for (int i = 0; i < burger.length; i++) {
            burger[i] = Integer.parseInt(input[i]);
        }

        input = br.readLine().split(" ");
        for (int i = 0; i < side.length; i++) {
            side[i] = Integer.parseInt(input[i]);
        }

        input = br.readLine().split(" ");
        for (int i = 0; i < drink.length; i++) {
            drink[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(burger, Collections.reverseOrder());
        Arrays.sort(side, Collections.reverseOrder());
        Arrays.sort(drink, Collections.reverseOrder());

        int maxLength = Math.max(burger.length, Math.max(side.length, drink.length));
        double result1 = 0;
        double result2 = 0;
        
        for (int i = 0; i < maxLength; i++) {
            int b = i < burger.length ? burger[i] : 0;
            int s = i < side.length ? side[i] : 0;
            int d = i < drink.length ? drink[i] : 0;
        
            double temp = b + s + d;  
            result1 += temp;
            
            if (b != 0 && s != 0 && d != 0) {
                temp *= 0.9;  
            }
            result2 += temp;
        }

        bw.write((int)result1 + "\n");
        bw.write((int)result2 + "\n");

        bw.flush();
        bw.close();
    }
}