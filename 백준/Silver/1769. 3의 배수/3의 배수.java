import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        String s = sc.next();
        int count = 0;

        while (s.length() > 1) {
            
            int tmp = 0;
            for(String ch : s.split("")){
                tmp += Integer.parseInt(ch);
            }
            
            s = String.valueOf(tmp);
            count++;
        }

        String result = "";
        if(Integer.parseInt(s)%3==0){
            result = "YES";
        }
        else{
            result = "NO";
        }

        System.out.println(count);
        System.out.println(result);
    }
}