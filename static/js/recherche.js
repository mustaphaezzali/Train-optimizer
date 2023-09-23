//list of info buttons
let infoButtons = document.querySelectorAll('[id="infoButton"]')
let infoContainers = document.querySelectorAll('[id="info"]')

console.log(infoButtons)
console.log(infoContainers)

//buttons states
let infoButtonsActive = []

infoButtons.forEach((infoButton, index) => {
    //init  state
    infoButtonsActive.push(true);
    //get corresponding info
    let info = infoContainers[index];

    // add on click event
    infoButton.addEventListener("click", () => {
        if (infoButtonsActive[index]) {
            info.style.display = "flex";
            setTimeout(() => {
                infoButton.setAttribute("class", "card-arrow-down card-arrow-down-flip")
                info.setAttribute("class", "card-arrow-info")
            }, 80);
        }
        else {
            infoButton.setAttribute("class", "card-arrow-down")
            info.setAttribute("class", "card-arrow-info card-arrow-info-hidden")
            setTimeout(() => {
                info.style.display = "none";
            }, 350);
        }
        infoButtonsActive[index] = !infoButtonsActive[index];

    });
})



