//File creation

import java.io.File;
import java.io.IOException;

public class F03_Create_text_file {

    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\yamuna.txt");
        if(file.exists()==false)
        {
            try{            
            file.createNewFile();//to create new file
            System.out.println("File successfully created");
            }catch(IOException e){
            e.printStackTrace();
            }
        }
        else{
            System.out.println("File already present created");
        }
    }}