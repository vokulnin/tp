package exo4;

public class Main {

	public static void main(String[] args) {

		Fenetre f = new Fenetre("fenetre");
		Ball_supervisor s = new Ball_supervisor(f);
		Affiche a = new Affiche(f);
		Timer t = new Timer(f);
		a.start();s.start();
		t.start();
	}

}
