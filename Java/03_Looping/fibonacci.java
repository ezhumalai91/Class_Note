import java.io.*;
import java.util.*;

class fibonacci {
    public static void main(String[] args) {
        int a=0,b=1,nextTerm,n;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of terms");
        n=sc.nextInt();
        System.out.print(a+" ");
        System.out.print(b+" ");
        while(n!=0){
            nextTerm=a+b;
            a=b;
            b=nextTerm;
            System.out.print(nextTerm+" ");
            n--;
        }
  
}
}