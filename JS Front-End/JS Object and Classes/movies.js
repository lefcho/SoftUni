function solve(input) {
    let movies = []

    for (const line of input) {
        if (line.includes('addMovie ')) {
            let movieName = line.substring(9);
            let movie = {
                name: movieName,
            }
            movies.push(movie);
        } else if (line.includes(' directedBy ')) {
            const [movieName, director] = line.split(' directedBy ');
            const movie = movies.find(m => m.name === movieName);

            if(movie) {
                movie.director = director; 
        }
        } else if (line.includes(' onDate ')) {
            const [movieName, date] = line.split(' onDate ');
            const movie = movies.find(m => m.name === movieName);

            if(movie) {
                movie.date = date; 
            }
        }
    }
    for (const movie of movies) {
        if (movie.director && movie.date) {
            console.log(JSON.stringify(movie));
        }
    }
}

solve(['addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ]
    )