import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class F19_bufferreadfile {
    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\Yamuna.txt");
        try{            
            FileWriter writer=new FileWriter(file);//
            BufferedWriter bwriter=new BufferedWriter(writer);
            
            bwriter.write("dhivya");
            bwriter.newLine();
            bwriter.write("Harini");
            bwriter.newLine();
            bwriter.write("Dhatchayani");
            bwriter.newLine();
            bwriter.flush();
            bwriter.close();
            FileReader fReader=new FileReader(file);
            BufferedReader bReader=new BufferedReader(fReader);
            String line=bReader.readLine();
            while (line!=null) {
               System.out.println(line);
               line=bReader.readLine();
            }

            
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
