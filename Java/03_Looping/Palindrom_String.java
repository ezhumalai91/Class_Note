import java.util.Scanner;

class Palindrome_String {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a String:");
        String str1 = sc.nextLine();
        
        String rev = new StringBuilder(str1).reverse().toString();
        
        if (rev.equals(str1)) {
            System.out.println(str1 + " is a Palindrome.");
        } else {
            System.out.println(str1 + " is not a Palindrome.");
        }
        
        sc.close();
    }
}
