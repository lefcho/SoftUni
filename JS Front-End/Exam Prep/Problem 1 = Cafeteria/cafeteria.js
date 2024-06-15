function solve(commands) {
    const baristasCount = commands.shift();
    const baristas = {}
    
    for (i = 0; i < baristasCount; i++) {
        [baristaName, shift, skills] = commands.shift().split(' ');
        baristas[baristaName] = {
            shift,
            drinks : skills.split(',')
        }
    }

    let command = commands.shift()

    while (command !== 'Closed') {
        let splitCommands = command.split(' / ');
        let mainCommand = splitCommands.shift();

        if (mainCommand === 'Prepare') {
            [currentBarista, currentShift, coffeOrdered] = splitCommands;
            if (baristas[currentBarista].shift === currentShift && baristas[currentBarista].drinks.includes(coffeOrdered)) {
                console.log(`${currentBarista} has prepared a ${coffeOrdered} for you!`);
            } else {
                console.log(`${currentBarista} is not available to prepare a ${coffeOrdered}.`);
            }
        } else if (mainCommand === 'Change Shift') {
            [currentBarista, currentShift] = splitCommands;
            baristas[currentBarista].shift = currentShift;
            console.log(`${currentBarista} has updated his shift to: ${currentShift}`);
        } else if (mainCommand === 'Learn') {
            [currentBarista, newDrink] = splitCommands;
            if (baristas[currentBarista].drinks.includes(newDrink)) {
                console.log(`${currentBarista} knows how to make ${newDrink}.`);
            } else {
                baristas[currentBarista].drinks.push(newDrink);
                console.log(`${currentBarista} has learned a new coffee type: ${newDrink}.`);
            }
        }
        command = commands.shift()

    }
    
    for (const barista in baristas) {
        console.log(`Barista: ${barista}, Shift: ${baristas[barista].shift}, Drinks: ${baristas[barista].drinks.join(', ')}`);
    }

}

solve([
    '3',
      'Alice day Espresso,Cappuccino',
      'Bob night Latte,Mocha',
      'Carol day Americano,Mocha',
      'Prepare / Alice / day / Espresso',
      'Change Shift / Bob / night',
      'Learn / Carol / Latte',
      'Learn / Bob / Latte',
      'Prepare / Bob / night / Latte',
      'Closed']
    )

console.log('___---------------____________---------_______');

solve(['4',
'Alice day Espresso,Cappuccino',
'Bob night Latte,Mocha',
'Carol day Americano,Mocha',
'David night Espresso',
'Prepare / Alice / day / Espresso',
'Change Shift / Bob / day',
'Learn / Carol / Latte',
'Prepare / Bob / night / Latte',
'Learn / David / Cappuccino',
'Prepare / Carol / day / Cappuccino',
'Change Shift / Alice / night',
 'Learn / Bob / Mocha',
'Prepare / David / night / Espresso',
'Closed']
)