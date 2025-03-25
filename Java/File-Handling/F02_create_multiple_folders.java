import java.io.File;

public class F02_create_multiple_folders {

    public static void main(String[] args) {
        
        for(int i = 1; i <= 1000; i++) {
        
            File file = new File("C:\\Class\\Java\\File-Handling\\testing" + "\\" + i);
            if (file.exists()) {
                System.out.println("Folder " + i + " already exists");
            } else {
                file.mkdirs();
                System.out.println("Folder " + i + " successfully created");        
            }
            
        }
    }
}
