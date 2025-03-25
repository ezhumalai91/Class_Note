import java.io.*;
import java.util.Scanner;

class MultiFunctionProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Choose an option:");
        System.out.println("1: Check if a number is even or odd");
        System.out.println("2: Swap two numbers");
        System.out.println("3: Check if two strings match");
        int choice = scanner.nextInt();
        
        switch (choice) {
            case 1:
                System.out.print("Enter a number: ");
                int number = scanner.nextInt();
                if (number % 2 == 0) {
                    System.out.println(number + " is even.");
                } else {
                    System.out.println(number + " is odd.");
                }
                break;

            case 2:
                System.out.print("Enter first number: ");
                int num1 = scanner.nextInt();
                System.out.print("Enter second number: ");
                int num2 = scanner.nextInt();

                System.out.println("Before swapping:");
                System.out.println("num1 "+num1);
                System.out.println("num2 "+num2);                
                // Swapping the numbers
                int temp = num1;
                num1 = num2;
                num2 = temp;
                
                System.out.println("After swapping:");
                System.out.println("num1 "+num1);
                System.out.println("num2 "+num2);
                break;

            case 3:
                System.out.print("Enter first string: \n");
                scanner.nextLine();// Consume newline left-over                
                String str1 = scanner.nextLine();
                System.out.print("Enter second string: ");
                String str2 = scanner.nextLine();
                
                if (str1.equals(str2)) {
                    System.out.println("Strings match.");
                } else {
                    System.out.println("Strings do not match.");
                }
                break;

            default:
                System.out.println("Invalid choice. Please select a valid option.");
                break;
        }

        scanner.close();
    }
}