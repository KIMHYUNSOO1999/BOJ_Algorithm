import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i = 0; i < n; i++) {
            
          int[] A = new int[4];                   
          int[] B = new int[4];                 
          String result = "D";    
            
          int a = sc.nextInt();
          for(int j = 0; j < a; j++) A[sc.nextInt()-1]++; 
            
          int b = sc.nextInt();
          for(int j = 0; j < b; j++) B[sc.nextInt()-1]++;
            
          for(int j = 3; j >=0; j--) {
              
            if(A[j] > B[j]) {
              result = "A";
              break;
            }
              
            else if(A[j] < B[j]) {
              result = "B";
              break;
            }
          }
          System.out.println(result);
        }
    }
}