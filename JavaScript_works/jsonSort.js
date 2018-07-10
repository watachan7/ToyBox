function jsonSort(){
	var json_data = '{"a":"1","c":"3","b":"2"}';
	var data = JSON.parse(json_data);

	var kekka = objectSort(data);

	var kekka2 : String = '';
	for(key in kekka){
		if (key !== 'checksum'){ 
			if (key !== 'shop_transaction_no') {
				kekka2 += kekka[key];
			}
		}
	}
}