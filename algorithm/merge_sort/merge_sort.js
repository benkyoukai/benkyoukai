/**
 * merge sort
 */

function merge_sort(arr, cmp) {
  cmp = cmp || function (x, y) {
    if (x < y) return -1;
    if (x > y) return 1;
    else return 0;
  };

  function sort(arr) {
    var left, right, merged = [];
    var left_length, right_length;

    if(arr.length < 2) return arr;

    left_length = Math.ceil(arr.length / 2);
    left = sort(arr.slice(0, left_length));
    right = sort(arr.slice(left_length));
    right_length = right.length;

    for(var i = 0, j = 0;;) {
      if (i == left_length) {
        [].push.apply(merged, right.slice(j));
        break;
      }

      if (j == right_length) {
        [].push.apply(merged, left.slice(i));
        break;
      }

      if(cmp(left[i], right[j]) < 0) merged.push(left[i++]);
      else merged.push(right[j++]);
    }

    return merged;
  }

  return sort(arr);
}


// test
var test = merge_sort([2,3,4,1,5,6,2,10,13]);
console.log(test);
