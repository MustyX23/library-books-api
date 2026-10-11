import { type FormEvent, useState } from 'react'
import { addBook } from './api'

export default function BookForm({ onAdded }: { onAdded: () => void }) {
  const [title, setTitle] = useState('')
  const [author, setAuthor] = useState('')
  const [year, setYear] = useState('')
  const [error, setError] = useState('')

  async function handleSubmit(e: FormEvent) {
    e.preventDefault()
    try {
      await addBook({ title, author, year: Number(year) })
      setTitle('')
      setAuthor('')
      setYear('')
      setError('')
      onAdded()
    } catch {
      setError('Could not save the book. Check that all fields are filled in.')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="Author" value={author} onChange={(e) => setAuthor(e.target.value)} />
      <input placeholder="Year" type="number" value={year} onChange={(e) => setYear(e.target.value)} />
      <button type="submit">Add book</button>
      {error && <p className="error">{error}</p>}
    </form>
  )
}
