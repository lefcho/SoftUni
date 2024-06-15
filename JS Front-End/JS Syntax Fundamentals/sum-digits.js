function solve(number) {
    let textNumber = number.toString();
    let sum = 0;
    for (let i = 0; i < textNumber.length; i++) {
        sum += Number(textNumber[i]);
    }

    console.log(sum)
}

solve(245678)