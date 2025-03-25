import java.util.Scanner;

public class ExtendedStringMethodsDemo {

    // Method to demonstrate string operations
    public void demonstrateStringMethods() {
        Scanner scanner = new Scanner(System.in);
        String input;

        while (true) {
            System.out.println("\nChoose a string operation:");
            System.out.println("1. Convert to Uppercase");
            System.out.println("2. Convert to Lowercase");
            System.out.println("3. Check Length");
            System.out.println("4. Check if String contains a substring");
            System.out.println("5. Trim String");
            System.out.println("6. Get Character at Index");
            System.out.println("7. Get Substring");
            System.out.println("8. Check if String starts with a prefix");
            System.out.println("9. Check if String ends with a suffix");
            System.out.println("10. Replace Characters");
            System.out.println("11. Split String");
            System.out.println("12. Check for Equality");
            System.out.println("13. Convert to Char Array");
            System.out.println("14. Find Index of a Character");
            System.out.println("15. Check if String is Empty");
            System.out.println("16. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt(); // Consume the newline


            System.out.print("Enter a string: ");
            input = scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.println("Uppercase: " + input.toUpperCase());
                    break;
                case 2:
                    System.out.println("Lowercase: " + input.toLowerCase());
                    break;
                case 3:
                    System.out.println("Length: " + input.length());
                    break;
                case 4:
                    System.out.print("Enter a substring to check: ");
                    String substring = scanner.nextLine();
                    System.out.println("Contains substring? " + input.contains(substring));
                    break;
                case 5:
                    System.out.println("Trimmed String: '" + input.trim() + "'");
                    break;
                case 6:
                    System.out.print("Enter index to get character: ");
                    int index = scanner.nextInt();
                    scanner.nextLine(); // Consume the newline
                    if (index >= 0 && index < input.length()) {
                        System.out.println("Character at index " + index + ": " + input.charAt(index));
                    } else {
                        System.out.println("Index out of bounds.");
                    }
                    break;
                case 7:
                    System.out.print("Enter start index for substring: ");
                    int start = scanner.nextInt();
                    System.out.print("Enter end index for substring: ");
                    int end = scanner.nextInt();
                    scanner.nextLine(); // Consume the newline
                    if (start >= 0 && end <= input.length() && start < end) {
                        System.out.println("Substring: " + input.substring(start, end));
                    } else {
                        System.out.println("Invalid indices.");
                    }
                    break;
                case 8:
                    System.out.print("Enter prefix to check: ");
                    String prefix = scanner.nextLine();
                    System.out.println("Starts with prefix? " + input.startsWith(prefix));
                    break;
                case 9:
                    System.out.print("Enter suffix to check: ");
                    String suffix = scanner.nextLine();
                    System.out.println("Ends with suffix? " + input.endsWith(suffix));
                    break;
                case 10:
                    System.out.print("Enter character to replace: ");
                    char oldChar = scanner.nextLine().charAt(0);
                    System.out.print("Enter new character: ");
                    char newChar = scanner.nextLine().charAt(0);
                    System.out.println("Replaced String: " + input.replace(oldChar, newChar));
                    break;
                case 11:
                    System.out.print("Enter delimiter to split by: ");
                    String delimiter = scanner.nextLine();
                    String[] parts = input.split(delimiter);
                    System.out.println("Split String: ");
                    for (String part : parts) {
                        System.out.println(part);
                    }
                    break;
                case 12:
                    System.out.print("Enter another string to compare: ");
                    String anotherString = scanner.nextLine();
                    System.out.println("Strings are equal? " + input.equals(anotherString));
                    break;
                case 13:
                    char[] charArray = input.toCharArray();
                    System.out.println("Character Array: ");
                    for (char c : charArray) {
                        System.out.print(c + " ");
                    }
                    System.out.println();
                    break;
                case 14:
                    System.out.print("Enter character to find index: ");
                    char searchChar = scanner.nextLine().charAt(0);
                    int indexOfChar = input.indexOf(searchChar);
                    if (indexOfChar != -1) {
                        System.out.println("Index of '" + searchChar + "': " + indexOfChar);
                    } else {
                        System.out.println("Character not found.");
                    }
                    break;
                case 15:
                    System.out.println("Is the string empty? " + input.isEmpty());
                    break;
                case 15:
                    System.out.println("Exiting the program.");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }

        scanner.close();
    }

    public static void main(String[] args) {
        ExtendedStringMethodsDemo demo = new ExtendedStringMethodsDemo();
        demo.demonstrateStringMethods();
    }
}
