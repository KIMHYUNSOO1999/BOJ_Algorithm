import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        sc.nextLine();

        char[][] arr = new char[h][w];
        for (int i = 0; i < h; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < w; j++) {
                arr[i][j] = line.charAt(j);
            }
        }
        
        int[][] visited = new int[h][w];
        for (int i = 0; i < h; i++) {
            Arrays.fill(visited[i], -1);
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (arr[i][j] == 'c') {
                    visited[i][j] = 0; 
                } else if (j > 0 && visited[i][j - 1]!=-1) {
                    visited[i][j] = visited[i][j - 1]+1;
                } else {
                    visited[i][j]=-1; 
                }
            }
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                System.out.print(visited[i][j] + " ");
            }
            System.out.println();
        }
        
        
    }
}