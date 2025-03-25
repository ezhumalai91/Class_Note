//File creation

import java.io.File;

public class F01_folder_create {

    public static void main(String[] args) {
        File file=new File("C:\\Class\\Java\\File-Handling\\javaBatch");
        if(file.exists())
        {
            System.out.println("Already folder found in same name");
        }
        else{
            file.mkdirs();
            System.out.println("Folder successfully created");
        }

    }
}