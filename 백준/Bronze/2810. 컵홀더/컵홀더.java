import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = sc.next();

        int result = 1;
        for(int i = 0; i < n; i++){
            if(s.charAt(i) == 'S'){
                result++;
            }
            else{
                result++;
                i++;
            }
        }

        if (result > n) result = n;
        System.out.println(result);

    }
}