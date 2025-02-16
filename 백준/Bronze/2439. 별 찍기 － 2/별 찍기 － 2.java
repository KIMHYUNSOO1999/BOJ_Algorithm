import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 

public class Main {
    public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int cnt = Integer.parseInt(br.readLine());

        for( int i = 1 ; i <= cnt ; i ++ ){
            for( int j = 1; j <= cnt-i ; j ++ ){
               bw.write(" ");
            }      
            for( int k = 1 ; k <= i ; k ++ ){
                bw.write("*");
            }
            bw.write("\n");
        }

        bw.flush();
		bw.close();
		br.close();
    
    }
}