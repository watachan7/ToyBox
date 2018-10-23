package sphereParts;

import java.awt.Color;
import java.awt.Dimension;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class CompornentFactory {
	
	// AI-Sphereのパネル
	public JPanel sphere(JTextArea sfias) {

		sfias.setLineWrap(true);
		JPanel jp = new JPanel();
		jp.setBackground(Color.DARK_GRAY);
		jp.setBounds(5, 20, 250, 120);
		JScrollPane sp = new JScrollPane(sfias);
		sp.setPreferredSize(new Dimension(245, 110));
		sfias.setEnabled(false);
		sfias.setDisabledTextColor(Color.BLUE);
		jp.add(sp);

		return jp;
	}
	
	// ユーザーのパネル生成
	public JPanel user(JTextArea users) {

		users.setLineWrap(true);
		JPanel jp = new JPanel();
		jp.setBackground(Color.DARK_GRAY); 
		jp.setBounds(5, 160, 250, 120); 
		JScrollPane sp = new JScrollPane(users);
		sp.setPreferredSize(new Dimension(245, 110));
		jp.add(sp);

		return jp;
	}
	
	// 各ボタンを作成
	public JButton createButton(String ImageName,int setX,int setY,int width,int height){

		final JButton but = new JButton();
		but.setBounds(setX, setY, width, height);
		ClassLoader cl_but = this.getClass().getClassLoader(); 
		ImageIcon Icon = new ImageIcon(cl_but.getResource(ImageName));
		but.setIcon(Icon);

		return but;
	}
}
