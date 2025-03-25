import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class F17_readfile_count_char {
    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\Yamuna.txt");
        try{            
            FileWriter writer=new FileWriter(file);
            writer.write("Yamuna\n");
            writer.write("I am from Pondicherry");
            writer.write("65");
            writer.flush();
            writer.close();
            FileReader fileReader=new FileReader(file);
            char[] ch=new char[(int)file.length()];
            System.out.println(ch.length);
            fileReader.read(ch);
            for(char ch1:ch){
                System.out.print(ch1);
            }
            
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
