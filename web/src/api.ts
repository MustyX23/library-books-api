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

export const getBooks = () => request<Book[]>('/books')
