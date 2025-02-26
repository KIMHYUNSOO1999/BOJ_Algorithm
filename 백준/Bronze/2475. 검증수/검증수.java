import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException; 
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int answer = 0;
        int tmp = 0;
        
        while (st.hasMoreTokens()) {
            tmp=Integer.parseInt(st.nextToken());
            answer+=tmp*tmp;
        }

        System.out.println(answer%10);
        
		br.close();
    
    }
}