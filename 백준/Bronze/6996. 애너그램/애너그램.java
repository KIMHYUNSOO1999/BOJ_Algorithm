import java.util.*;
import java.lang.*;
import java.io.*;

class Main {

    public static boolean CheckAlpha(String str1, String str2){
        
        if ( str1.length() != str2.length()) return false;

        char[] a = str1.toCharArray();
        char[] b = str2.toCharArray();

        Arrays.sort(a);
        Arrays.sort(b);

        return Arrays.equals(a, b);
        
    }
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        
        for(int i = 0; i < n; i++){
            String tmp = sc.nextLine();
            String[] line = tmp.split(" ");

            String a = line[0];
            String b = line[1];

            if (CheckAlpha(a, b)) {
                System.out.printf("%s & %s are anagrams.\n", a, b);
            } else {
                System.out.printf("%s & %s are NOT anagrams.\n", a, b);
            }
        }
    }
}