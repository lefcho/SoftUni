function solve(numberStr, c1, c2, c3, c4, c5) {

    number = Number(numberStr);
    let operations = c1[0] + c2[0] + c3[0] + c4[0] + c5[0];
    for (let i = 0; i < 5; i++) {
        switch (operations[i]) {
            case 'c':
                number /= 2;
                break;
            case 'd':
                number = Math.sqrt(number)
                break;
            case 's':
                number += 1;
                break;
            case 'b':
                number *= 3;
                break;
            case 'f':
                number = 0.8 * number;
                break;
    
            
        }
        console.log(number)
    }

}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet');