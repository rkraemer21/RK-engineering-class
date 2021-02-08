//importing, while loop, error handling, Files, reading files, arrayLists, ints, instances, printing

import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;
import java.io.FileNotFoundException;

public class arrayer {

    public ArrayList<Integer> theCode(String fileInput) throws FileNotFoundException {
        File inpFile = new File(fileInput);
        Scanner theArrayer = new Scanner(inpFile);
        ArrayList<Integer> theArray = new ArrayList<Integer>();
            
        while (theArrayer.hasNextLine()) {
           String input = theArrayer.nextLine();
           int input2 = Integer.parseInt(input);
           
           theArray.add(input2);
        }

        theArrayer.close();

        return theArray;
    }

    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<Integer> finalArray;
        arrayer finalize = new arrayer();
        finalArray = finalize.theCode(args[0]);
        System.out.println(finalArray);
    }
}
