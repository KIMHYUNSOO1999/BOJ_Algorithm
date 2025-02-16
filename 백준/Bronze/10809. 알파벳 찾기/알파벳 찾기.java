import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException; 

public class Main {
    public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[26];
        for( int i = 0; i < arr.length ; i++ ){
            arr[i] = -1;
        }

        String S = br.readLine();
        for( int i = 0 ; i < S.length(); i++){
            char tmp = S.charAt(i);

            if(arr[tmp-'a'] == -1){
                arr[tmp-'a'] = i;
            }
        }

        for( int i = 0 ; i < arr.length ; i++){
            bw.write(String.valueOf(arr[i]) + " ");
        }        
        
        bw.flush();
		bw.close();
		br.close();
    
    }
}