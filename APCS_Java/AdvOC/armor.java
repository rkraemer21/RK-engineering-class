class armor {
    protected String name;
    protected int level;
    protected int strength;
    protected int discipline;
    protected int intellect;

    armor(String nm, int lvl, int strngth, int disc, int intllct) {
        this.name = nm;
	this.level = lvl;
	this.strength = strngth;
	this.discipline = disc;
	this.intellect = intllct;
    }

    public String getDescription() {
        return "A sturdy piece of armor";
    }

    public String stats() {
	String lvl = Integer.toString(level);
        String strngth = Integer.toString(strength);
	String disc = Integer.toString(discipline);
	String intllct = Integer.toString(intellect);
	String overlay = "Level: " + lvl + " /// >Strength: " + strngth + " >Discipline: " + disc + " >Intellect: " + intllct + "\n";
	return overlay;
    }

}
