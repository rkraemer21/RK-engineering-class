class tell {
    private void teller(armor piece) {
        System.out.println("\n" + piece.name + " ~~~ " + piece.getDescription());
        System.out.println(piece.stats());
    }

    public static void main(String[] args) {
        tell thisPiece = new tell();
	armor InsMount = new helmet();
	armor TwiG = new chest();

	thisPiece.teller(InsMount);
	thisPiece.teller(TwiG);
    }
}
