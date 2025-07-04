import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int arr[] = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int start = arr[0];
        int result = 0;
        
        for(int i = 1; i < n; i++) {
            if (arr[i] > arr[i - 1]) {
                int diff = arr[i] - start;
                if (diff > result) {
                    result = diff;
                }
            } else {
                start = arr[i];
            }
        }

        System.out.println(result);

    }
}