
var height = 6; //nombre de possibilités
var width = 5; //longueur du mot

var row = 0; //nombre de tentatives effectuées
var col = 0; //nombre de lettres actuellement placées

var gameOver = false;

var wordList = ["lever", "kifez", "voyez"]

var guessList = ["bleue", "livre", "jolie"]

guessList = guessList.concat(wordList);

var word = wordList[Math.floor(Math.random()*wordList.length)].toUpperCase(); // on prend un mom au hasard de wordlist (math.random prend sa valeur entre 0 et 1 donc on multiplie par la longueur de la liste pour avoir le nombre de mots voulu en random possibilités), on utilise floor pour éviter les décimales entre 0 et 1
console.log(word);

window.onload = function(){  // en gros quand la page se charge, on appelle la fonction initialize
    intialize();
}


function intialize() {

    // On créer le tableau de jeu
    for (let r = 0; r < height; r++) {
        for (let c = 0; c < width; c++) {
            // <span id="0-0" class="tile">P</span> c'est en gros la commande qu'on fait ici sans devoir la copié-collé 40 fois
            let tile = document.createElement("span");  //span permet de mettre les "carrés" les uns à côtés des autres plutôt que en dessous avec passage à la ligne
            tile.id = r.toString() + "-" + c.toString();  // on créer les positions: 0-0, 0-1 ... (colonne - ligne)
            tile.classList.add("tile"); //on ajoute le style de "tile" tiré du css directement
            tile.innerText = ""; // on définit notre texte intérieur
            document.getElementById("board").appendChild(tile); // notre code va trouver la tableau et insérer ce code dans la partie html de board
        }
    }

    // On créer le clavier numérique
    let keyboard = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", " "],
        ["Entrer", "Z", "X", "C", "V", "B", "N", "M", "⌫" ]
    ]

    for (let i = 0; i < keyboard.length; i++) { // on créer un espace pour chaque lettre et on les places à l'intérieur du clavier numérique
        let currRow = keyboard[i];
        let keyboardRow = document.createElement("div");
        keyboardRow.classList.add("keyboard-row");

        for (let j = 0; j < currRow.length; j++) {
            let keyTile = document.createElement("div");

            let key = currRow[j];
            keyTile.innerText = key;
            if (key == "Entrer") {
                keyTile.id = "Entrer";
            }
            else if (key == "⌫") {
                keyTile.id = "Backspace";
            }
            else if ("A" <= key && key <= "Z") {
                keyTile.id = "Key" + key; // "Key" + "A"; par exemple
            } 

            keyTile.addEventListener("click", processKey);

            if (key == "Entrer") {
                keyTile.classList.add("enter-key-tile");
            } else {
                keyTile.classList.add("key-tile");
            }
            keyboardRow.appendChild(keyTile);
        }
        document.body.appendChild(keyboardRow);
    }
    

    // On traîte l'entrée utilisateur
    document.addEventListener("keyup", (e) => { // keyup permet de rentrer des lettres juste par le clavier, on utilise une fonction flèche 
        processInput(e);
    })
}

function processKey() {
    e = { "code" : this.id }; // permet de sélectionner une lettre du clavier numérique
    processInput(e);
}

function processInput(e) {
    if (gameOver) return; 

    // alert(e.code);
    if ("KeyA" <= e.code && e.code <= "KeyZ") { // on vérifie que l'utilisateur a pressé une lettre du clavier alphabétique entre A et Z
        if (col < width) {  // On vérifie que la colonne dans laquelle l'utilisateur rentre les lettres est bien inférieur à la longueur du tableau (5 ici)
            let currTile = document.getElementById(row.toString() + '-' + col.toString());
            if (currTile.innerText == "") { // on vérifie que le carré est vide, on peut passer au prochain après avoir compléter
                currTile.innerText = e.code[3]; // e.code renvoi KeyA... nous on veut seulement A, pas les 3 premières lettre "Key"
                col += 1;
            }
        }
    }
    else if (e.code == "Backspace") { // on gère le retour en arrière ici
        if (0 < col && col <= width) { // on permet à l'utilisateur de revenir en arrière uniquement si il a rentré au moins une lettre
            col -=1;
        }
        let currTile = document.getElementById(row.toString() + '-' + col.toString());
        currTile.innerText = "";
    }

    else if (e.code == "Enter") {
        update(); // On montre le nombre de bonnes lettres
    }

    if (!gameOver && row == height) { // si on a utilisé toutes les tentatives possibles, c'est game over
        gameOver = true;
        document.getElementById("answer").innerText = word; // on révèle le mot
    }
}

