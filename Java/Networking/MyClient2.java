import java.io.*;  
import java.net.*;  
import java.util.Scanner;

class MyClient2 {  
    public static void main(String[] args) {  
        try {      
            Socket s = new Socket("localhost", 6666);  
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            DataInputStream din = new DataInputStream(s.getInputStream());
            Scanner scanner = new Scanner(System.in);

            String message = "";
            while (!message.equalsIgnoreCase("exit")) {
                System.out.print("Client: ");
                message = scanner.nextLine();
                dout.writeUTF(message);  
                dout.flush();
                
                // Receive response from server
                String serverMessage = din.readUTF();
                System.out.println("Server: " + serverMessage);
            }

            // Cleanup
            dout.close();  
            din.close();  
            s.close();  
            scanner.close();  
        } catch (Exception e) {  
            System.out.println(e);  
        }  
    }  
}
