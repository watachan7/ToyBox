package sphereParts;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class LogFileRecording {
	
	DateManager dm = new DateManager();
	private String filename;
	
	// ログファイルを作成する
	public void logFileMake() {

		String d = dm.toDate();
		String t = dm.toTime();
	    File newfile = new File("sphere/memoryFile/memory"+ d + t + ".txt");
	    setFilename(newfile + "");

	    try {
	    	if (newfile.createNewFile()) {

	    	} else {

	    	}

	    } catch (IOException e) {
	    	//TODO:return動作
	    }

	}

	// ファイルに書き込む
	public void logMemorySet(String phreas, String talkings) {

		try {
	        FileWriter fstring = new FileWriter(this.filename, true);
	        fstring.write(talkings + "：" + phreas + "\r\n");
	        fstring.close();

	    } catch (IOException e) {
	    	//TODO:return動作
	    }

	}

	// ファイル名をセット
	public void setFilename(String newName){
		this.filename = newName;
		
	}

}
