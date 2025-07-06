// Import prompt-sync for terminal input
const prompt = require('prompt-sync')({ sigint: true });


const questions = [
  {
    q: "1) What does const mean in JS?",
    options: ["A. can be reassigned", "B. can't be reassigned", "C. it's a loop"],
    answer: "B"
  },
  {
    q: "2) Which is valid function syntax?",
    options: ["A. function myFunc()", "B. const myFunc => {}", "C. var myFunc = function()"],
    answer: "A"
  },
  {
    q: "3) What does === test?",
    options: ["A. value only", "B. type only", "C. value & type"],
    answer: "C"
  }
];

let score = 0;


questions.forEach(q => {
  console.log(`\n${q.q}`);
  q.options.forEach(opt => console.log(opt));

  const ans = prompt("Your answer (A/B/C): ").trim().toUpperCase();
  if (ans === q.answer) {
    console.log("Correct!");
    score++;
  } else {
    console.log(`Wrong. Correct answer is ${q.answer}`);
  }
});


console.log(`\n Quiz Complete! Your score: ${score} / ${questions.length}`);