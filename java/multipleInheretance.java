interface a21{
    void a1();
}
interface a22{
    void a2();
}
interface a23{
    void a3();
}
class a24 implements a21 ,a22, a23{
    public void a1(){
        System.out.println("sayan in a1");
    }
    public void a2(){
        System.out.println("sayan in a1");
    }
    public void a3(){
        System.out.println("sayan in a1");
    }
}

public class multipleInheretance{
    public static void main(String argu[]){
        a24 aa = new a24();
        aa.a1();
    }
}
