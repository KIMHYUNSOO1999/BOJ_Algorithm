import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] h = new int[n];
        for(int i = 0; i < n; i++) h[i] = sc.nextInt();

        int result = 0;
        
        for(int i = 0; i < n; i++){
            
            int start = h[i];
            int tmp = 0;
            
            for(int j = i+1; j < n; j++){
                
                int end = h[j];
                
                if (start > end) {
                    tmp++;
                } else {
                    break;
                }
            }

            if(result < tmp) result = tmp;
        
            } 
        
        System.out.println(result);
    }
}