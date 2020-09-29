import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.util.Arrays;

class day8two {

    public static void main(String[] args) throws FileNotFoundException {
        int[][][] picture = new int[25][6][100];
        ArrayList<Integer> theNumbers = numSplitter.main(args);

        for (int i2 = 0; i2 < 100; i2 ++) {
            for (int i3 = 0; i3 < 6; i3 ++) {
                for (int i4 = 0; i4 < 25; i4 ++) {
                      int i = i2 * 150 + i4 + 25 * i3;
                      picture[i4][i3][i2] = theNumbers.get(i);
                }
            }
        }

        int[][] finalPic = new int[25][6];
       
        for (int iRow = 0; iRow < 6; iRow ++) {
            for (int iPix = 0; iPix < 25; iPix ++) {
                int pixel = 3;
                for (int i = 0; i < 100; i ++) {
		    if (picture[iPix][iRow][i] == 0) {
		        pixel = 0;
			break;
		    } else if (picture[iPix][iRow][i] == 1) {
		        pixel = 1;
			break;
		    } else if (picture[iPix][iRow][i] == 2) {
		        continue;
		    } else {
		        System.out.println("uh oh");
		    }
                }
		finalPic[iPix][iRow] = pixel;
            }
        }
//        System.out.println(Arrays.deepToString(finalPic));

        for (int iRow = 0; iRow < 6; iRow ++) {
            String row = "";
            for (int iPix = 0; iPix < 25; iPix ++) {
                if (finalPic[iPix][iRow] == 1) {
                    row += "@";
                } else if (finalPic[iPix][iRow] == 0) {
                    row += " ";
                }
            }
            System.out.println(row);
        }
    }
}
