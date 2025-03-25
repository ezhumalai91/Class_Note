//File creation

import java.io.File;
import java.io.IOException;

public class F04_delete_file {

    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\yamuna.txt");
        if(file.exists())
        {
            file.delete();
            System.out.println("File successfully deleted");
    }
    else{
        System.out.println("File does not exist");
    }
    }}