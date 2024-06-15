const gamesURL = 'http://localhost:3030/jsonstore/games';

const loadGamesButtonElement = document.getElementById('load-games');
const gamesListElemnt = document.getElementById('games-list');
const addGameButttonElement = document.getElementById('add-game');
const gameNameInputElement = document.getElementById('g-name');
const gameTypeInputElement = document.getElementById('type');
const maxPlayersInputElement = document.getElementById('players');
const editGameButtonElement = document.getElementById('edit-game');

let currentGameID;

loadGamesButtonElement.addEventListener('click', loadGames())

addGameButttonElement.addEventListener('click', async () => {
    let gameName = gameNameInputElement.value;
    let gameType = gameTypeInputElement.value;
    let maxPlayers = maxPlayersInputElement.value;

    if (!gameName || !gameType || !maxPlayers) {
        return;
    }
    
    const response = await fetch(gamesURL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
          },
        body: JSON.stringify({
            name: gameName,
            type: gameType,
            players: maxPlayers,
        }),
    })

    if (!response.ok) {
        return;
    }

    loadGames()

    gameNameInputElement.value = '';
    gameTypeInputElement.value = '';
    maxPlayersInputElement.value = '';
})

editGameButtonElement.addEventListener('click', async () => {
    let gameName = gameNameInputElement.value;
    let gameType = gameTypeInputElement.value;
    let maxPlayers = maxPlayersInputElement.value;

    const response = await fetch(`${gamesURL}/${currentGameID}`, {
        method: 'PUT',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name: gameName,
            type: gameType,
            players: maxPlayers,
            _id: currentGameID,
        })
    });

    if (!response.ok) {
        return;
    }

    loadGames();

    editGameButtonElement.setAttribute('disabled', 'disabled');

    addGameButttonElement.removeAttribute('disabled');

    gameNameInputElement.value = '';
    gameTypeInputElement.value = '';
    maxPlayersInputElement.value = '';
    currentGameID = null;

})

async function loadGames() {
    let data = await fetch(gamesURL);
    let games = await data.json();

    gamesListElemnt.innerHTML = '';

    for (const game of Object.values(games)) {

        const namePElement = document.createElement('p')
        namePElement.textContent = game.name;
        const typePElement = document.createElement('p')
        typePElement.textContent = game.type; 
        const playersPElement = document.createElement('p')
        playersPElement.textContent = game.players;        

        const contentDivElement = document.createElement('div')
        contentDivElement.classList.add('content');
        contentDivElement.appendChild(namePElement);
        contentDivElement.appendChild(typePElement);
        contentDivElement.appendChild(playersPElement);
        
        const changeButtonElement = document.createElement('button');
        changeButtonElement.classList.add('change-btn');
        changeButtonElement.textContent= 'Change'
        const deleteButtonElement = document.createElement('button');
        deleteButtonElement.classList.add('delete-btn');
        deleteButtonElement.textContent = 'Delete'

        const buttonsContainerElement = document.createElement('div');
        buttonsContainerElement.classList.add('buttons-container');
        buttonsContainerElement.appendChild(changeButtonElement);
        buttonsContainerElement.appendChild(deleteButtonElement);

        const boardGameElement = document.createElement('div');
        boardGameElement.classList.add('board-game');
        boardGameElement.appendChild(contentDivElement);
        boardGameElement.appendChild(buttonsContainerElement);

        gamesListElemnt.appendChild(boardGameElement);

        changeButtonElement.addEventListener('click', () => {
            gameNameInputElement.value = game.name;
            gameTypeInputElement.value = game.type;
            maxPlayersInputElement.value = game.players;

            currentGameID = game._id;

            editGameButtonElement.removeAttribute('disabled');

            addGameButttonElement.setAttribute('disabled', 'disabled')
        })

        deleteButtonElement.addEventListener('click', async () => {
            await fetch(`${gamesURL}/${game._id}`, {
                method: 'DELETE'
            })

            boardGameElement.remove();
        })
    }
}