import java.util.ArrayList;
import java.io.FileNotFoundException;

public class day1 {

    public static void main(String[] args) throws FileNotFoundException {
        arrayer thisArrayer = new arrayer();
        ArrayList<Integer> thisArray = thisArrayer.theCode(args[0]);
        //System.out.println(thisArray);

	for (int x : thisArray) {
	    for (int y : thisArray) {
	        for (int z : thisArray) {
	            if (x + y + z == 2020) {
		        System.out.println(x + " " + y + " " + z);
		        System.out.println(x * y * z);
		    }
		}
	    }
	}
    }

}
