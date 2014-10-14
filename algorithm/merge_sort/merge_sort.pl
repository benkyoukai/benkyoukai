#!/usr/bin/perl 

use strict;
use warnings;

sub merge_sort {
    my @array = @_;
    return @array if @array < 2;
    my $m = int @array / 2;
    my @a = merge_sort(@array[0 .. $m - 1]);
    my @b = merge_sort(@array[$m .. $#array]);
    for (@array) {
        $_ = !@a            ? shift @b
           : !@b            ? shift @a
           : $a[0] <= $b[0] ? shift @a
           :                  shift @b;
    }
    @array;
}

my @test_array = (5, 3, 1, 7, 2, 6, 4, 10);
warn "original array: ".join(" ", @test_array);
warn "sorted array: ".join(" ", merge_sort(@test_array));
