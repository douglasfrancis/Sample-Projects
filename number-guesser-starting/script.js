let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

generateTarget = () => {
  return Math.floor(Math.random()*10);
}

compareGuesses = (human, computer, generateTarget) => {
    if(Math.abs(human - generateTarget) <= Math.abs(computer - generateTarget)) {
      return true
    } else {
      return false
    }
};

updateScore = (winner) => {
 if(winner === 'human'){
   humanScore += 1;
 } else {
   computerScore +=1;
 }
}

advanceRound = () => {
  currentRoundNumber += 1
}





   
   
   
   
   
   
   