import java.io.*;
import java.util.Scanner;
class Prime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter any number :");
        int n=sc.nextInt();
        for(int i=2;i<n;i++){
            if(n%i==0){
                System.out.println(n+ " is not a Prime");
                break;
            }
            else{
                System.out.println(n+ " is a Prime");
                break;
            }

        }
    }
}