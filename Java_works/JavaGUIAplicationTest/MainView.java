package JavaGUIAplicationTest;

import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class MainView extends JFrame {

	public MainView() {

		final JPanel panel1 = new JPanel();
		panel1.setLayout(null);

		panel1.setBounds(0, 0, 375,380);
		panel1.setOpaque(false);

		JPanel panel2 = new JPanel();

		panel2.setLayout(new FlowLayout());

		panel2.setBounds(0, -20,375,380);

		panel2.setBackground(Color.WHITE);
	}
}
