//booleans, nested loops, if

import java.util.ArrayList;

public class day4two {

    public static void main(String[] args) {
        int low = 271973;
        int high = 785961;
        ArrayList<Integer> passwords = new ArrayList<Integer> ();

        while (low <= high) {
            String bottom = Integer.toString(low);
            String top = Integer.toString(high);

            boolean check1 = false;
            boolean check2 = false;
            
            //Check for adjacent numbers
            for (int i = 0; i < 5; i++) {
                if (bottom.charAt(i) == (bottom.charAt(i + 1))) {
                    check1 = true;
                }
            }
            
            //Check for decreasing
            for (int i = 0; i < 5; i ++) {
                if (Integer.parseInt(String.valueOf(bottom.charAt(i))) <= Integer.parseInt(String.valueOf(bottom.charAt(i + 1)))) {
                    check2 = true;
                } else {
                    check2 = false;
                    break;
                }
            } 
   
            //Check for both and add to ArrayList of passwords
            if (check1 == true && check2 == true) {
                passwords.add(low);
            }
          
            low ++;
        }
//Part 2 --------------------------------------------------------------------------------------------------------------
        int total = 0;
        for (int password : passwords) {
            String pass = Integer.toString(password);
            System.out.println(pass);
            int check = 0;  
            boolean checkFinal = false;
  
            for (int i = 0; i < 5; i++) {
                if (pass.charAt(i) == pass.charAt(i + 1)) {
                    check ++;
                } else if (check == 1 && pass.charAt(i) != pass.charAt(i + 1)) {
                    checkFinal = true;
                } else if (pass.charAt(i) != pass.charAt(i + 1)) {
                    check = 0;
                }
                if (pass.charAt(5) == pass.charAt(4) && pass.charAt(5) != pass.charAt(3)) {
                    checkFinal = true;
                }
                System.out.println(check + " " + checkFinal);

            }
            if (checkFinal == true) {
                total ++;  
            } 
        }
        System.out.println(total);
    }
}
