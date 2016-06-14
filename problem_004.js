start = 999 * 999;
end = 100 * 100;
hasAnswer = false;

for (x = start; x >= end && !hasAnswer; x--) {
    curr = x.toString();
    if (curr.charAt(0) == curr.charAt(curr.length - 1) && 
        curr.charAt(1) == curr.charAt(curr.length - 2) &&
        curr.charAt(2) == curr.charAt(curr.length - 3)) {
        for (y = 100; y <= 999 && !hasAnswer; y++) {
            if (x % y == 0 && x/y <= 999 && x/y >= 100) {
                console.log(x);
                hasAnswer = true;
            }
        }   
    }
}