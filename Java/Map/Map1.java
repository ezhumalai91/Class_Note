import java.util.HashMap;
import java.util.Map;

class Map1{
    public static void main(String[] arg){
        Map<Integer,String> map=new HashMap<Integer,String>();
        map.put(1,"Dhivya");
        map.put(2,"Nalini");
        map.put(3,"Balaji");
        System.out.println(map);
        System.out.println(map.get(2));
        map.remove(2);
        System.out.println(map);
    }
}