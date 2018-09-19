/*
 *　提出用コード『JSONのBase64変換・復元』
 */

// 対象のJSON
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

// base64変換のための文字列
var base64list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';

// jsonを再帰的に分解する処理
function getValue(obj) {
    if (typeof obj === 'object') {
        var strValue = '';
        for (key in obj) {
            strValue += getValue(obj[key]);
            strValue += ',';
        }
        return strValue;
    } else {
        return obj;
    }
}

// Base64エンコーディング
function base64encode(str) {
    var t = '',
        p = -6,
        a = 0,
        i = 0,
        v = 0,
        c;

    while ((i < str.length) || (p > -6)) {
        if (p < 0) {
            if ( i < str.length ) {
                c = str.charCodeAt(i++);
                v += 8;
            } else {
                c = 0;
            }
            a = ((a　&　255)　<<　8)　|　(c　&　255);
            p += 8;
        }
        t += base64list.charAt((v > 0)? (a　>>　p)　&　63 : 64)
        p -= 6;
        v -= 6;
    }
    return t;
}

// Base64デコーディング
function base64decode(str) {
    var t = '',
        p = -8,
        a = 0,
        c,
        d;

    for(var i=0; i < str.length; i++) {
        if ((c = base64list.indexOf(str.charAt(i))) < 0)
            continue;
            a = (a　<<　6)　|　(c　&　63);
            
        if ((p += 6) >= 0) {
            d = (a　>>　p)　&　255;

        if (c != 64)
            t += String.fromCharCode(d);
            a &= 63;
            p -= 8;
        }
    }
    return t;
}

// 出力結果：元々の文字列
var jsonstr = getValue(jsons);
console.log('元々の文字列：' + jsonstr);

// 出力結果：Base64エンコード変換結果
var encode = base64encode(jsonstr);
console.log('Base64エンコード変換：' + encode);

// 出力結果：Base64デコード復元結果
var decode = base64decode(encode);
console.log('Base64デコード復元：' + decode);