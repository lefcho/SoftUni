function solve(input) {
    const wordsCounter = input
        .toLowerCase()
        .split(' ')
        .reduce((result, word) => {
            if (result.hasOwnProperty(word)) {
                result[word] += 1;
            } else {
                result[word] = 1;
            }
            return result;
        }, {})
    
    const correctWords = Object.entries(wordsCounter)
        .reduce((result, word) => {
            if (word[1] % 2 !== 0) {
                result.push(word[0]);
            }
            return result;
        }, [])
    
    console.log(correctWords.join(' '));
        
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')