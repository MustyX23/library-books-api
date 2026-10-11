export const API_URL = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000'

export type Book = {
  id: number
  title: string
  author: string
  year: number
  is_borrowed: boolean
  borrower: string | null
}

export async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) throw new Error(`Request failed: ${res.status}`)
  return res.status === 204 ? (undefined as T) : res.json()
}

export type NewBook = Pick<Book, 'title' | 'author' | 'year'>

export const getBooks = (q = '') => request<Book[]>(q ? `/books?q=${encodeURIComponent(q)}` : '/books')
export const addBook = (book: NewBook) =>
  request<Book>('/books', { method: 'POST', body: JSON.stringify(book) })
export const deleteBook = (id: number) => request<void>(`/books/${id}`, { method: 'DELETE' })
