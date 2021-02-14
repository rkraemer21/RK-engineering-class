import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.util.Arrays;

class GridToCharArray {

    String inpFile;

    public GridToCharArray(String inp) throws FileNotFoundException {
        inpFile = inp;
    }

    public char[][] fileHandler() throws FileNotFoundException {
        File inputFile = new File(inpFile);
        Scanner readingFile1 = new Scanner(inputFile);
	ArrayList<char[]> dummy = new ArrayList<char[]>();
	int len = 0;

        while (readingFile1.hasNextLine()) {
	    char[] charFile = readingFile1.nextLine().toCharArray();
	    dummy.add(charFile);
	    len = charFile.length;
	}

        char[][] finalArray = new char[len][dummy.size()];
	int i = 0;
	Scanner readingFile = new Scanner(inputFile);

	while (readingFile.hasNextLine()) {
	    char[] charFile = readingFile.nextLine().toCharArray();
	    finalArray[i] = charFile;
	    i++;
	}

	return finalArray;
    }

    public static char[][] main(String[] args) throws FileNotFoundException {
        GridToCharArray doer = new GridToCharArray(args[0]);
        char[][] readFile = doer.fileHandler();

	return readFile;
    }
}
