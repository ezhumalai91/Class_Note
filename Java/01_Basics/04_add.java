import java.io.*;
import java.util.Scanner;

class AdditionProgram {
    public static void main(String[] args) {
        int num1,num2,sum;
		Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        num1 = scanner.nextInt();
        System.out.print("Enter the second number: ");
        num2 = scanner.nextInt();
        sum = num1 + num2;
        System.out.print("The sum of " + num1 + " and " + num2 + " is " + sum);
        scanner.close();
    }
}