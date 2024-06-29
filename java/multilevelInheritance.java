class a31{
    void a1(){
        System.out.println("sayan in a1");
    }
}
class a32 extends a31{
    void a2(){
        System.out.println("sayan in a2");
    }
}
class a33 extends a32{
    void a3(){
        System.out.println("sayan in a3");
    }
}
public class multilevelInheritance {
    public static void main(String argu[]){
        a33 aa = new a33();
        aa.a1();
        aa.a2();
        aa.a3();
    }
}
