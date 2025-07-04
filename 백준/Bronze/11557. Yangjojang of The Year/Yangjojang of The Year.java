import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i=0; i<n; i++){
            
            int m = sc.nextInt();
            int tmp = 0;
            String result = "";
            
            for(int j=0;j<m;j++){
                
                String a = sc.next();
                int b = sc.nextInt();

                if(b>tmp){
                    result = a;
                    tmp = b;
                }
                
            }
            System.out.println(result);
        }
    }
}