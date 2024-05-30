import './Calculator.css';
import React, { useState } from 'react';

const Calculator = () => {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const calculateExpression = async () => {
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/calculator`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expr: expression })
      });
      if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.detail);
        return;
      }
      const data = await response.json();
      setResult(data.result);
      setError(null);
    } catch (err) {
      setError('An unexpected error occurred');
    }
  };

  const downloadCSV = () => {
    const link = document.createElement('a');
    link.href = `${process.env.REACT_APP_API_URL}/export/csv`;
    link.setAttribute('download', 'rpn_expressions.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div>
      <h1>RPN Calculator</h1>
      <input
        type="text"
        value={expression}
        onChange={e => setExpression(e.target.value)}
        placeholder="Enter RPN expression"
      />
      <button onClick={calculateExpression}>Calculate</button>
      {result !== null && (
        <div>
          <h2>Result: {result}</h2>
        </div>
      )}
      {error && (
        <div>
          <h2>Error: {error}</h2>
        </div>
      )}
      <button onClick={downloadCSV}>Download CSV</button>
    </div>
  );
};

export default Calculator;
