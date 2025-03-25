import java.util.*;

class List_example{
    public static void main(String[] args) {
        List<Integer> l1 = new ArrayList<Integer>();
        l1.add(0, 10);
        l1.add(1, 20);
        l1.add(2, 200);

        System.out.println(l1);


        l1.remove(1);

        System.out.println(l1);

        l1.set(0, 5);
        System.out.println(l1);
    }
}