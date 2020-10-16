import java.util.ArrayList;
import java.io.FileNotFoundException;
//hi
public class day1 {

    public static void main(String[] args) throws FileNotFoundException {
        arrayer thisArrayer = new arrayer();
        ArrayList<Integer> thisArray = thisArrayer.theCode(args[0]);
        int total = 0;

        for (int inp : thisArray) {
            inp /= 3;
            inp -= 2;
            total += inp;
        }

        System.out.println(total);
    }
}
