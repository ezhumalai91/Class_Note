import java.io.*;
import java.util.Scanner;
class amstrong{
    Scanner sc = new Scanner(System.in);
    public int ams(int n){
    int rem,sum=0;
    while (n!=0) {
        rem=n%10;
        sum=sum+(rem*rem*rem);
        n=n/10;           
    }
    return sum;   
}
    public static void main(String arg[]){
        amstrong a = new amstrong();
        System.out.println("Please enter any number:");
        int n = a.sc.nextInt();
        if (a.ams(n)==n) {
            System.out.println(n+" is an amstrong number");
            }
            else{
                System.out.println(n+" is not an amstrong number");    
            }
    }
}