import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());  

        for (int i = 0 ; i < n ; i ++) {
            
            int n2 = Integer.parseInt(br.readLine());  

            int total = 0;
            int result = -1;
            int idx = -1;
            int cnt = 0;

            for (int j = 1 ; j <= n2 ; j++) {
                int temp = Integer.parseInt(br.readLine());
                total += temp;

                if (result < temp) {
                    result = temp;
                    idx = j;
                    cnt = 1;
                } else if (result == temp) {
                    cnt++;
                }
            }

            if (cnt > 1) {
                sb.append("no winner\n");
            } else {
                if (result > total / 2) {
                    sb.append("majority winner ").append(idx).append("\n");
                } else {
                    sb.append("minority winner ").append(idx).append("\n");
                }
            }
        }

        System.out.print(sb.toString());
    }
}
