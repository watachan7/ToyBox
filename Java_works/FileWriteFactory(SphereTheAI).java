package sphereParts;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

/**
 * FileWriteFactory
 */
public class FileWriteFactory {

	// ファイルアドレスと書き込み用の文字列を受け取り、ファイルに書き込む
	public void fileWrite(String addless,String str) {
		try {
			File file = new File(addless);
			FileWriter filewriter = new FileWriter(file, true);
			filewriter.write(str + "¥r¥n");
			filewriter.close();
	    } catch (IOException e) {
	    	System.out.println("FileWriteFactory_fileWrite_Error:" + e);
	    	
	    }
	}
	
}
