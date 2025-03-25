import java.util.HashMap;
import java.util.Map;

class Map2{
    public static void main(String[] arg){
        Map<Integer,Integer> map=new HashMap<Integer,Integer>();
        
        for(int i=1;i<=10000;i++){
            map.put(i,i*3);
        }
        for(int i=1;i<=10000;i++){
            System.out.println(i+"==="+map.get(i));               
        }

        for(Integer i:map.values()){

            System.out.println(i);
        }

        for(Integer i:map.keySet()){

            System.out.println(i);
        }

        for(Map.Entry<Integer, Integer> i:map.entrySet()){

            System.out.println(i.getKey()+"==="+i.getValue());
        }
    }
}