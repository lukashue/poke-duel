const imgBaseURL =
  "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/";

const pkmnImg = document.querySelector("#pkmn-img");
const pkmnSelectors = document.querySelectorAll(".pkmn-selector");
const type1 = document.querySelector("#type1");
const type2 = document.querySelector("#type2");
const levelCounters = document.querySelectorAll(".levelCount");
const levelRanges = document.querySelectorAll(".levelRange");

function capitalize(string) {
  return string[0].toUpperCase() + string.substring(1);
}
function stripLeftZeroes(string) {
  let regex = /[^0]+[0-9]*/;
  return string.match(regex)[0];
}

for (let levelRange of levelRanges) {
  levelRange.oninput = function () {
    let levelCounter = levelRange.nextSibling.nextSibling;
    levelCounter.value = this.value;
  };
}
for (let levelCounter of levelCounters) {
  levelCounter.onchange = function () {
    let levelRange = levelCounter.previousSibling.previousSibling;
    levelRange.value = this.value;
  };
}
for (pkmnSelector of pkmnSelectors) {
  pkmnSelector.onchange = function () {
    let pkmn = this.value;
    fetch("../data/pkmnData.json")
      .then((response) => response.json())
      .then((data) => {
        let [primary, secondary] = data[pkmn].type;
        let imgURL = imgBaseURL + stripLeftZeroes(data[pkmn].no) + ".png";

        let siblings = this.parentElement.parentElement.children;
        let pkmnImg = siblings[0];
        let type1 = siblings[1].children[1].children[0];
        let type2 = siblings[1].children[1].children[1];

        pkmnImg.src = imgURL;

        type1.innerText = capitalize(primary);
        type1.setAttribute("class", primary);
        if (secondary) {
          type2.innerText = capitalize(secondary);
          type2.setAttribute("class", secondary);
        } else {
          type2.innerText = "";
          type2.setAttribute("class", "hidden");
        }
      });
  };
}
