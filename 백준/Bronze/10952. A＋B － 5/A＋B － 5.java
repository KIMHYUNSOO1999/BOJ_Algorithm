import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException; 
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String str;
        
        while( (str=br.readLine()) != null ){
            
			st = new StringTokenizer(str, " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(a+b==0){
                 break;   
            }
            else{
                System.out.println(a+b);
            }
            
		}

        br.close();
        
    }
}