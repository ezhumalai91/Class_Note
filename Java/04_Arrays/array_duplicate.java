
class array_duplicate{
    public static void main(String[] args) {
        int[] arr={6,20,24,10,26,12,20,10};
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++)
            {
                if(arr[i]==arr[j]){
                    System.out.println("Duplicate element is "+arr[i]);
                }
            }
        }
    
    }
}