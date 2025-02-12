import { Paper } from '@mui/material'
import { DataGrid, GridToolbar } from '@mui/x-data-grid'
import { useMemo } from 'react'

export const ThreatTable = ({ threats, loading }) => {
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
        valueFormatter: (value) => value?.toLocaleString(), // TODO: fix issue with date filtering
      },
    ],
    [threatTypes]
  )

  return (
    <Paper>
      <DataGrid
        rows={threats?.map((threat, i) => ({ ...threat, id: i }))}
        columns={columns}
        initialState={{
          pagination: { paginationModel: { page: 0, pageSize: 10 } },
        }}
        pageSizeOptions={[5, 10, 25, 50, 100]}
        sx={{ border: 0 }}
        slots={{ toolbar: GridToolbar }}
        loading={loading}
      />
    </Paper>
  )
}
