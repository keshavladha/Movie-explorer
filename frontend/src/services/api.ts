import axios from 'axios'
import type { Movie, MovieSummary, Actor, Director, Genre, FilterOptions } from '@/types'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

export const movieApi = {
  // Movies
  getMovies: (filters?: FilterOptions): Promise<MovieSummary[]> =>
    api.get('/movies/', { params: filters }).then(res => res.data),
  
  getMovie: (id: number): Promise<Movie> =>
    api.get(`/movies/${id}`).then(res => res.data),

  // Actors
  getActors: (filters?: { movie_id?: number; genre_id?: number }): Promise<Actor[]> =>
    api.get('/actors/', { params: filters }).then(res => res.data),
  
  getActor: (id: number): Promise<Actor> =>
    api.get(`/actors/${id}`).then(res => res.data),

  // Directors
  getDirectors: (): Promise<Director[]> =>
    api.get('/directors/').then(res => res.data),
  
  getDirector: (id: number): Promise<Director> =>
    api.get(`/directors/${id}`).then(res => res.data),

  // Genres
  getGenres: (): Promise<Genre[]> =>
    api.get('/genres/').then(res => res.data),
  
  getGenre: (id: number): Promise<Genre> =>
    api.get(`/genres/${id}`).then(res => res.data)
}

export default api 