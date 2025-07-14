import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        Set<String> set = new HashSet<>();

        for (int i = 1; i <= n; i++) {
            String password = sc.next();
            StringBuffer sb = new StringBuffer(password);
            String reverse = sb.reverse().toString();

            set.add(password);

            if(set.contains(reverse)){
                int middle = password.length() / 2;
                System.out.println(password.length() + " " + password.charAt(middle));
            }
        }
    }
}