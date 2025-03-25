import java.io.*;
import java.util.Scanner;
class calculator1{
    Scanner sc = new Scanner(System.in);
    public int add(){
    int a,b,result;
    System.out.println("Enter first number");
    a = sc.nextInt();
    System.out.println("Enter second number");
    b = sc.nextInt();
    result = a + b ;
    return result;
    }
    public static void main(String arg[]){
        calculator1 c = new calculator1();
        System.out.println("The addition is "+c.add());
    }
}