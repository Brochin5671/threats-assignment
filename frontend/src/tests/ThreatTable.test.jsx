import { render, screen, cleanup, waitFor } from '@testing-library/react'
import { ThreatTable } from '../components/ThreatTable'
import { afterEach, beforeEach, expect, it, vi } from 'vitest'
import axios from 'axios'

// Mock Axios
vi.mock('axios')
afterEach(cleanup)

describe('ThreatTable', () => {
  it('displays filled table', async () => {
    axios.get.mockResolvedValueOnce({
      data: {
        threats: [
          {
            id: 1,
            host: 'evil',
            url: 'evil.com',
            threat_type: 'bad',
            date_added: '1/1/2024 00:00:00 UTC',
          },
        ],
        length: 1,
      },
    })
    render(<ThreatTable />)
    await waitFor(() => {
      expect(screen.getByText('evil')).toBeInTheDocument()
    })
  })

  it('displays empty table', async () => {
    axios.get.mockResolvedValueOnce({
      data: {
        threats: [],
        length: 0,
      },
    })
    render(<ThreatTable />)
    await waitFor(() => {
      expect(screen.getByText('No rows')).toBeInTheDocument()
    })
  })

  it('displays empty table from axios error', async () => {
    axios.get.mockRejectedValueOnce(new Error('Axios mock test failure'))
    render(<ThreatTable />)
    await waitFor(() => {
      expect(screen.getByText('No rows')).toBeInTheDocument()
    })
  })
})
