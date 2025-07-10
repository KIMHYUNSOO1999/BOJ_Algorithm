import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        s = s.replaceAll(" ", "");
        
        int[] result = new int[2];
        
        for(int i = 0; i < s.length(); i++){
            if (i + 3 <= s.length()) {
                String tmp = s.substring(i,i+3);

                if(tmp.equals(":-)")){
                    result[0]+=1;
                }
                else if(tmp.equals(":-(")){
                    result[1]+=1;
                }
            }
        }

        if(result[0]==0 && result[1]==0){
            System.out.println("none");
        }
        else if(result[0]>result[1]){
            System.out.println("happy");
        }
        else if(result[0]<result[1]){
            System.out.println("sad ");
        }
        else{
            System.out.println("unsure");
        }
        
    }
}