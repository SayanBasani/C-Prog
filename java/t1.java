
class box1{
    int b1(int a , int b){
        return a+b;
    }
    int b2(int a , int b , int c){
        return a+b+c;
    }
}

public class t1 {
    public static void main(String[] args) {
        box1 a = new box1();
        int bb ;
        try {
            bb = a.b1(5,6);
        }
        catch(Exception m) {
            bb = a.b2(5,6,7);
        }
        System.out.println("answer "+bb);
    }

}