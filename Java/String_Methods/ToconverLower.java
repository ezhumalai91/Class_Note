import java.util.Scanner;

class ToconverLower {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter any string:");
        String str=sc.nextLine();
        String newStr=str.toLowerCase();
        System.out.println("The output is:"+newStr);
    }
    
}
