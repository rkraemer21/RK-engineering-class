import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.ArrayList;
import java.lang.Math;

class day10 {

    char[][] starter;
    ArrayList<Integer> tot;

    public day10(String[] args) throws FileNotFoundException {
        starter = day10handler.main(args);
        tot = new ArrayList<Integer>();
    }

    public void finder() {
        System.out.println(Arrays.deepToString(starter));
        int iRow = 0;
	for (char[] row : starter) {
	    int iSpace = 0;
	    for (char space : row) {
	        if (space != '#') {
		    iSpace ++;
		} else if (space == '#') {
		    meter(iRow, iSpace);
		    iSpace ++;
		} else {
		    iSpace ++;
		}
	    }
	    iRow ++;
	}
    }

    public void meter(int iRow, int iSpace) {
       double checkRow = 0;
       ArrayList<Double> slopes = new ArrayList<Double>();
       for (char[] row : starter) {
	   System.out.println("checkRow: " + checkRow);
           double checkSpace = 0;
           for (char space : row) {
	       if (space != '#') {
		   System.out.println("N-P");
	       } else if (space == '#') {
	           double rise = iRow - checkRow;
		   double run = iSpace - checkSpace;
	           double slope = Math.atan2(run, rise);
		   if (rise == 0.0 && run == 0.0) {
		       System.out.println("N-Z");
		   /*} else if (slope == 0.0 && slopes.indexOf(slope) != -1) {
		       slopes.add(slope);
		       System.out.println("Y-Z");*/
		   } else if (slopes.indexOf(slope) == -1) {
	               slopes.add(slope);
		       System.out.println("Y-S");
        	   } else if (slopes.indexOf(slope) != -1) {
		       System.out.println("N-A");
		   }
	       }
	       System.out.println("checkSpace: " + checkSpace);
	       checkSpace ++;
	   }
           checkRow ++;
       }
       System.out.println(slopes.size() + "~" + iRow + "-" + iSpace + "-----------------");
 //      System.out.println(slopes.toString());
       tot.add(slopes.size());
    }

    public void max() {
        int maximum = 0;
        for (int i : tot) {
	    if (i > maximum) {
	        maximum = i;
	    } else {
	        continue;
	    }
	}
	System.out.println(maximum);
    }

    public static void main(String[] args) throws FileNotFoundException {
        day10 doer = new day10(args);
        doer.finder();
	doer.max();
    }
}
