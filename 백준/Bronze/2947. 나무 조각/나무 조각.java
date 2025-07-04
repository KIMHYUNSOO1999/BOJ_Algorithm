import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = 5;
        int arr[] = new int[5];
        for(int i = 0; i < n; i++) arr[i] = sc.nextInt();

        boolean flag  = false;
        while (!flag) {
            flag = true;
            int tmp = 0;
            for(int i = 0; i< n-1 ; i++){
                if(arr[i]>arr[i+1]) {
                    tmp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = tmp;
    
                    for(int j = 0; j < n; j++){
                        System.out.print(arr[j] +" ");
                    }
                    System.out.println();
                    flag = false;
                    }
                }
            }
        }
    }