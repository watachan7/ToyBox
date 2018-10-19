package sphereParts;

public class UserCertification {
	
	// ArrayDataBuilderインスタンス
	static ArrayDataBuilder adb = new ArrayDataBuilder();
   	/** 
	 * UserNameを判断
	 * */
	public static boolean who(String user){
		
		// userNameファイルをロードしてユーザ名を確認
		String[] users = adb.loadAndCreate("userFiles/userName.txt");
		
		// ユーザーを検索
		for(String point : users){
			
			// ノーヒット
			if (point == null){
				// 何もしない
				
			// ヒット
			} else if (point.equals(user)) {
				
				// ユーザープロファイルをロードして各パラメータを配列に格納
	        	String[] userState = adb.loadAndCreate("userFiles/" + user + ".txt");
	        	
	        	final int funnyPoint = Integer.parseInt(userState[0]);Sphere.setFunny(funnyPoint);
	        	final int sadPoint = Integer.parseInt(userState[1]);Sphere.setSad(sadPoint);
	        	final int anglyPoint = Integer.parseInt(userState[2]);Sphere.setAngly(anglyPoint);
	        	final String usern = userState[3];Sphere.setUser(usern);
	        	
	        	return true;
			} 
		}

		return true;
		
	}

}