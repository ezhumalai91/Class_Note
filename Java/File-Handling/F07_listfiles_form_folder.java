//File creation

import java.io.File;
import java.io.IOException;

public class F07_listfiles_form_folder {

    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna");
        String[] listoffiles=file.list();
        // System.out.println(listoffiles);
        
        // for(int i=0;i<listoffiles.length;i++)
        // {
        //     System.out.println(listoffiles[i]);
        // }
        for(String c:listoffiles)
        {
            System.out.println(c);
        }
    }
}