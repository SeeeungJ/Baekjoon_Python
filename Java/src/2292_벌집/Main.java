import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        
        int output = 1;
        int compare = 1;

        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();

        while(compare < N){
            compare += (output * 6);
            output++;
        }

        System.out.println(output);
    }
}
