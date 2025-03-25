//File creation

import java.io.File;
import java.io.IOException;

public class F12_delete_particular_file {

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
                    f.delete();
                    System.out.println(filename+" Successfully deleted ");
                }
            
            }
        }
    }
}