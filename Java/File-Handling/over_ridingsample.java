class Employee{  
    void display(int a,int b){
        a=200;
        b=300;
        System.out.println("A,B"+a+b);

    }   
   }  
   class Programmer extends Employee{  
    void display(int a,int b){
        a=20;
        b=30;
        System.out.println("A,B"+a+b);

    } 
    public static void main(String args[]){  
      Programmer p=new Programmer();  
        p.display(2,4);
    //   System.out.println("Bonus of Programmer is:"+p.bonus);  
   }  
   }  