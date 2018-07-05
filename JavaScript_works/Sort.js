function sort() {

  var crashName = 'whatanca';
  var ArrayCrashName = crashName.split('');
  
  ArrayExactName = ArrayCrashName.sort(function (a, b) {
    a = a.toString().toLowerCase();
    b = b.toString().toLowerCase();
    return (a > b) ?  1 :
         (b > a) ? -1 : 0;
  });
  
  var myName = ArrayExactName.join('');// watachan
}