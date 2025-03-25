import java.io.*;  
import java.net.*;  

class MyServer1 {  
    public static void main(String[] args) {  
        try {  
            ServerSocket ss = new ServerSocket(6666);  
            System.out.println("Server is waiting for a client...");  
            Socket s = ss.accept(); // establishes connection   
            System.out.println("Client connected.");
            
            DataInputStream dis = new DataInputStream(s.getInputStream());  
            String str = dis.readUTF();  
            System.out.println("Message from client: " + str);  
            
            dis.close();
            s.close();
            ss.close();  
        } catch (Exception e) {  
            System.out.println(e);  
        }  
    }  
}  
