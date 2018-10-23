import javax.swing.JFrame;

public class SystemStart extends JFrame{
	public static void main(String[] args){
		
		JFrame frame = new JFrame();
		frame.setTitle("メモ帳");
		frame.setLayout(null);
		frame.setBounds(0,0,540,490);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setResizable(false);
		frame.setVisible(true);
		
	}
}