import { useEffect, useState } from 'react'
import './App.css'
import { ThreatTable } from './components/ThreatTable'
import axios from 'axios'

function App() {
  return (
    <>
      <h1>Threats</h1>
      <div className="card">
        <ThreatTable />
      </div>
    </>
  )
}

export default App
