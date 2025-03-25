import java.sql.*;
import java.util.Scanner;

public class CRUDOperations {

    // JDBC URL, username, and password of MySQL server
    private static final String URL = "jdbc:mysql://localhost:3306/java_studentdb";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "";

    public static void main(String[] args) {
        try {
            // Register JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish connection
            Connection connection = DriverManager.getConnection(URL, USERNAME, PASSWORD);
            System.err.println("Connection succ");

            // Create a Scanner object for user input
            Scanner scanner = new Scanner(System.in);

            // Present options to the user
            System.out.println("Choose an option:");
            System.out.println("1. Add a record");
            System.out.println("2. View records");
            System.out.println("3. Update a record");
            System.out.println("4. Delete a record");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    createRecord(connection);
                    break;
                case 2:
                    readRecords(connection);
                    break;
                case 3:
                    updateRecord(connection);
                    break;
                case 4:
                    deleteRecord(connection);
                    break;
                default:
                    System.out.println("Invalid choice");
            }

            // Close resources
            scanner.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Create operation raw input
    // private static void createRecord(Connection connection) throws SQLException {
    //     String insertQuery = "INSERT INTO student (roleno, name, age) VALUES (?, ?, ?)";
    //     PreparedStatement preparedStatement = connection.prepareStatement(insertQuery);
    //     // Set values for parameters
    //     preparedStatement.setInt(1, 101);
    //     preparedStatement.setString(2, "John Doe");
    //     preparedStatement.setInt(3, 25);
    //     int rowsAffected = preparedStatement.executeUpdate();
    //     System.out.println(rowsAffected + " row(s) inserted.");
    // }
    private static void createRecord(Connection connection) throws SQLException {
        Scanner scanner = new Scanner(System.in);
    
        System.out.println("Enter roll number:");
        int rollNo = scanner.nextInt();
    
        System.out.println("Enter name:");
        String name = scanner.next(); // Assuming the name doesn't contain spaces
    
        System.out.println("Enter age:");
        int age = scanner.nextInt();
    
        // Close the scanner after input
        scanner.close();
    
        // Execute the insert query with the user input
        String insertQuery = "INSERT INTO student (roleno, name, age) VALUES (?, ?, ?)";
        PreparedStatement preparedStatement = connection.prepareStatement(insertQuery);
        preparedStatement.setInt(1, rollNo);
        preparedStatement.setString(2, name);
        preparedStatement.setInt(3, age);
    
        int rowsAffected = preparedStatement.executeUpdate();
        System.out.println(rowsAffected + " row(s) inserted.");
    }
    
    // Read operation
    private static void readRecords(Connection connection) throws SQLException {
        String selectQuery = "SELECT * FROM student";
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery(selectQuery);
        while (resultSet.next()) {
            // Process each row
            int rollNo = resultSet.getInt("roleno");
            String name = resultSet.getString("name");
            int age = resultSet.getInt("age");
            System.out.println("Roll No: " + rollNo + ", Name: " + name + ", Age: " + age);
        }
    }

    // Update operation
    private static void updateRecord(Connection connection) throws SQLException {
        String updateQuery = "UPDATE student SET age = ? WHERE roleno = ?";
        PreparedStatement preparedStatement = connection.prepareStatement(updateQuery);
        preparedStatement.setInt(1, 26);
        preparedStatement.setInt(2, 101);
        int rowsAffected = preparedStatement.executeUpdate();
        System.out.println(rowsAffected + " row(s) updated.");
    }

    // Delete operation
    private static void deleteRecord(Connection connection) throws SQLException {
        String deleteQuery = "DELETE FROM student WHERE roleno = ?";
        PreparedStatement preparedStatement = connection.prepareStatement(deleteQuery);
        preparedStatement.setInt(1, 101);
        int rowsAffected = preparedStatement.executeUpdate();
        System.out.println(rowsAffected + " row(s) deleted.");
    }
}
