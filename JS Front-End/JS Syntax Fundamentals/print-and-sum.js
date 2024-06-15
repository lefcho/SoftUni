function solve (start, end) {
    let result1 = '';
    sum = 0;
    for (let i = start; i <= end; i++) {
        result1 += `${i} `;
        sum += i;
    }

    console.log(result1);
    console.log(`Sum: ${sum}`);
}

solve(5, 10);
solve(0, 26);