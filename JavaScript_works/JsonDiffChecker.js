var json1 ={
    "masterNumber": 10000,
    "code": "m-001",
    "customerData": {
        "name": "Jiro",
        "age": 45
    },
    "Address": [{
        "name": "testAreport",
        "email": "tA@sample.co.jp"
    }],
    "items": [{
        "itemId": "item01",
        "itemName": "item01"
        },
        {
        "itemId": "item02",
        "itemName": "item02"
        },
        {
        "itemId": "item03",
        "itemName": "item03"
    }]
};

var json2 ={
    "masterNumber": 10000,
    "code": "m-001",
    "customerData": {
        "name": "Jiro",
        "age": 45
    },
    "Address": [{
        "name": "testAreport",
        "email": "tA@sample.co.jp"
    }],
    "items": [{
        "itemId": "item01",
        "itemName": "item01"
        },
        {
        "itemId": "item02",
        "itemName": "item02"
        },
        {
        "itemId": "item03",
        "itemName": "item03"
    }]
};

function compareObj(obja, objb) {
	console.log(obja);
    for (var key in obja) {
    	if (obja[key] != null) {
	        if (typeof obja[key] == 'object') {
	            if (!compareObj(obja[key], objb[key])) return false;
	        } else {
	            if (obja[key] != objb[key]) return false;
	        }
    	}
    }
    return true;
}

// 出力結果：True or False
var result = compareObj(json1, json2);
console.log('結果：' + result);