UPPER_BOUND = 4000000;
total = 0;
x = 1;
y = 2;
while (y < UPPER_BOUND) {
    if (y % 2 == 0) {
        total += y;
    }
    temp = x + y;
    x = y;
    y = temp;
}
console.log(total);