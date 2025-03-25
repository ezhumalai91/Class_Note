import java.io.File;

public class F02_Deletefolder {

    public static void main(String[] args) {
        
        for (int i = 1; i <= 1000; i++) {
            File file = new File("C:\\Class\\Java\\File-Handling\\testing" + "\\" + i);
            if (file.exists()) {
                file.delete();
                System.out.println("Folder " + i + " successfully deleted");
                
            } else {
                System.out.println("Folder " + i + " does not exist");
            }
        }
    }
}
