package sphereParts;
import java.io.File;

public class FileLoaderFactory {
	
	ArrayDataBuilder adb = new ArrayDataBuilder();
	FileWriteFactory fwf = new FileWriteFactory();
	
	// ファイル名をサーチして配列に格納
	public String[] searchFileVolume(String addless) {

		String[] partsBox = new String[1000];
        File file = new File(addless);
        File[] files = file.listFiles();

        for (int i=0; i<files.length; i++) {
        	String sfiles = String.valueOf(files[i]);

        	if (sfiles == null) {
        		partsBox[i] = "";
        	} else {
        		partsBox[i] = sfiles;
        	}
        }
        return partsBox;
	}

	// IFLM(ファイル内のテキストを読み込み、配列にして格納)
	public void idiomFileLoadMaker(){
		
		String addless = "sphere/idiomFile";
		String[] fileNameBox = searchFileVolume(addless);
		
		for (int k=0; k < fileNameBox.length; k++) {
			
			String rechange1 = String.valueOf(fileNameBox[k]);
			String rechange2 = rechange1.replace("\\", "/");
			String rechange3 = rechange2.replace("sphere/", "");
			System.out.println("現在のロードファイル" + rechange3);
			String[] files = adb.loadAndCreate(rechange3);
			
			String varb;
			String read;
			String mean;
			
			for (int i=0; i < files.length;i += 3) {
				
				if (!(files[i]==null)) {
					varb = files[i];
					//fwf.stringWriter("sphere/knowsVocaburary/vocaburary_varb.txt", varb);
					System.out.println("言葉:"+varb);
					
					read = files[i+1];
					//fwf.stringWriter("sphere/knowsVocaburary/vocaburary_leading.txt", read);
					System.out.println("読み:"+ read);
					
					mean = files[i+2];
					//fwf.stringWriter("sphere/knowsVocaburary/vocaburary_mean.txt", mean);
					System.out.println("意味:"+mean);

				} else {
					files[i] = "";

				}
			}

		}
	}
	
	// スフィアの持っている知識・単語。動詞ファイルロードメソッド
	public String[] voc_list(){String[] Box = adb.loadAndCreate3("knowsVocaburary/vocaburary_list.txt");return Box;}
	public String[] voc_varb(){String[] Box = adb.loadAndCreate3("knowsVocaburary/vocaburary_varb.txt");return Box;}
	public String[] voc_end(){String[] Box = adb.loadAndCreate3("knowsVocaburary/vocaburary_ending.txt");return Box;}
	public String[] voc_userSay(){String[] Box = adb.loadAndCreate3("knowsVocaburary/vocaburary_userSay.txt");return Box;}
	public String[] voc_miss(){String[] Box = adb.loadAndCreate3("knowsVocaburary/vocaburary_miss.txt");return Box;}
	
	// 助詞ファイルロードメソッド
	public String[] pos_arrange(){String[] Box = adb.loadAndCreate3("stringJointer/postpositional_arrange.txt");return Box;}
	public String[] pos_assistant(){String[] Box = adb.loadAndCreate3("stringJointer/postpositional_assistant.txt");return Box;}
	public String[] pos_charge(){String[] Box = adb.loadAndCreate3("stringJointer/postpositional_charge.txt");return Box;}
	public String[] pos_connecting(){String[] Box = adb.loadAndCreate3("stringJointer/postpositional_connecting.txt");return Box;}
	public String[] pos_end(){String[] Box = adb.loadAndCreate3("stringJointer/postpositional_end.txt");return Box;}
	public String[] pos_standing(){String[] Box = adb.loadAndCreate3("stringJointer/postpositional_standing.txt");return Box;}
	
	//public String[] knw_(){String[] Box = adb.loadAndCreate("stringJointer/postpositional_standing.txt");return Box;}
}
