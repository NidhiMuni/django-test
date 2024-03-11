import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Vote() {
  const [questions, setQuestions] = useState([]);
  const [choices, setChoices] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/')
      .then(response => {
        setQuestions(response.data.question);
        setChoices(response.data.choice);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Poll Questions</h1>
      {questions.map(question => (
        <div key={question.id}>
          <h2>{question.question_text}</h2>
          <ul>
            {choices
              .filter(choice => choice.question.id === question.id)
              .map(choice => (
                <li key={choice.id}>
                  {choice.choice_text} - Votes: {choice.votes}
                </li>
              ))}
          </ul>
        </div>
      ))}
    </div>
  );
  
}

export default Vote;
