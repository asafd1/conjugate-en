let verbs = [];
const subjectGroup1 = ["I", "you", "we", "they"];
const subjectGroup2 = ["he", "she", "it"];
const tenses = ["present simple", "present continuous", "past simple", "past continuous", "future simple"];
const forms = ["positive", "negative", "question", "negative question"];

let currentVerb, currentSubject, currentTense, currentForm;

function generatePrompt() {
  currentVerb = verbs[Math.floor(Math.random() * verbs.length)];
  currentTense = tenses[Math.floor(Math.random() * tenses.length)];
  currentForm = forms[Math.floor(Math.random() * forms.length)];

  const subjectList = currentVerb.stative && currentTense.includes("continuous")
    ? [...subjectGroup1, ...subjectGroup2] : Math.random() < 0.5 ? subjectGroup1 : subjectGroup2;

  currentSubject = subjectList[Math.floor(Math.random() * subjectList.length)];

  document.getElementById("prompt").innerText = `${currentSubject}, ${currentTense}, ${currentForm}, verb: ${currentVerb.base}`;
  document.getElementById("user-input").value = ""; // Clear the input field
  document.getElementById("feedback").innerText = ""; // Clear feedback
}

function generateCorrectSentence() {
  const { base, third_person, gerund, past, stative } = currentVerb;

  // Handle stative verbs for continuous tenses
  if (stative && currentTense.includes("continuous")) {
    return "n/a";
  }

  if (currentTense === "present simple") {
    if (currentForm === "positive") {
      if (["he", "she", "it"].includes(currentSubject)) {
        return `${currentSubject} ${third_person}`;
      }
      return `${currentSubject} ${base}`;
    }
    if (currentForm === "negative") {
      if (["he", "she", "it"].includes(currentSubject)) {
        return `${currentSubject} doesn't ${base}`;
      }
      return `${currentSubject} don't ${base}`;
    }
    if (currentForm === "question") {
      if (["he", "she", "it"].includes(currentSubject)) {
        return `Does ${currentSubject} ${base}`;
      }
      return `Do ${currentSubject} ${base}`;
    }
    if (currentForm === "negative question") {
      if (["he", "she", "it"].includes(currentSubject)) {
        return `Doesn't ${currentSubject} ${base}`;
      }
      return `Don't ${currentSubject} ${base}`;
    }
  }

  if (currentTense === "present continuous") {
    if (currentForm === "positive") {
      if (currentSubject === "I") return `${currentSubject} am ${gerund}`;
      if (["he", "she", "it"].includes(currentSubject)) return `${currentSubject} is ${gerund}`;
      return `${currentSubject} are ${gerund}`;
    }
    if (currentForm === "negative") {
      if (currentSubject === "I") return `${currentSubject} am not ${gerund}`;
      if (["he", "she", "it"].includes(currentSubject)) return `${currentSubject} isn't ${gerund}`;
      return `${currentSubject} aren't ${gerund}`;
    }
    if (currentForm === "question") {
      if (currentSubject === "I") return `Am ${currentSubject} ${gerund}`;
      if (["he", "she", "it"].includes(currentSubject)) return `Is ${currentSubject} ${gerund}`;
      return `Are ${currentSubject} ${gerund}`;
    }
    if (currentForm === "negative question") {
      if (currentSubject === "I") return `Aren't I ${gerund}`;
      if (["he", "she", "it"].includes(currentSubject)) return `Isn't ${currentSubject} ${gerund}`;
      return `Aren't ${currentSubject} ${gerund}`;
    }
  }

  if (currentTense === "past simple") {
    if (currentForm === "positive") return `${currentSubject} ${past}`;
    if (currentForm === "negative") return `${currentSubject} didn't ${base}`;
    if (currentForm === "question") return `Did ${currentSubject} ${base}`;
    if (currentForm === "negative question") return `Didn't ${currentSubject} ${base}`;
  }

  if (currentTense === "past continuous") {
    if (currentForm === "positive") {
      if (["I", "he", "she", "it"].includes(currentSubject)) return `${currentSubject} was ${gerund}`;
      return `${currentSubject} were ${gerund}`;
    }
    if (currentForm === "negative") {
      if (["I", "he", "she", "it"].includes(currentSubject)) return `${currentSubject} wasn't ${gerund}`;
      return `${currentSubject} weren't ${gerund}`;
    }
    if (currentForm === "question") {
      if (["I", "he", "she", "it"].includes(currentSubject)) return `Was ${currentSubject} ${gerund}`;
      return `Were ${currentSubject} ${gerund}`;
    }
    if (currentForm === "negative question") {
      if (["I", "he", "she", "it"].includes(currentSubject)) return `Wasn't ${currentSubject} ${gerund}`;
      return `Weren't ${currentSubject} ${gerund}`;
    }
  }

  if (currentTense === "future simple") {
    if (currentForm === "positive") return `${currentSubject} will ${base}`;
    if (currentForm === "negative") return `${currentSubject} won't ${base}`;
    if (currentForm === "question") return `Will ${currentSubject} ${base}`;
    if (currentForm === "negative question") return `Won't ${currentSubject} ${base}`;
  }

  return "";
}

document.getElementById("submit-btn").addEventListener("click", function () {
  const userAnswer = document.getElementById("user-input").value.trim();
  const correctAnswer = generateCorrectSentence();

  if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
    document.getElementById("feedback").innerHTML = "<span class='correct'>Correct!</span>";
    setTimeout(generatePrompt, 1000); // Show the next prompt after 1 second
  } else {
    document.getElementById("feedback").innerHTML = `<span class='incorrect'>Incorrect. Try again.</span>`;
  }
});

// Fetch verbs from JSON file and initialize
fetch('verbs.json')
  .then(response => response.json())
  .then(data => {
    verbs = data;
    generatePrompt();  // Generate initial prompt after loading the verbs
  });
