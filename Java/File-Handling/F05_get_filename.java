//File creation

import java.io.File;
import java.io.IOException;

public class F05_get_filename {

    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\yamuna.txt");
        String file_name=file.getName();
        
        System.out.println("File name is "+file_name);
    
    }
}