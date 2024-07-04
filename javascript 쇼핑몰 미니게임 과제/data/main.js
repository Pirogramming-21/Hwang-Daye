function loadItems(){
  return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

function displayItems(items){
    const container=document.querySelectior('.items');
    //const html = items.map(item => createHTMLString(item));
    contaniner.innerHTML = items.map(item => createHTMLString(item)).join('');
}

function createHTMLString(item){
  return `
    <li class="item">
        <img src="${item.image}" alt="{$item.type}" class="item__thumbnail" />
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;

}

function onButtonClick(event,items){
      const dataset = event.target.dataset;
      const key = dataset.key;
      const value = dataset.value;

      if(key==null || value ==null){
        return;
      }
      displayItems(items.filter(item => item[key] ===value));

}

function setEventListeners(items){
    const logo = document.quertSelector('.logo');
    const buttons = document.qurySelctor('.buttons');
    logo.addEventListener('click',() => displayItems(items));
    buttons.addEventListener('click',event => onButtonClick(event, items));
}

loadItems()
.then(items => {
    displayItems(items);
    setEventlisteners(items);
}  )

.catch(console.log);