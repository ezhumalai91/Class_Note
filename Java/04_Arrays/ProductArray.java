import java.util.Scanner;

class ProductArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of products: ");
        int numProducts = scanner.nextInt();
        scanner.nextLine(); // Consume the newline
       String[][] products = new String[numProducts][3];

        for (int i = 0; i < numProducts; i++) {
            System.out.println("Enter details for product " + (i + 1) + ":");
            System.out.print("Product ID: ");
            products[i][0] = scanner.nextLine();
            System.out.print("Product Name: ");
            products[i][1] = scanner.nextLine();
            System.out.print("Product Count: ");
            products[i][2] = scanner.nextLine();
        }

        System.out.println("\nProduct Information:");
        System.out.println("Product ID \t Product Name \t Count\n");
        for (int i = 0; i < numProducts; i++) {
            System.out.println(products[i][0]+"\t"+products[i][1]+"\t"+products[i][2]+"\n");
        }

        scanner.close();
    }
}
