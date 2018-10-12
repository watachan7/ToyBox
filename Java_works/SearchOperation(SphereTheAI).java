package sphereParts;

import javax.swing.JTextArea;

public class SearchOperation {

	/**
	*vocaburaryファイルをロード
	*/
	public static String[] operation1(JTextArea user, JTextArea sfia) {

		ArrayDataBuilder adb = new ArrayDataBuilder();
		String userIdea = user.getText();
		String[] ideaChank = adb.messageReorganization(userIdea);
		String fileName = "vocaburary_list.txt";
		String[] item = adb.loadAndCreate(fileName);

		if (!(item == null)) {

			String[] searchs = adb.searchAndMake(item, ideaChank);
			return searchs;

		}

		return null;
	}

	//public static void operation2(String[] txts) {}
	
}