function update() { // on veut compter le nombre de lettres qui sont bonnes
    let guess = ""; 
    document.getElementById("answer").innerText = ""; 

    // on parcours les lettres du mot que le jouer a rentré
    for (let c = 0; c < width; c++) {
        let currTile = document.getElementById(row.toString() + '-' + c.toString());
        let letter = currTile.innerText;
        guess += letter;
    }

    guess = guess.toLowerCase(); //on vérifie que le mot appartient à la guess liste
    console.log(guess);

    if (!guessList.includes(guess)) { // si le mot n'est pas dans la guess liste
        document.getElementById("answer").innerText = "Pas dans la liste de mots";
        return;
    }
    
    //start processing guess
    let correct = 0;

    let letterCount = {}; // On regarde la fréquence d'apparition des différentes lettres du mot pour éviter les doublons , exemple : KENNY -> {K:1, E:1, N:2, Y: 1}
    for (let i = 0; i < word.length; i++) {
        let letter = word[i];

        if (letterCount[letter]) { // si la lettre est dans la liste
           letterCount[letter] += 1;
        } 
        else {
           letterCount[letter] = 1; // si elle ne l'est pas
        }
    }

    console.log(letterCount);

    // Pour la première itération, on regarde uniquement les lettres qui sont dans la bonne position
    for (let c = 0; c < width; c++) {
        let currTile = document.getElementById(row.toString() + '-' + c.toString());
        let letter = currTile.innerText; 
 
        //Est-ce que la lettre est à la bonne position ?
        if (word[c] == letter) {
            currTile.classList.add("correct");

            let keyTile = document.getElementById("Key" + letter); // On parcours aussi le clavier numérique pour pouvoir avoir la modification du clavier numérique avec
            keyTile.classList.remove("present"); // la lettre est présente
            keyTile.classList.add("correct"); // la lettre est au bon emplacement 

            correct += 1; // on passe à la lettre d'après
            letterCount[letter] -= 1; // On trouve une instance de cette lettre, donc on peut réduire le comptage de 1
        }

        if (correct == width) {
            gameOver = true; // si toutes les lettres sont dans l'état correct, on a directement fini
        }
    }

    console.log(letterCount);
    // on refait un "tour" en regardant quelles lettres sont présentes mais dans la mauvaise position
    for (let c = 0; c < width; c++) {
        let currTile = document.getElementById(row.toString() + '-' + c.toString());
        let letter = currTile.innerText;

        // On passe la lettre si elle a été marqué correcte
        if (!currTile.classList.contains("correct")) {
            //Est-ce que c'est dans le mot         //On fait attention à pas compter deux fois la lettre
            if (word.includes(letter) && letterCount[letter] > 0) { // on vérifie que dans notre liste de lettres, on a encore des lettres
                currTile.classList.add("present");
                
                let keyTile = document.getElementById("Key" + letter);
                if (!keyTile.classList.contains("correct")) {
                    keyTile.classList.add("present");
                }
                letterCount[letter] -= 1; // même principe que précédemment, on réduit
            } // Pas dans le mot 
            else {
                currTile.classList.add("absent");
                let keyTile = document.getElementById("Key" + letter);
                keyTile.classList.add("absent")
            }
        }
    }

    row += 1; // On passe  à la ligne d'apres
    col = 0; // On commence à la colonne 0 pour la nouvelle ligne
}