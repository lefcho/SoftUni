function solve(speed, area) {
    let speedLimit = 0
    let speedingLevel = ''

    switch (area) {
        case 'motorway':
            speedLimit= 130
            break;
        
        case 'interstate':
            speedLimit = 90
            break;
    
        case 'city':
            speedLimit = 50
            break;
    
        case 'residential':
            speedLimit = 20
            break;
    }

    if (speed > speedLimit) {
        let speedDifference = speed - speedLimit;

        if (speedDifference <= 20) {
            speedingLevel = 'speeding'
        } else if (speedDifference <= 40) {
            speedingLevel = 'excessive speeding'
        } else {
            speedingLevel = 'reckless driving'
        }

        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedLimit} - ${speedingLevel}`)

    } else {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`)
    }

}



solve(40, 'city')
solve(21, 'residential')
solve(120, 'interstate')
solve(200, 'motorway')