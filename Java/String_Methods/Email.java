import java.util.Scanner;

public class Email {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter any string:");
        String str=sc.nextLine();
        String[] newStr=str.split("@");//{"khdskj","gmail.com"}
        String[] newStr1=newStr[1].split("\\.");//{"gmail","com"}
        
        if(newStr1[0].equals("gmail") && newStr1[1].equals("com")){
            System.out.println(str+" is a valid email");
        }
        
    }
}