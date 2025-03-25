import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class F23_BufferedReader_Word_count {
    public static void main(String[] args) {
        File file=new File("C:\\Java_class\\Yamuna\\Yamuna.txt");
        try{            
            FileWriter writer=new FileWriter(file,true);//FileWriter writer=new FileWriter(file,true);--append data
            BufferedWriter bwriter=new BufferedWriter(writer);
            bwriter.write("Yamuna i a good girl.");
            bwriter.newLine();
            bwriter.write("I am from pondy.");
            bwriter.newLine();
            bwriter.write("Dhivya is a good girl");
            bwriter.newLine();
            bwriter.write("I am from pondy.");
            bwriter.flush();
            bwriter.close();
            FileReader fReader=new FileReader(file);
            BufferedReader bReader=new BufferedReader(fReader);
            String line=bReader.readLine();
            int LineCount=0;
            int sentanceCount=0;
            int WordCount=0;
            while (line!=null) {
                String[] sentance=line.split("[.]");
                String[] words=line.split(" ");
                sentanceCount+=sentance.length;
                LineCount++;
                WordCount+=words.length;
               System.out.println(line);
               line=bReader.readLine();
            }
            System.out.println("Number of lines =\t"+LineCount);
            System.out.println("Number of Sentance ="+sentanceCount);
            System.out.println("Number of Words ="+WordCount);

            
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}