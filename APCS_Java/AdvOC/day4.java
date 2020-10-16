public class day4 {

    public static void main(String[] args) {
        int low = 271973;
        int high = 785961;
        int total = 0;

        while (low <= high) {
            String bottom = Integer.toString(low);
            String top = Integer.toString(high);

            System.out.println(bottom + "-" + top);
            boolean check1 = false;
            boolean check2 = false;

            for (int i = 0; i < 5; i++) {
                if (bottom.charAt(i) == (bottom.charAt(i + 1))) {
                    check1 = true;
                }
            }

            for (int i = 0; i < 5; i ++) {
                if (Integer.parseInt(String.valueOf(bottom.charAt(i))) <= Integer.parseInt(String.valueOf(bottom.charAt(i + 1)))) {
                    check2 = true;
                } else {
                    check2 = false;
                    break;
                }
            } 
   
            if (check1 == true && check2 == true) {
                System.out.println("~~~~ TRUE ~~~~");
                total ++;
            }
          
            low ++;
        }
        System.out.println(total);             
    }
}
