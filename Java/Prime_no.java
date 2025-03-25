import java.util.*;
class Prime_no{
    public static void main(String[] arg){
        Scanner sc=new Scanner(System.in);
        int i,j,temp=0,n;
        System.out.println("Please enter any value:");
        n=sc.nextInt();
        for(i=2;i<n;i++){
            for(j=2;j<i;j++){
                if(i%j==0){
                    System.out.println(i+"is not a prime number");
                    break;
                }
                else{
                    System.out.println(i+"is a prime number");
                    break;
            }}}
 
    }}
