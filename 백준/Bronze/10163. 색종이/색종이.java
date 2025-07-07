import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] visited = new int[1001][1001];
        
        for(int i=1;i<=n;i++){
            
            int x = sc.nextInt();
            int y = sc.nextInt();
            int w = sc.nextInt();
            int h = sc.nextInt();

            for(int j = x ; j < x+w ; j++){
                for(int k = y ; k < y+h ; k++)
                    visited[j][k] = i;
            }
        }

        for (int i = 1; i <= n; i++) {
            int count = 0;
            for (int j = 0; j < 1001; j++) {
                for (int k = 0; k < 1001; k++) {
                    if (visited[j][k] == i) count++;
                }
            }
            System.out.println(count);
        }
        
    }
}