// instances, int, enhanced for loop, algorithms, nested loop

import java.util.ArrayList;
import java.io.FileNotFoundException;

public class day1recursive {

    ArrayList<Integer> thisArray;

    public day1recursive(String inpFile) throws FileNotFoundException {
        arrayer thisArrayer  = new arrayer();
	thisArray = thisArrayer.theCode(inpFile);
	int grandTotal = 0;
	System.out.println(thisArray);
	for (int inp : thisArray) {
//	    System.out.println(calculate(inp, 0));
	    grandTotal += calculate(inp, 0);
	}
	System.out.println(grandTotal);
    }

    public int calculate(int inp, int total) {
        if (inp > 6) {
	    System.out.println(inp + " " + total);
	    inp /= 3;
	    inp -= 2;
	    total += inp;
	    calculate(inp, total);
	}
	return total;
    }

    public static void main(String[] args) throws FileNotFoundException {
        day1recursive doer = new day1recursive(args[0]);
    }
}
