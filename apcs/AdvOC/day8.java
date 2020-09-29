import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.util.Arrays;

class day8 {

    public static void main(String[] args) throws FileNotFoundException {
//        int[][][] picture = new int[25][6][100];
        int[][] layers = new int[150][100];
        ArrayList<Integer> theNumbers = numSplitter.main(args);

        for (int i2 = 0; i2 < 100; i2 ++) {
            int zeroes = 0;
            int ones = 0;
            int twos = 0;
            for (int i3 = 0; i3 < 150; i3 ++) {
                int newI = i3 + 150 * i2;
                layers[i3][i2] = theNumbers.get(newI);
                if (theNumbers.get(newI) == 0) {
                    zeroes ++;
                } else if (theNumbers.get(newI) == 1) {
                    ones ++;
                } else if (theNumbers.get(newI) == 2) {
                    twos ++;
                }
            }
            System.out.println(i2 + " " + zeroes + " " + ones * twos);
        }
        System.out.println(Arrays.deepToString(layers));
    }
}
