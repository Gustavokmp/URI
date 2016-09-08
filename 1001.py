import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        int a,b,resultado;
	    Scanner teclado = new Scanner(System.in);
    	a = teclado.nextInt();
    	b = teclado.nextInt();
    	resultado = a + b;
    	System.out.println("X = " + resultado);
    }
}