import java.io.*;
class SwapTwoNumbers {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        System.out.println("Before swapping:");
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        int temp = a;
        a = b;
        b = temp;

        System.out.println("After swapping:");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
