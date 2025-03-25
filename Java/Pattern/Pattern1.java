// class Pattern1{
//     public static void main(String[] args) {
//         int row = 5,col=5;
//         for(int i=1;i<=row;i++)
//         {
//             for(int j=1;j<=col;j++)
//             {
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
// }
// }


// class Pattern1{
//     public static void main(String[] args) {
//         int row = 5,col=5;
//         for(int i=1;i<=row;i++)
//         {
//             for(int j=1;j<=col;j++)
//             {
//                 if(j==1 || i==5 ||j==5 ||i==1){
//                 System.out.print("*");
//                 }
//                 else{
//                     System.out.print(" ");
//                 }
//             }
//             System.out.println();
//         }
// }
// }

// class Pattern1{
//     public static void main(String[] args) {
//         int row = 5,col=5;
//         for(int i=1;i<=row;i++)
//         {
//             for(int j=1;j<=col;j++)
//             {
//                 if(i==j || i+j==6){
//                 System.out.print("*");
//                 }
//                 else{
//                     System.out.print(" ");
//                 }
//             }
//             System.out.println();
//         }
// }
// }


class Pattern1{
    public static void main(String[] args) {
        int row = 5,col=5;
        for(int i=1;i<=row;i++)
        {
            for(int j=1;j<=col;j++)
            {
                if(i==j || i+j==6 || j==1 || i==5 ||j==5 ||i==1){
                System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
}
}