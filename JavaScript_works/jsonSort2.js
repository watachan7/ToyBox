function getValue(obj) {
    if (typeof obj === 'object') {
        var strValue = '';
        for (key in obj) {
        	var aazaz = key;
        	if (key !== 'shop_transaction_no') {
        		if (key !== 'checksum') {
            		strValue += getValue(obj[key]);
        		}
        	}
        }
        return strValue;
    } else {
        return obj;
    }
}