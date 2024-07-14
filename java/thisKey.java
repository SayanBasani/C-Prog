class thisBox1{
    int x = 5;
    void box1(int x){
        System.out.println(x);
        System.out.println(this.x);
    }
}
class thisBox2 extends thisBox1{
    void box2(){
        int x = 10;
        System.out.println(super.x);
        System.out.println(x);
    }
}

public class thisKey{
    public static void main(String args[]){
        System.out.println(" sayan ");
        thisBox2 obj = new thisBox2();
        obj.box2();
    }
}