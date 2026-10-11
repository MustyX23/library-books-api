import { useEffect, useState } from 'react'
import { type Book, getBooks } from './api'
import BookForm from './BookForm'

export default function App() {
  const [books, setBooks] = useState<Book[]>([])
  const [query, setQuery] = useState('')
  const [error, setError] = useState('')

  function load() {
    getBooks(query)
      .then((data) => {
        setBooks(data)
        setError('')
      })
      .catch(() => setError('Could not load books. Is the API running?'))
  }

  useEffect(load, [query])

  return (
    <main>
      <h1>Library Books</h1>
      {error && <p className="error">{error}</p>}
      <BookForm onAdded={load} />
      <input
        className="search"
        placeholder="Search by title or author"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      {books.length === 0 ? (
        <p>No books yet</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Title</th>
              <th>Author</th>
              <th>Year</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {books.map((book) => (
              <tr key={book.id}>
                <td>{book.title}</td>
                <td>{book.author}</td>
                <td>{book.year}</td>
                <td>{book.is_borrowed ? `Borrowed by ${book.borrower}` : 'Available'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  )
}
