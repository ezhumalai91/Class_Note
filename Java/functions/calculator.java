import java.io.*;
import java.util.Scanner;
class calculator{
    Scanner sc = new Scanner(System.in);

    public void add(){
    int a,b,result;
    System.out.println("Enter first number");
    a = sc.nextInt();
    System.out.println("Enter second number");
    b = sc.nextInt();
    result = a + b ;
    System.out.println("Result is "+result);
    }


    public static void main(String arg[]){
        calculator c = new calculator();
        c.add();
    }
}