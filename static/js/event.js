const addBoardButton = document.querySelector('.addBtn');
const boardsRoute = '/get-boards';
const statusesRoute = '/get-statuses';
const cardsRoute = '/get-cards';
const inputNewBoard = document.getElementById('input-board');
const saveButton = document.querySelector('.saveBtn');
const modal = document.querySelector('.modal');
const container = document.querySelector('#board-container');


addBoardButton.addEventListener('click', ()=>{
    modal.classList.toggle('visible')
})

saveButton.addEventListener('click', ()=>{
    submit_entry(inputNewBoard.value)
    modal.classList.toggle('visible')
    main()
})


//GET
async function apiGet(boardsEndpoint) {
    let data = await fetch(`${boardsEndpoint}`)
    let jsonData = await data.json()
    return jsonData
}

//POST
async function submit_entry(newBoardName) {
    let submitData = {
        'name': `${newBoardName}`
    };
    let response = await fetch(`/new-board/${newBoardName}`, {
        method: "POST",
        mode: "cors",
        cache: "default",
        credentials: "include",
        headers: {"Content-Type": "application/json"},
        redirect: "follow",
        body: JSON.stringify(submitData)
    })
    //callback
    let result = await response.json()
}

async function getBoards(callback) {
        // the boards are retrieved and then the callback function is called with the boards

        // Here we use an arrow function to keep the value of 'this' on dataHandler.
        //    if we would use function(){...} here, the value of 'this' would change.
        let jsonData = await apiGet(boardsRoute)
        callback(jsonData)
}


function showBoards(boards) {
        // shows boards appending them to #boards div
        // it adds necessary event listeners also
    for (let board of boards) {
        let section = document.createElement('section')
            section.classList.add('board')
            section.setAttribute('data-id', `${board.id}`)
        let boardHeader = document.createElement('div')
            boardHeader.classList.add('board-header')
        let title = document.createElement('span')
            title.classList.add('board-title')
            title.innerHTML = `${board.title}`
        let addButton = document.createElement('button')
            addButton.classList.add('board-add')
            addButton.innerHTML = `Add Card`
        let dropDwnButton = document.createElement('button')
            dropDwnButton.classList.add('board-toggle')
            dropDwnButton.innerHTML = '<i class="fas fa-chevron-down"></i>'
        boardHeader.appendChild(title)
        boardHeader.appendChild(addButton)
        boardHeader.appendChild(dropDwnButton)
        section.appendChild(boardHeader)
        container.appendChild(section)
        }
    }


async function getStatuses(callback) {
        // the boards are retrieved and then the callback function is called with the boards

        // Here we use an arrow function to keep the value of 'this' on dataHandler.
        //    if we would use function(){...} here, the value of 'this' would change.
        let jsonData = await apiGet(statusesRoute)
        callback(jsonData)
}


function showStatuses(statuses) {
    // shows boards appending them to #boards div
    // it adds necessary event listeners also
    let sections = document.querySelectorAll('.board')
    for (let section of sections) {
        let boardColumnHolder = document.createElement('div')
        boardColumnHolder.classList.add("board-columns")
        let boardColumn = document.createElement('div')
        boardColumn.classList.add('board-column')
        let boardId = section.getAttribute('data-id') //????
        for (let status of statuses) {
            let boardColTitle = document.createElement('div')
                boardColTitle.classList.add("board-column-title")
                boardColTitle.innerHTML = `${status.title}`
            let boardColContent = document.createElement('div')
                boardColContent.classList.add("board-column-content")
                boardColContent.setAttribute('status-id', `${status.id}`)
                boardColContent.setAttribute('board-id', `${boardId}`)
            boardColumn.appendChild(boardColTitle)
            boardColumn.appendChild(boardColContent)
        }
        boardColumnHolder.appendChild(boardColumn)
        section.appendChild(boardColumnHolder)
    }
}


async function getCards(callback) {
        // the boards are retrieved and then the callback function is called with the boards

        // Here we use an arrow function to keep the value of 'this' on dataHandler.
        //    if we would use function(){...} here, the value of 'this' would change.
        let jsonData = await apiGet(cardsRoute)
        callback(jsonData)
}


function showCards(cards) {
    // shows boards appending them to #boards div
    // it adds necessary event listeners also

    let boardColContents = document.querySelectorAll('.board-column-content')
    for (let boardColContent of boardColContents) {
        let boardId = boardColContent.getAttribute('board-id')
        let statusId = boardColContent.getAttribute('status-id')
        for (let card of cards) {
            if (card.boards_id == +boardId && card.statuses_id == +statusId) {
                let task = document.createElement('div')
                task.classList.add("card")
                let buttonRemove = document.createElement('div')
                buttonRemove.classList.add('card-remove')
                buttonRemove.innerHTML = '<i class="fas fa-trash-alt"></i>'
                let cardTitle = document.createElement('div')
                cardTitle.classList.add('card-title')
                cardTitle.innerHTML = `${card.title}`
                task.appendChild(cardTitle)
                task.appendChild(buttonRemove)
                boardColContent.appendChild(task)
            }
        }
    }
}


function init() {
    getBoards(showBoards)
    getStatuses(showStatuses)
    getCards(showCards)
}

function main(){
    container.innerHTML = ''
    init()






};

main()


