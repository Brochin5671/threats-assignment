import { Paper } from '@mui/material'
import { DataGrid, GridToolbar } from '@mui/x-data-grid'
import { useMemo, useState, useEffect } from 'react'
import axios from 'axios'

export const ThreatTable = () => {
  const [threats, setThreats] = useState([])
  const [loading, setLoading] = useState(false)

  const [page, setPage] = useState(1)
  const [limit, setLimit] = useState(10)
  const [length, setLength] = useState(0)

  // Get threats data from API service
  const getThreats = async () => {
    setLoading(true)
    try {
      const res = await axios.get(
        `http://localhost:5000/api/threats?page=${page}&limit=${limit}`
      )
      setThreats(res.data['threats'])
      setLength(res.data['length'])
    } catch (err) {
      setThreats([])
      setLength(0)
    }
    setLoading(false)
  }

  // Get threats data when there is a change to the pagination model
  useEffect(() => {
    getThreats()
  }, [page, limit])

  const threatTypes = useMemo(
    () => [...new Set(threats?.map((threat) => threat['threat_type']))],
    [threats]
  )
  const columns = useMemo(
    () => [
      { field: 'host', headerName: 'Host', width: 200 },
      { field: 'url', headerName: 'URL', width: 250 },
      {
        field: 'threat_type',
        headerName: 'Threat Type',
        width: 150,
        type: 'singleSelect',
        valueOptions: threatTypes,
      },
      {
        field: 'date_added',
        headerName: 'Date Added',
        width: 175,
        type: 'datetime',
        valueGetter: (date) => date && new Date(date),
        valueFormatter: (value) => value?.toLocaleString(),
      },
    ],
    [threatTypes]
  )

  return (
    <Paper>
      <DataGrid
        aria-label="Threats table data"
        rows={threats?.map((threat, i) => ({ ...threat, id: i }))}
        columns={columns}
        initialState={{
          pagination: { paginationModel: { page: 0, pageSize: 10 } },
        }}
        pageSizeOptions={[5, 10, 25, 50, 100]}
        sx={{ border: 0 }}
        slots={{ toolbar: GridToolbar }}
        loading={loading}
        onPaginationModelChange={(model) => {
          setPage(model.page + 1)
          setLimit(model.pageSize)
        }}
        paginationMode="server"
        rowCount={length}
      />
    </Paper>
  )
}
