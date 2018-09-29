var base64list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';

function base64encode(s) {
    var t = '', p = -6, a = 0, i = 0, v = 0, c;

    while ( (i < s.length) || (p > -6) ) {
        if ( p < 0 ) {
            if ( i < s.length ) {
                c = s.charCodeAt(i++);
                v += 8;
            } else {
                c = 0;
            }
            a = ((a&255)<<8)|(c&255);
            p += 8;
        }
        t += base64list.charAt( ( v > 0 )? (a>>p)&63 : 64 )
        p -= 6;
        v -= 6;
    }
    return t;
}

function base64decode(s) {
    var t = '', p = -8, a = 0, c, d;

    for( var i = 0; i < s.length; i++ ) {
        if ( ( c = base64list.indexOf(s.charAt(i)) ) < 0 )
            continue;
            a = (a<<6)|(c&63);
            
        if ( ( p += 6 ) >= 0 ) {
            d = (a>>p)&255;

        if ( c != 64 )
            t += String.fromCharCode(d);
            a &= 63;
            p -= 8;
        }
    }
    return t;
}
