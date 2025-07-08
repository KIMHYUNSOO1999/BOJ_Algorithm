import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();

        ArrayList<Integer> xArr = new ArrayList<>(Arrays.asList(0, x));
        ArrayList<Integer> yArr = new ArrayList<>(Arrays.asList(y, 0));
        
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            if(a==0) yArr.add(b);
            else xArr.add(b);
        }

        Collections.sort(xArr);
        Collections.sort(yArr);

        int maxX = -1;
        for(int i = 0; i < xArr.size() - 1; i++) {
    		int dis = xArr.get((i+1)) - xArr.get(i); 
        	maxX = Math.max(maxX, dis); 
    	}
        
        int maxY = -1;
        for(int i = 0; i < yArr.size() - 1; i++) {
    		int dis = yArr.get((i+1)) - yArr.get(i);
    		maxY = Math.max(maxY, dis); 
    	}
        
        System.out.println(maxX * maxY);
    }
}