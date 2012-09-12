/**
 * Test text. Please Ignore.
 * @author Admin
 */
public class Demo {
    private static final String CONSTANT = "String";
    private Object o;
    
    /**
     * Creates a new demo. <p>Paragraph!</p>
     * 
     * https://www.google.com/
     * 
     * @param o The object to demonstrate.
     */
    public Demo(Object o) {
        // Comment
        this.o = o;
        String s = CONSTANT;
        int i = 1; 
        E e = E.A;
    }
    
    public static void main(String[] args) {
        Demo demo = new Demo(args);
        demo.o.toString();
    }
}

interface A {
    public void a();
}

@interface Anno {
    String value();
}

@Anno("test")
abstract class B implements A {
    @Override
    public void a() {
        
    }
}

class C<T> extends B {
    private Class<T> clazz;

    public C(Class<T> clazz) {
        this.clazz = clazz;
    }
}

enum E {
    A,
    B,
    C;
}
