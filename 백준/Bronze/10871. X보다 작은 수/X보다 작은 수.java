import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException; 
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int N = Integer.parseInt(st.nextToken());
        int std = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
		st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
        
		for (int i = 0; i < N; i++) {
			if (arr[i] < std) {
				System.out.print(arr[i] + " ");
			}
		}
    
    }
}