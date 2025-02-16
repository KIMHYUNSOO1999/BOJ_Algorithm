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

        int Cnt = Integer.parseInt(br.readLine());

        int h,w,n= 0;
        for( int i = 0 ; i < Cnt ; i++){
            
            StringTokenizer arr = new StringTokenizer(br.readLine(), " ");

            h = Integer.parseInt(arr.nextToken());
            w = Integer.parseInt(arr.nextToken());
            n = Integer.parseInt(arr.nextToken());

            if( n % h == 0 ){
                bw.write(String.valueOf(h*100 + (n/h)) + "\n");      
            }
            else{
                bw.write(String.valueOf((n%h*100) + (n/h)+1) + "\n");    
            }
            
        }
        
        bw.flush();
		bw.close();
		br.close();
    
    }
}