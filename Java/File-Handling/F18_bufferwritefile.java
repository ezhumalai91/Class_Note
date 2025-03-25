import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class F18_bufferwritefile {
    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\Yamuna.txt");
        try{            
            FileWriter writer=new FileWriter(file);//
            BufferedWriter bwriter=new BufferedWriter(writer);
            bwriter.write("dhivya");
            bwriter.newLine();
            bwriter.write("yamuna");
            bwriter.flush();
            bwriter.close();
            
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
