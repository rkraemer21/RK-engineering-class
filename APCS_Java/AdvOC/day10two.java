import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.ArrayList;
import java.lang.Math;
import java.util.Collections;

class day10two {

    char[][] starter;
    ArrayList<double[]> tot;

    public day10two(String[] args) throws FileNotFoundException {
        starter = day10handler.main(args);
        tot = new ArrayList<double[]>();
    }

    public ArrayList<Double> finder() {
        ArrayList<Double> slopes = new ArrayList<Double>();
        int iRow = 0;
	for (char[] row : starter) {
	    int iSpace = 0;
	    for (char space : row) {
	        if (space != '#') {
		    iSpace ++;
		} else if (space == '#') {
		    slopes = meter(iRow, iSpace);
		    iSpace ++;
		} else {
		    iSpace ++;
		}
	    }
	    iRow ++;
	}
	return slopes;
    }

    public ArrayList<Double> meter(int iRow, int iSpace) {
       double checkRow = 0;
       ArrayList<Double> slopes = new ArrayList<Double>();
       for (char[] row : starter) {
//	   System.out.println("checkRow: " + checkRow);
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
		   } else if (slopes.indexOf(slope) == -1) {
	               slopes.add(slope);
		       System.out.println("Y-S");
        	   } else if (slopes.indexOf(slope) != -1) {
		       System.out.println("N-A");
		   }
	       }
//	       System.out.println("checkSpace: " + checkSpace);
	       checkSpace ++;
	   }
           checkRow ++;
       }
       double[] point = {slopes.size(), iRow, iSpace};
//       System.out.println(slopes.size() + "~" + iRow + "-" + iSpace + "-----------------");
       tot.add(point);
       return slopes;
    }

    public void max(ArrayList<Double> theSlopes) {
        double maximum = 0;
	double[] base = new double[3];
        for (double[] thePoint : tot) {
	    if (thePoint[0] > maximum) {
	        maximum = thePoint[0];
		base = thePoint;
	    } else {
	        continue;
	    }
	}
	System.out.println(Arrays.toString(base));
	laser(base, theSlopes);
    }

    public void laser(double[] base, ArrayList<Double> theSlopes) {
        //ArrayList<Double> angles = Collections.sort(theSlopes);
        double x = base[2];
	double y = base[1];
	int i = 0;
	System.out.println(theSlopes);
	Collections.sort(theSlopes);
	System.out.println(theSlopes);
	//System.out.println(angles);
//	double 
	while (i < 200) {
	       theSlopes.remove(0);
	       
	       i ++; 
	}
	System.out.println(theSlopes);
    }

/*    public ArrayList<Double> sort(ArrayList<Double> theSlopes) {
        ArrayList<Double> angles = new ArrayList<Double>();
	double start = 0.5 * Math.PI;
	int begin;
	for (double slope : theSlopes) {
	   if (slope == start) {
	       angles.add(slope);
	   }
	}
	return angles;
    }
*/

    public static void main(String[] args) throws FileNotFoundException {
        day10two doer = new day10two(args);
        ArrayList<Double> theSlopes = doer.finder();
	doer.max(theSlopes);
    }
}
