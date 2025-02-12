import { useEffect, useState } from 'react'
import './App.css'
import { ThreatTable } from './components/ThreatTable'
import axios from 'axios'

function App() {
  const [threats, setThreats] = useState([])
  const [loading, setLoading] = useState(false)

  // Get threats data from API service
  useEffect(() => {
    setLoading(true)
    axios
      .get('http://localhost:5000/api/threats?page=1&limit=10')
      .then((res) => {
        setThreats(res.data['threats'])
      })
      .catch((err) => {
        setThreats([])
        console.error(err)
      })
      .finally(() => {
        setLoading(false)
      })
  }, [])

  return (
    <>
      <h1>Threats</h1>
      <div className="card">
        <ThreatTable threats={threats} loading={loading} />
      </div>
    </>
  )
}

export default App
