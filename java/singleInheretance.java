class a{
    void a11(){
        System.out.println("sayan in a1");
    }
}
class b extends a{
    void b11(){
        System.out.println("sayan in b1");
    }
}
public class singleInheretance{
    public static void main(String arg[]){
        b aa = new b();
        aa.a11();
        aa.b11();
    }
}

    