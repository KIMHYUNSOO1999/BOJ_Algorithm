import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int len = sc.nextInt();
        int[] arr = new int[len];
        boolean[] visited = new boolean[len];
        
        int n = sc.nextInt();

        int result1 = 1001;
        int num1 = -1;
        
        int result2 = 1001;
        int num2 = -1;
        
        for(int i = 1 ; i<= n ; i++){
            
            int start = sc.nextInt();
            int end = sc.nextInt();
        
            // 1
            int tmp = end-start+1;
            if (tmp > num1) {
                num1 = tmp;
                result1 = i;
            }

            // 2
            int tmp2 = 0;
            for(int j = start-1; j<=end-1 ; j++){
                if (!visited[j]){
                    tmp2++;
                    visited[j]=true;
                }
            }
            
            if (tmp2 > num2) {
                num2 = tmp2;
                result2 = i;
            }


        }

        System.out.println(result1);
        System.out.println(result2);
    }
}