import java.io.*;  
import java.net.*;  
import java.util.Scanner;

class MyClient1 {  
    public static void main(String[] args) {  
        try {      
            Socket s = new Socket("localhost", 6666);  
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter a message to send to the server: ");
            String message = scanner.nextLine();
            
            dout.writeUTF(message);  
            dout.flush();  
            
            dout.close();  
            s.close();  
            scanner.close();  
        } catch (Exception e) {  
            System.out.println(e);  
        }  
    }  
}  
