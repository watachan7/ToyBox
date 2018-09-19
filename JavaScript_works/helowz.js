// Jsonの中身
var jsons ={
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
        "itemName": "商品01"
        },
        {
        "itemId": "item02",
        "itemName": "商品02"
        },
        {
        "itemId": "item03",
        "itemName": "商品03"
    }]
};

// jsonを分解する処理
function getValue(obj) {
    if (typeof obj === 'object') {
        var strValue = '';
        for (key in obj) {
            strValue += getValue(obj[key]);
        }
        return strValue;
    } else {
        return obj;
     }
}

// 出力結果
console.log(getValue(jsons));
