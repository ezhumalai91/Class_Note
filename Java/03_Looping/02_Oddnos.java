import java.util.Scanner;
class Oddnos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number:");
        int n = scanner.nextInt();

        System.out.println("The first " + n + " natural Odd numbers are:");
        for (int i = 1; i <= n; i++) {
            if(i%2!=0){
            System.out.print(i + " ");
        }
        }
        scanner.close();
    }
}
