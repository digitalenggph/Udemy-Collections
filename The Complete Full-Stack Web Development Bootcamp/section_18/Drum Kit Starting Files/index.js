const drumSet = document.querySelector(".set")
const soundEffects = {
    "w": "tom-1.mp3",
    "a": "tom-2.mp3",
    "s": "tom-3.mp3",
    "d": "tom-4.mp3",
    "j": "snare.mp3",
    "k": "crash.mp3",
    "l": "kick-bass.mp3",
}

// detect button click
drumSet.addEventListener('click', (e) => {
    const target = e.target;
    // do not proceed logic if item clicked is not button
    if (!target.matches('button')) return; 

    const pressedButton = target.textContent;
    playSound(pressedButton);
});

// detect keypress
document.addEventListener('keydown', (e) => {
    const pressedKey = e.key;
    if (soundEffects[pressedKey] !== undefined) {
        playSound(pressedKey);
    };
});

function playSound(key) {
    const mp3 = soundEffects[key];
    const audioAddress = `./sounds/${mp3}`;
    const audio = new Audio(audioAddress);
    audio.play();
}


