function solve(commands) {
    const gunslingersCount = Number(commands.shift());
    const gunslingers = {}
    
    for (i = 0; i < gunslingersCount; i++) {
        let [gunslingerName, startingHP, startingBullets] = commands.shift().split(' ');
        gunslingers[gunslingerName] = {
            hitPoints: Number(startingHP),
            bullets: Number(startingBullets)
        }
    }


    let command = commands.shift()

    while (command !== 'Ride Off Into Sunset') {
        let splitCommands = command.split(' - ');
        let mainCommand = splitCommands.shift();

        switch (mainCommand) {
            case 'FireShot':
                let [gunslinger, target] = splitCommands;
                if (gunslingers[gunslinger].bullets <= 0) {
                    console.log(`${gunslinger} doesn't have enough bullets to shoot at ${target}!`);
                } else {
                    gunslingers[gunslinger].bullets -= 1;
                    console.log(`${gunslinger} has successfully hit ${target} and now has ${gunslingers[gunslinger].bullets} bullets!`);
                }
                break;
            case 'TakeHit':
                let [gunslingerName, damage, attacker] = splitCommands;
                if (gunslingers[gunslingerName].hitPoints - Number(damage) <= 0) {
                    delete(gunslingers[gunslingerName]);
                    console.log(`${gunslingerName} was gunned down by ${attacker}!`);
                } else {
                    gunslingers[gunslingerName].hitPoints -= Number(damage);
                    console.log(`${gunslingerName} took a hit for ${damage} HP from ${attacker} and now has ${gunslingers[gunslingerName].hitPoints} HP!`);
                }
                break;
            case 'Reload':
                let [characterName] = splitCommands;
                if (gunslingers[characterName].bullets === 6) {
                    console.log(`${characterName}'s pistol is fully loaded!`);
                } else {
                    let bulletsReloaded = 6 - gunslingers[characterName].bullets;
                    gunslingers[characterName].bullets = 6;
                    console.log(`${characterName} reloaded ${bulletsReloaded} bullets!`);
                }
                break;
            case 'PatchUp':
                let [character, amountHP] = splitCommands;
                if (gunslingers[character].hitPoints === 100) {
                    console.log(`${character} is in full health!`);
                } else {
                    let recoveredHP;
                    if (gunslingers[character].hitPoints + Number(amountHP) > 100) {
                        recoveredHP = 100 - gunslingers[character].hitPoints;
                        gunslingers[character].hitPoints = 100;
                    } else {
                        recoveredHP = Number(amountHP);
                        gunslingers[character].hitPoints += Number(amountHP);
                    }
                    console.log(`${character} patched up and recovered ${recoveredHP} HP!`);
                }
                break;
        }
        command = commands.shift()
    }

    for (const gunslinger in gunslingers) {
        console.log(gunslinger);
        console.log(` HP: ${gunslingers[gunslinger].hitPoints}`);
        console.log(` Bullets: ${gunslingers[gunslinger].bullets}`);
    }
}

