import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

class day4 {

    Scanner starter;

    public day4(String[] args) throws FileNotFoundException {
        File inpFile = new File(args[0]);
        starter = new Scanner(inpFile); 
    }

    public int finder() {
        int amt = 0;
	boolean check = false;
	int total = 0;
        while (starter.hasNextLine()) {
            //System.out.println(starter.nextLine());
	    String x = starter.nextLine();
	    int count = x.length() - x.replaceAll(":","").length();
	    System.out.println(count + "-" + amt);
	    amt += count;

	    if (x.contains("cid")) {
	        check = true;
	    }

	    //System.out.println(check);

	    if (count == 0 || !starter.hasNextLine()) {
	        if (amt < 7) {
		} else if (amt == 8) {
		    total ++;
		    System.out.println("trig8-add");
		} else if (amt == 7) {
		    if (check == false) {
		        total ++;
			System.out.println("trig7-add");
		    } 
		}
		amt = 0;
		check = false;
	    } 
	}
	return total;
    }

    public static void main(String[] args) throws FileNotFoundException {
        day4 doer = new day4(args);
	int done = doer.finder();
	System.out.println("total" + done);
    }
}
