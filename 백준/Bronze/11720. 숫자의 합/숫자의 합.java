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

        int cnt = Integer.parseInt(br.readLine());
        String st = br.readLine();
        
        int answer = 0;
        for( int i = 0 ; i < cnt ; i ++ ){
            answer += Integer.parseInt(String.valueOf(st.charAt(i)));
        }

        bw.write(String.valueOf(answer));

        bw.flush();
		bw.close();
		br.close();
    
    }
}