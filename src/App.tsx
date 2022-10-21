import React from 'react';
import logo from './logo.svg';
import './App.css';
import LineChart from './components/LineChart';
import Stats from './components/Stats';

function App() {
	return (
		<div className="bg-slate-800 h-screen p-10 flex justify-between">
			<LineChart></LineChart>
			<Stats></Stats>
		</div>
	);
}

export default App;
