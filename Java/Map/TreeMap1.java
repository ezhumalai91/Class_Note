import java.util.Map;
import java.util.TreeMap;

class TreeMap1{
    public static void main(String[] arg){
        TreeMap<Integer, String> numbers = new TreeMap<>();
        numbers.put(0,"Anu");
        numbers.put(9,"Anu1");
        numbers.put(10,"Anu2");
        numbers.put(90,"Anu3");
        System.out.println(numbers);
        numbers.remove(0);
        System.out.println(numbers);
        
        for(Map.Entry<Integer, String> i:numbers.entrySet()){
            System.out.println(i.getKey()+" "+i.getValue());
        }
    }
}