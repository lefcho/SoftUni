window.addEventListener("load", solve);

function solve() {
  const nameInputElement = document.getElementById('name');
  const phoneInputElement = document.getElementById('phone');
  const categoryInputElement = document.getElementById('category');
  const addButtonElement = document.getElementById('add-btn');
  const checkListElement = document.getElementById('check-list');
  const contactsElement = document.getElementById('contact-list');

  addButtonElement.addEventListener('click', () => {
    let name = nameInputElement.value;
    let phone = phoneInputElement.value;
    let category = categoryInputElement.value;

    if (!name || !phone || !category) {
      return
    }
    checkListElement.appendChild(createLiElemnt(name, phone, category));

    nameInputElement.value = '';
    phoneInputElement.value = '';
    categoryInputElement.value = '';

    const editButtonElement = checkListElement.querySelector('.edit-btn');
    const saveButtonElement = checkListElement.querySelector('.save-btn');

    editButtonElement.addEventListener('click', () => {
      nameInputElement.value = name;
      phoneInputElement.value = phone;
      categoryInputElement.value = category;

      checkListElement.innerHTML = '';
    });

    saveButtonElement.addEventListener('click', () => {
      checkListElement.innerHTML = '';

      const savedContactElement = createLiElemnt(name, phone, category)
      const toDeleteButtonElement = savedContactElement.querySelector('.buttons');
      toDeleteButtonElement.remove();
      const deleteButtonElement = document.createElement('button');
      deleteButtonElement.classList.add('del-btn');
      deleteButtonElement.addEventListener('click', () => {
        savedContactElement.remove();
      })
      savedContactElement.appendChild(deleteButtonElement);
      contactsElement.appendChild(savedContactElement);
    })

  })
  
  function createLiElemnt(name, phone, category) {
    const namePElement = document.createElement('p')
    namePElement.textContent = `name:${name}`;            
    const phonePElement = document.createElement('p');
    phonePElement.textContent = `phone:${phone}`;            
    const categoryPElement = document.createElement('p')
    categoryPElement.textContent = `category:${category}`;

    const articleElement = document.createElement('article');
    articleElement.appendChild(namePElement);
    articleElement.appendChild(phonePElement);
    articleElement.appendChild(categoryPElement);

    const editButtonElemnt = document.createElement('button');
    editButtonElemnt.classList.add('edit-btn');

    const saveButtonelemnt = document.createElement('button');
    saveButtonelemnt.classList.add('save-btn');

    const buttonDivElement = document.createElement('div');
    buttonDivElement.classList.add('buttons');
    buttonDivElement.appendChild(editButtonElemnt);
    buttonDivElement.appendChild(saveButtonelemnt);

    const liElement = document.createElement('li');
    liElement.appendChild(articleElement);
    liElement.appendChild(buttonDivElement);

    return liElement;
  }


  }
  