package sphereParts;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class ArrayDataBuilder {
	
	/**
	 * 「文字列を検索する」送られてきた文字を1文字ずつ検証し、配列に格納して返す
	 */
	public String[] searchAndMake(String[] item, String[] message) {
		String[] itemBox = new String[1000];
		String chank = "";
		for (int i = 0; i < message.length; i++) {
			if (message[i] == null) {message[i] = "";}
			chank += message[i];
			for (int j = 0; j < item.length; j++) {
				if (chank.equals(item[j])) {
					for (int k = 0; k < itemBox.length; k++) {if (chank.equals(item[k])) {itemBox[k] = chank;}}
				}
			}
		}return itemBox;
	}
	
	/**
	 * 「文字列をミンチにする」受け取った文字列をchar単位に分解して配列に格納して返す
	 */
	public String[] messageReorganization(String message) {
		String[] chank = new String[1000];
		for (int i = 0; i < message.length(); i++) {
			chank[i] = String.valueOf(message.charAt(i));
		}return chank;
	}
	
	/**
	 * 「ファイル内容を配列に入れる」txtファイルをロードし、内容を配列に格納する
	 */
	public String[] loadAndCreate(String fileName) {
		BufferedReader bf = null;
		String[] inputItem = new String[1000];
		try {
			InputStream is = getClass().getClassLoader().getResourceAsStream(fileName);
			bf = new BufferedReader(new InputStreamReader(is, "UTF-8"));
			String str = null;
			for (int i = 0; (str = bf.readLine()) != null; i++) {inputItem[i] = str;}
			for (int i = 0; i < inputItem.length; i++) {
				if (inputItem[i] == null) {inputItem[i] = "";}
			}bf.close();}
		catch (FileNotFoundException e) {return null;} 
		catch (NullPointerException e) {return null;} 
		catch (IOException e) {return null;}
		return inputItem;
	}
	/**
	 * ver2(指定ファイルの内容が決まっている時)
	 */
	public String[] loadAndCreate2(String fileName,int arraynum) {
		BufferedReader bf = null;
		String[] inputItem = new String[arraynum];
		try {
			InputStream is = getClass().getClassLoader().getResourceAsStream(fileName);
			bf = new BufferedReader(new InputStreamReader(is, "UTF-8"));
			String str = null;
			for (int i = 0; (str = bf.readLine()) != null; i++) {inputItem[i] = str;}
			for (int i = 0; i < inputItem.length; i++) {
				if (inputItem[i] == null) {inputItem[i] = "";}
			}bf.close();}
		catch (FileNotFoundException e) {return null;} 
		catch (NullPointerException e) {return null;} 
		catch (IOException e) {return null;}
		return inputItem;
	}
	// ファイルをロードして配列に返還
	public String[] loadAndCreate3(String addless){
		int line = LineGetters(addless);
		String[] Box = loadAndCreate2(addless,line);return Box;
	}
	// ファイルをロードしてその行数を取得
	public int LineGetters(String fileName){
		BufferedReader bf = null;
		int count = 0;
		try {
			InputStream is = getClass().getClassLoader().getResourceAsStream(fileName);
			bf = new BufferedReader(new InputStreamReader(is, "UTF-8"));
			String str = null;
			for (int i = 0; (str = bf.readLine()) != null; i++) {
				count = count + 1;
			}bf.close();}
		catch (Exception e) {}
		return count;
	}

	/**
	 * * ユーザのメッセージを分析して主語を見つけ出す
	 */
	public String[] searchSubject(String explain) {
		String[] subject = loadAndCreate("Subject.txt");
		String[] subBox = new String[1000];
		for (int i = 0; i < subject.length; i++) {
			if (explain.matches(".*" + subject[i] + ".*")) {subBox[i] = subject[i];}
		}return subBox;
	}
	
	public void p(String str) {
		System.out.println(str);
		System.out.println();
	}
}
