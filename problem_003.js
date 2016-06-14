number = 600851475143;
index = 2;

while (number > 1) {
    while (number % index == 0) {
        number /= index;
    }
    index += 1;
}
console.log(index-1);