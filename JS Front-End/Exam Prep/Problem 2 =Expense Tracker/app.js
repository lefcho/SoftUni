window.addEventListener("load", solve);

function solve() {
    const expenseInputElement = document.getElementById('expense');
    const amountInputElement = document.getElementById('amount');
    const dateInputElement = document.getElementById('date');
    const addButtonElement = document.getElementById('add-btn');
    const previewListElement = document.getElementById('preview-list');
    const expensesElemnt = document.getElementById('expenses-list');
    const deleteButtonElement = document.querySelector('.btn.delete');

    deleteButtonElement.addEventListener('click', () => {
        expensesElemnt.innerHTML = '';
    })

    addButtonElement.addEventListener('click', () => {
        const expense = expenseInputElement.value;
        const amount = amountInputElement.value;
        const date = dateInputElement.value;

        if (!expense || !amount || !date) {
            return;
        }

        previewListElement.appendChild(createLiExpenseItemElement(expense, amount, date));
        addButtonElement.setAttribute('disabled', 'disapbled');

        expenseInputElement.value = '';
        amountInputElement.value = '';
        dateInputElement.value = '';

        const editButtonElement = previewListElement.querySelector('.edit')
        editButtonElement.addEventListener('click', () => {
            previewListElement.innerHTML = '';
            expenseInputElement.value = expense;
            amountInputElement.value = amount;
            dateInputElement.value = date;

            addButtonElement.removeAttribute('disabled');
        })

        const okButtonElement = previewListElement.querySelector('.ok');
        okButtonElement.addEventListener('click', () => {
            previewListElement.innerHTML = '';

            const articleFinishedElement =  createLiExpenseItemElement(expense, amount, date);
            const buttonElement = articleFinishedElement.querySelector('.buttons');
            buttonElement.remove();
            expensesElemnt.appendChild(articleFinishedElement);
            addButtonElement.removeAttribute('disabled');
        })
    });

    function createLiExpenseItemElement(expense, amount, date) {
        const expensePElement = document.createElement('p')
        expensePElement.textContent = `Type: ${expense}`;            
        const amountPElement = document.createElement('p');
        amountPElement.textContent = `Amount: ${amount}$`;            
        const datePElement = document.createElement('p')
        datePElement.textContent = `Date: ${date}`;

        const articleElement = document.createElement('article');
        articleElement.appendChild(expensePElement);
        articleElement.appendChild(amountPElement);
        articleElement.appendChild(datePElement);

        const editButtonElemnt = document.createElement('button');
        editButtonElemnt.classList.add('btn', 'edit');
        editButtonElemnt.textContent = 'edit';

        const okButtonelemnt = document.createElement('button');
        okButtonelemnt.classList.add('btn', 'ok');
        okButtonelemnt.textContent = 'ok';

        const buttonDivElement = document.createElement('div');
        buttonDivElement.classList.add('buttons');
        buttonDivElement.appendChild(editButtonElemnt);
        buttonDivElement.appendChild(okButtonelemnt);

        const liExpenseItemElement = document.createElement('li');
        liExpenseItemElement.classList.add('expense-item');
        liExpenseItemElement.appendChild(articleElement);
        liExpenseItemElement.appendChild(buttonDivElement);

        return liExpenseItemElement;
    }
}
