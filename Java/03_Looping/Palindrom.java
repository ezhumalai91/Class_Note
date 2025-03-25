import java.io.*;
import java.util.Scanner;
class Palindrom {
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        int n,temp,rev=0;
        System.out.println("Enter a Number");
        n = sc.nextInt();
        temp = n;
        while (n!=0) {
            int rem = n%10;
            rev=rev*10+rem; 
            n = n/10;  
            }
    if(temp==rev){
        System.out.println(temp+" is a Palindrome");
     
    }
    else{
        System.out.println(temp+" is not a Palindrome");
    }
        }
    }