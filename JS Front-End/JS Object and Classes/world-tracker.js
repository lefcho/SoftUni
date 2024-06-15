function solve(input) {
    const searchWords = input
        .shift()
        .split(' ')
        .reduce((result, word) => ({...result, [word]: 0}), {});

        for (const word of input) {
            if (searchWords.hasOwnProperty(word)) {
                searchWords[word] += 1;
            }           
        }

        Object.entries(searchWords)
            .sort((a, b) => b[1]- a[1])
            .forEach(([word, occurrences]) => console.log(`${word} - ${occurrences}`));

}

solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
    )