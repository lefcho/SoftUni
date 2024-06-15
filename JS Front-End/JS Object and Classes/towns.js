function solve(towns) {
    let townsParams = []
    for (const townInfo of towns   ) {
        let townArray = townInfo.split(' | ')
        let townObj = {
            town: townArray[0],
            latitude: Number(townArray[1]).toFixed(2),
            longitude: Number(townArray[2]).toFixed(2),
        }
        townsParams.push(townObj);
    }
    for (const town of townsParams) {
        console.log(town);
    }
}

solve(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625'])

solve(['Plovdiv | 136.45 | 812.575'])