import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
    
        // Integer
        int answer = A + B - C;
        bw.write(String.valueOf(answer)+"\n");

        // String
        answer = Integer.parseInt(String.valueOf(A)+String.valueOf(B))-C;
        bw.write(String.valueOf(answer));
        
        bw.flush();
		bw.close();
		br.close();
    
    }
}