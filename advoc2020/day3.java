import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;

class day3 {
   
    char[][] starter;

    public day3(String[] args) throws FileNotFoundException {
        starter = hashArrayer.main(args);
    }

    public int finder(int z, int w) {
        //System.out.println(Arrays.deepToString(starter));
        //System.out.println(starter.length);
	int x = 0;
	int trees = 0;
        for (int y = 0; y < starter.length; y += w) {

	    char check = starter[y][x];

	    //System.out.println(y + "-" + x + " = " + check);

            if (check == '#') {
	        trees += 1;
	    }

	    x += z;
	    //System.out.println(starter[y].length);
	    if (x >= starter[y].length) {
	        x %= starter[y].length;
	    }
        }
	System.out.println(trees);
	return trees;
    }

    public static void main(String[] args) throws FileNotFoundException {
        day3 doer = new day3(args);
	int r1 = doer.finder(1, 1);
	int r2 = doer.finder(3, 1);
	int r3 = doer.finder(5, 1);
	int r4 = doer.finder(7, 1);
	int r5 = doer.finder(1, 2);
	System.out.println(r1  * r2 * r3 * r4 * r5);
    }
}
