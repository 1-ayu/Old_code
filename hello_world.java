public class hello_world { //public is a access modifier and it means it can be visible any where
     
//     public static void main(String args[]){
//         System.out.println("Hello World");
//         //System.out.println(args[0]);
//     }
// } 
 
    public static void main(String args[]){
        int n=5;
        for(int i=1;i<=n;i++){
            System.out.println("*");
                for(int j=1;j<=i;j++){
                    System.out.print(" ");
                }
        } System.out.println();
    }
}
