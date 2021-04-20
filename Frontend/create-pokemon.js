const imgBaseURL =
  "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/";

const pkmnImg = document.querySelector("#pkmn-img");
const pkmnSelector = document.querySelector("#pkmn-selector");
const type1 = document.querySelector("#type1");
const type2 = document.querySelector("#type2");
const levelCounter = document.querySelector("#levelCount");
const levelRange = document.querySelector("#levelRange");

function capitalize(string) {
  return string[0].toUpperCase() + string.substring(1);
}
function stripLeftZeroes(string) {
  let regex = /[^0]+[0-9]*/;
  return string.match(regex)[0];
}

levelRange.oninput = function () {
  levelCounter.value = this.value;
};
levelCounter.onchange = function () {
  levelRange.value = this.value;
};
pkmnSelector.onchange = function () {
  let pkmn = this.value;
  fetch("../data/pkmnData.json")
    .then((response) => response.json())
    .then((data) => {
      let [primary, secondary] = data[pkmn].type;
      let imgURL = imgBaseURL + stripLeftZeroes(data[pkmn].no) + ".png";

      pkmnImg.src = imgURL;

      type1.innerText = capitalize(primary);
      type1.setAttribute("class", primary);
      if (secondary) {
        type2.innerText = capitalize(secondary);
        type2.setAttribute("class", secondary);
      } else {
        type2.setAttribute("class", "hidden");
        type1.classList.add("single-type");
      }
    });
};
