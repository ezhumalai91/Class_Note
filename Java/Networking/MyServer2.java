import java.io.*;  
import java.net.*;  

class MyServer2 {  
    public static void main(String[] args) {  
        try {  
            ServerSocket ss = new ServerSocket(6666);  
            System.out.println("Server is waiting for a client...");  
            Socket s = ss.accept(); // establishes connection   
            System.out.println("Client connected.");

            DataInputStream dis = new DataInputStream(s.getInputStream());  
            DataOutputStream dos = new DataOutputStream(s.getOutputStream());
            
            // Continuous chat
            String clientMessage = "", serverMessage = "";
            while (!clientMessage.equalsIgnoreCase("exit")) {
                clientMessage = dis.readUTF();  
                System.out.println("Client: " + clientMessage);
                
                // Send response to client
                System.out.print("Server: ");
                serverMessage = new BufferedReader(new InputStreamReader(System.in)).readLine();
                dos.writeUTF(serverMessage);  
                dos.flush();
            }
            
            // Cleanup
            dis.close();
            dos.close();
            s.close();
            ss.close();  
        } catch (Exception e) {  
            System.out.println(e);  
        }  
    }  
}
