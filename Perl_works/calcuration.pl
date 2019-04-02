#!/usr/bin/perl

use strict;
use warnings;

if (@ARGV == 3){
  my $sum1 = $ARGV[0];
  my $operator = $ARGV[1];   
  my $sum2 = $ARGV[2];
  my $result = eval $sum1.$operator.$sum2;

  print "結果：$result\n";

} else {

  print "引数を1 + 1と指定して下さい\n";

}
