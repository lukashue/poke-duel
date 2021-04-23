const imgBaseURL =
  "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/";

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

        let header = this.parentElement.parentElement;

        let pkmnImg = header.querySelector(".pkmn-img");
        pkmnImg.src = imgURL;

        let typeSpans = header.querySelectorAll(".type");
        let type1 = typeSpans[0];
        let type2 = typeSpans[1];
        type1.innerText = capitalize(primary);
        type1.setAttribute("class", "type " + primary);
        if (secondary) {
          type2.innerText = capitalize(secondary);
          type2.setAttribute("class", "type " + secondary);
        } else {
          type2.innerText = "";
          type2.setAttribute("class", "type hidden");
        }
      });
  };
}
