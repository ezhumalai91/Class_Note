//File creation

import java.io.File;
import java.io.IOException;

public class F08_listfiles_only {

    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna");
        File[] files=file.listFiles();
        for(File f:files)
        {
            if(f.isFile())//f.isDirectory()
            {
                System.out.println(f);
            }
        }
    }
}