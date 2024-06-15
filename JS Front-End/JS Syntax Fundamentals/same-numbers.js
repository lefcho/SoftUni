function solve(number) {
    let same = true
    let textNumber = number.toString();
    let sum = 0;
    for (let i = 0; i < textNumber.length - 1; i++) {
        if (textNumber[i] !== textNumber[i + 1]) {
            same = false
        }
        sum += Number(textNumber[i]);
    }
    sum += Number(textNumber[textNumber.length - 1]);
}

solve(2222222);
solve(1234);

let str = 'hello';

for (let  i = 0; i < 4; i++) {
    console.log(str[i]);
}