// instances, int, enhanced for loop, algorithms, nested loop

import java.util.ArrayList;
import java.io.FileNotFoundException;

public class day1two {

    public static void main(String[] args) throws FileNotFoundException {
        arrayer thisArrayer = new arrayer();
        ArrayList<Integer> thisArray = thisArrayer.theCode(args[0]);
        int total = 0;

        for (int inp : thisArray) {
            while (inp > 6) {
                inp /= 3;
                inp -= 2;
                total += inp;
            }
        }

        System.out.println(total);
    }
}
