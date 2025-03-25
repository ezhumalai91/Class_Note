import javax.swing.*;

public class WelcomeApp {
    public static void main(String[] args) {
        // Create a new JFrame
        JFrame frame = new JFrame("Welcome Application");
        JLabel welcomeLabel = new JLabel("Welcome to the Swing Application!", SwingConstants.CENTER);
        welcomeLabel.setFont(new java.awt.Font("Arial", java.awt.Font.BOLD, 24));
        
        // Add the label to the frame
        frame.add(welcomeLabel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}