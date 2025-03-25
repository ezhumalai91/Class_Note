import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class F15_readfile {
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
            int read=fileReader.read();
            //read charater by using FileReader class --method---read()
            while(read!=-1) {
                
                System.out.println(read);//System.out.println((char)read);
                read=fileReader.read();
            }

        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
