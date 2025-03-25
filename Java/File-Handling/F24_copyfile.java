import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class F24_copyfile {
    public static void main(String[] args) {
        try {
            InputStream input=new FileInputStream("C:\\Java_class\\Yamuna\\file");
            OutputStream output=new FileOutputStream("C:\\Java_class\\Yamuna\\1");
            int content=input.read();
            while (content!=-1) {
                output.write(content);
                content=input.read();
            }
            input.close();
            output.flush();
            
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
}
