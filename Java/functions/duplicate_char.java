import java.util.Scanner;

class DuplicateChar {
    // Method to print characters of each string
    public void dupChar(String[] strings) {
        for (String str : strings) {
            System.out.println("Characters in string: " + str);
            for (int i = 0; i < str.length(); i++) {
                System.out.println(str.charAt(i)); // Use charAt to get characters
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        DuplicateChar ch = new DuplicateChar();
        System.out.println("Please enter 5 strings:");

        String[] str = new String[5];
        for (int i = 0; i < 5; i++) {
            str[i] = sc.nextLine();
        }

        ch.dupChar(str);
        sc.close();
    }
}
