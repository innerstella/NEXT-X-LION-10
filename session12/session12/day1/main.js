play = (e) => {
  let audio = document.querySelectorAll(`[data-key="${e.keyCode}"]`)[1];
  let key = document.querySelectorAll(`[data-key="${e.keyCode}"]`)[0];
  if (audio) {
    audio.play();
    key.classList.add("play");
  }
  console.log('누름');
};
pause = (e) => {
  let audio = document.querySelectorAll(`[data-key="${e.keyCode}"]`)[1];
  let key = document.querySelectorAll(`[data-key="${e.keyCode}"]`)[0];
  if (audio) {
    audio.currentTime = 0;
    audio.pause();
    key.classList.remove("play");
  }
};

window.onkeydown = play;
window.onkeyup = pause;