import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][3];
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < 3; j++){
                arr[i][j] = sc.nextInt();
            }
        }
        
        boolean[][] check = new boolean[n][3];
        
        for(int j = 0; j < 3; j++){
            for(int i = 0; i < n; i++){
                for(int k = i + 1; k < n; k++){
                    if(arr[i][j] == arr[k][j]){
                        check[i][j] = true;
                        check[k][j] = true;
                    }
                }
            }
        }
        
        int[] sum = new int[n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < 3; j++){
                if(!check[i][j]){
                    sum[i] += arr[i][j];
                }
            }
        }
        
        for(int i = 0; i < n; i++){
            System.out.println(sum[i]);
        }
    }
}
