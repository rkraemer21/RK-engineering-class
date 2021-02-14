import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;

class NumsToArrayList {

    String inpFile;

    public NumsToArrayList(String inp) throws FileNotFoundException {
        inpFile = inp;
    }

    public ArrayList<Integer> fileHandler() throws FileNotFoundException {
        File inputFile = new File(inpFile);
        Scanner readingFile = new Scanner(inputFile);
        char[] charFile = readingFile.nextLine().toCharArray();
//        System.out.println(charFile);
        ArrayList<Integer> finalArray = new ArrayList<Integer>();

        for (char character : charFile) {
            finalArray.add(Character.getNumericValue(character));
        }
//        System.out.println(finalArray);

        return finalArray;
    }

    public static ArrayList<Integer> main(String[] args) throws FileNotFoundException {
        NumsToArrayList doer = new NumsToArrayList(args[0]);
        ArrayList<Integer> readFile = doer.fileHandler();
        return readFile;
    }
}
