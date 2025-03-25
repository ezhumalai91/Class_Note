import java.io.*;
import java.util.*;
class GreatestThreeNo{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a,b,c;
        System.out.println("Enter first Number");
        a = sc.nextInt();
        System.out.println("Enter second Number");
        b = sc.nextInt();
        System.out.println("Enter third Number");
        c = sc.nextInt();
        if(a>b && a>c){
            System.out.println("A is Greater than B and C");
        }
        else if(b>c && b>a){
            System.out.println("B is Greater than A and C");
        }
        else{
            System.out.println("C is Greater than A and B");
        }
}}