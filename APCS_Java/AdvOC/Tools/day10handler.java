import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.util.Arrays;

class day10handler {

    String inpFile;

    public day10handler(String inp) throws FileNotFoundException {
        inpFile = inp;
    }

    public char[][] fileHandler() throws FileNotFoundException {
        File inputFile = new File(inpFile);
        Scanner readingFile = new Scanner(inputFile);
        char[][] finalArray = new char[21][21];
	int i = 0;

	while (readingFile.hasNextLine()) {
	    char[] charFile = readingFile.nextLine().toCharArray();
	    finalArray[i] = charFile;
	    i++;
	}

	return finalArray;
    }

    public static char[][] main(String[] args) throws FileNotFoundException {
        day10handler doer = new day10handler(args[0]);
        char[][] readFile = doer.fileHandler();

	return readFile;
    }
}
