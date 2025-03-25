import java.util.Scanner;

class All_in_one {

    // 1. Count characters in a string
    public static int countCharacters(String str) {
        return str.length();
    }

    // 2. Count words in a string
    public static int countWords(String str) {
        if (str == null || str.isEmpty()) {
            return 0;
        }
        String[] words = str.trim().split(" ");
        return words.length;
    }

    public static int countSentance(String str) {
        if (str == null || str.isEmpty()) {
            return 0;
        }
        String[] lines = str.split("\\.");
        return lines.length;
    }

    // 3. Count lines in a string
    public static int countLines(String str) {
        if (str == null || str.isEmpty()) {
            return 0;
        }
        String[] lines = str.split("\n");
        return lines.length;
    }

    // 4. Check if a string is a valid 10-digit phone number
    public static boolean isValidPhoneNumber(String phoneNumber) {
        if (phoneNumber == null || phoneNumber.length() != 10) {
            return false;
        }
        // Check if all characters are digits
        for (char c : phoneNumber.toCharArray()) {
            if (!Character.isDigit(c)) {
                return false;
            }
        }
        return true;
    }

    // 5. Check if a string is a valid email address (basic validation)
    public static boolean isValidEmail(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        // csc@gmail.com
        String[] str1=email.split("@");  //{"csc","gamil.com"}
        String[] str2=str1[1].split("\\.");     //{"gmail","com"}
        if(str1[0].equals("gmail") && str1[1].equals("com")){
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input;

        while (true) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Count Characters");
            System.out.println("2. Count Words");
            System.out.println("3. Count Lines");
            System.out.println("4. Validate 10-digit Phone Number");
            System.out.println("5. Validate Email Address");
            System.out.println("6. Sentance Lines");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter a string: ");
                    input = scanner.nextLine();
                    System.out.println("Character count: " + countCharacters(input));
                    break;
                case 2:
                    System.out.print("Enter a string: ");
                    input = scanner.nextLine();
                    System.out.println("Word count: " + countWords(input));
                    break;
                case 3:
                    System.out.print("Enter a string: ");
                    input = scanner.nextLine();
                    System.out.println("Line count: " + countLines(input));
                    break;
                case 4:
                    System.out.print("Enter a 10-digit phone number: ");
                    input = scanner.nextLine();
                    System.out.println("Valid phone number: " + isValidPhoneNumber(input));
                    break;
                case 5:
                    System.out.print("Enter an email address: ");
                    input = scanner.nextLine();
                    System.out.println("Valid email: " + isValidEmail(input));
                    break;
                case 6:
                    System.out.print("Enter a string: ");
                    input = scanner.nextLine();
                    System.out.println("Sentance count: " + countSentance(input));
                break;
                case 7:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        }
    }
}