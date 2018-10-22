package sphereParts;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

/**
 * 本日の日付・時間を取得して返す
 * @author trio
 */
public class DateManager {
	
	// 日付を取得して渡す
	public String toDate() {	

	    Date date = new Date();
	    SimpleDateFormat today = new SimpleDateFormat("yyyyMMdd");

	    return today.format(date);
	}

	// 時間を取得して返す
	public String toTime() {

		Calendar now = Calendar.getInstance();
		int h = now.get(Calendar.HOUR_OF_DAY);
		int m = now.get(Calendar.MINUTE);
		int s = now.get(Calendar.SECOND);

		return ""+h+m+s+"";
	}
	
}