import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        input.nextLine();
        
        for ( int i = 0 ; i < n ; i++ ){
            
            String line = input.nextLine();    
            String[] tmp = line.split(" ");
            int x = Integer.parseInt(tmp[0]);
            int y = Integer.parseInt(tmp[1]);
            int result = 0;

            for( int j = x ; j <= y ; j++ ){ 
               for(int k = 0 ; k < String.valueOf(j).length() ; k++){
                    if(String.valueOf(j).charAt(k) == '0'){
                        result++;
                    }
                }
            }
            
            System.out.println(result);
            
        }
    }
}