import java.io.*;
import java.util.*;
class Vowels {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        char ch;
        System.out.println("Please enter any character:");
        ch=sc.next().charAt(0);
        
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
        {
            System.out.println(ch + " is a vowel");
        }
        else
        {
            System.out.println(ch + " is not a vowel");
        }
        
    }
    }
