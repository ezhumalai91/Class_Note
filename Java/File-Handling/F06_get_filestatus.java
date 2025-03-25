//File creation

import java.io.File;
import java.io.IOException;

public class F06_get_filestatus {

    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\yamuna.txt");
        String file_name=file.getName();
        System.out.println("File name is"+file_name);        
        System.out.println(file.canExecute());
        System.out.println(file.canRead());
        System.out.println(file.canWrite());    
    }
}