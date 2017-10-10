package exo4;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Random;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Fenetre extends JFrame implements ActionListener {
	//elements grphiques de la fenetre
	JButton start;
	JButton plus;
	JButton moins;
	JLabel horloge;
	JLabel score;
	//liste contenant les balles a gerer
	Vector<Ball> dessins = new Vector<Ball>() ;
	
	Container contentPane = getContentPane();
	JPanel ballzone = new JPanel() ;
	JPanel buttonzone = new JPanel(new GridLayout(1,10));
	
	Ball test;
	Ball test2;
	
	public boolean pause;
	double minx , miny , maxx , maxy;
	int time;
	int ball_size;
	int score_value;
	int max_ball;
	public Fenetre(String titre ){
		super(titre);
		//parametre de la fenetre
		setLocation(10,150);
		setVisible(true);
		setSize(1600,900);

		ball_size = 10;
		
		//initialisation des boutons et des label
		start = new JButton("Pause");
		plus = new JButton("+");
		moins = new JButton("-");
		horloge = new JLabel("00:00");
		score = new JLabel("0");
		
		start.addActionListener(this);
		plus.addActionListener(this);
		moins.addActionListener(this);
		pause = false;
		
		contentPane.add(buttonzone,BorderLayout.SOUTH);
		contentPane.add(ballzone,BorderLayout.CENTER);
		ballzone.setBackground(new Color(0.5f,0.5f,0.5f));
		//ajout des elements dans les panels
		buttonzone.add(start);
		buttonzone.add(plus);
		buttonzone.add(moins);
		buttonzone.add(horloge);
		buttonzone.add(score);
		minx = contentPane.getBounds().getMinX();
		miny = contentPane.getBounds().getMinY();
		maxx = contentPane.getBounds().getMaxX();
		maxy = contentPane.getBounds().getMaxY();


	    score_value = 0;
		time = 0;
		max_ball = 10;
		repaint();

	}
	
	@Override
	public void paint(Graphics g){
		//fonction servant a rafraichir la fenetre
		super.paint(g);
		score.setText("" + score_value);
		horloge.setText(time + " s");
		
		for(int i=0;i<dessins.size();i++){
		dessins.get(i).draw(g);
		}
	}

	
	@Override
	public void actionPerformed(ActionEvent e) {

		Object source = e.getSource();
		
		//bouton plus
		if(source == plus){
			if(dessins.size() <max_ball) {

			Random test = new Random();
			
			int newx = (int) (minx + (test.nextInt((int) maxx) - minx));
			int newy = (int) (miny + (test.nextInt((int) maxy) - miny));

			float r = (float)test.nextInt((int)10)/10;
			float green= (float)test.nextInt((int)10)/10;
			float b= (float)test.nextInt((int)10)/10;
			Color color = new Color(r,green,b);
			
			int newvx = (int) (-5 + (test.nextInt((int) 5) ));
			int newvy = (int) (-5 + (test.nextInt((int) 5) ));
			dessins.addElement(new Ball(newx,newy,newvx,newvx,10 , minx , miny , maxx , maxy , color));
		}
		}
		//bouton moins

		if(source == moins){
			if(dessins.size() >0) {
			dessins.remove(dessins.size()-1);
			}
		}
		//bouton start

		if(source == start){
			pause = !pause;
			if(pause){
				start.setText("Start");
			}
			else{
				start.setText("Pause");
			}
		}

		// TODO Auto-generated method stub
		
	}





}
