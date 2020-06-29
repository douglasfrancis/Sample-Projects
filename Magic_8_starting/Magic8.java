import java.util.Random; 
  
public class Magic8{ 
  
    public static void main(String args[]) 
    { 
        Random rand = new Random(); 
  
        int rand_int = rand.nextInt(4); 
  
        if(rand_int == 0){
          System.out.println("Ask again later"); 
        } else if(rand_int == 1){
          System.out.println("Don\'t count on it"); 
        } else {
          System.out.println("It is certain"); 
        }
    
    } 
} 