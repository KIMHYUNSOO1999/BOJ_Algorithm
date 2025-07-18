import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next(); 
        String b = sc.next();

        int crossCol = -1; 
        int crossRow = -1;

        boolean flag = true;
        
        for (int i = 0; i < a.length(); i++) {
            
            if(flag == false) break;
            
            for (int j = 0; j < b.length(); j++) {
                if (a.charAt(i) == b.charAt(j)) {
                    crossCol = i;
                    crossRow = j;
                    flag = false;
                    break;
                }
            }
        }

        for (int i = 0; i < b.length(); i++) {
            for (int j = 0; j < a.length(); j++) {
                if (i == crossRow) {
                    System.out.print(a.charAt(j));
                } else if (j == crossCol) {
                    System.out.print(b.charAt(i));
                } else {
                    System.out.print(".");
                }
            }
            System.out.println();
        }
    }
}
