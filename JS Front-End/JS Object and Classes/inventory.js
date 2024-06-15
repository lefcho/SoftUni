function solve(input) {
    let heroes = []
    for (const hero of input) {
        const [heroName, level, items] = hero.split(' / ');

        const heroInfo = {
            name: heroName,
            level: Number(level),
            items,
        }
        heroes.push(heroInfo)
    }

    heroes.sort((a, b) => {
        return a.level - b.level;
    });

    heroes.forEach(hero => console.log(`Hero: ${hero.name}\nlevel => ${hero.level}\nitems => ${hero.items}`));
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ]
    )