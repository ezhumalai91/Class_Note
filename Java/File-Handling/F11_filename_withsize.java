//File creation

import java.io.File;
import java.io.IOException;

public class F11_filename_withsize {

    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna");
        File[] files=file.listFiles();
        for(File f:files)
        {
            if(f.isFile())//f.isDirectory()
            {
                String filename=f.getName();
                int lastdot=filename.lastIndexOf('.');
                String extension=filename.substring(lastdot+1);
                // System.out.println(extension);
                if(extension.equals("jpeg"))
                {
                    System.out.println(filename+" of size is "+f.length());
                }
            
            }
        }
    }
}