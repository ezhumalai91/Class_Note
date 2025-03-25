import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class F14_writefile_without_file_from_folder {
    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\Yamuna.txt");
        try{
            file.createNewFile();
            FileWriter writer=new FileWriter(file);
            writer.write("Yamuna\n");
            writer.write("I am from Pondicherry");
            writer.write("65");
            writer.flush();
            writer.close();
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
