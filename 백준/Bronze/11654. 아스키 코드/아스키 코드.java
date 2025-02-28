import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException; 
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        int answer= (int)s.charAt(0);
        
        System.out.println(answer);
        
        br.close();
        
    }
}