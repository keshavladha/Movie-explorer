import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { Movie, MovieSummary, Actor, Director, Genre, FilterOptions } from '@/types'
import { movieApi } from '@/services/api'

export const useMovieStore = defineStore('movie', () => {
  // State
  const movies = ref<MovieSummary[]>([])
  const currentMovie = ref<Movie | null>(null)
  const actors = ref<Actor[]>([])
  const directors = ref<Director[]>([])
  const genres = ref<Genre[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Getters
  const moviesCount = computed(() => movies.value.length)
  const uniqueReleaseYears = computed(() => {
    const years = movies.value.map(movie => movie.release_year)
    return [...new Set(years)].sort((a, b) => b - a)
  })

  // Actions
  const fetchMovies = async (filters?: FilterOptions) => {
    loading.value = true
    error.value = null
    try {
      movies.value = await movieApi.getMovies(filters)
    } catch (err) {
      error.value = 'Failed to fetch movies'
      console.error('Error fetching movies:', err)
    } finally {
      loading.value = false
    }
  }

  const fetchMovie = async (id: number) => {
    loading.value = true
    error.value = null
    try {
      currentMovie.value = await movieApi.getMovie(id)
    } catch (err) {
      error.value = 'Failed to fetch movie details'
      console.error('Error fetching movie:', err)
    } finally {
      loading.value = false
    }
  }

  const fetchActors = async (filters?: { movie_id?: number; genre_id?: number }) => {
    loading.value = true
    error.value = null
    try {
      actors.value = await movieApi.getActors(filters)
    } catch (err) {
      error.value = 'Failed to fetch actors'
      console.error('Error fetching actors:', err)
    } finally {
      loading.value = false
    }
  }

  const fetchActor = async (id: number) => {
    loading.value = true
    error.value = null
    try {
      const actor = await movieApi.getActor(id)
      return actor
    } catch (err) {
      error.value = 'Failed to fetch actor details'
      console.error('Error fetching actor:', err)
      return null
    } finally {
      loading.value = false
    }
  }

  const fetchDirectors = async () => {
    loading.value = true
    error.value = null
    try {
      directors.value = await movieApi.getDirectors()
    } catch (err) {
      error.value = 'Failed to fetch directors'
      console.error('Error fetching directors:', err)
    } finally {
      loading.value = false
    }
  }

  const fetchDirector = async (id: number) => {
    loading.value = true
    error.value = null
    try {
      const director = await movieApi.getDirector(id)
      return director
    } catch (err) {
      error.value = 'Failed to fetch director details'
      console.error('Error fetching director:', err)
      return null
    } finally {
      loading.value = false
    }
  }

  const fetchGenres = async () => {
    loading.value = true
    error.value = null
    try {
      genres.value = await movieApi.getGenres()
    } catch (err) {
      error.value = 'Failed to fetch genres'
      console.error('Error fetching genres:', err)
    } finally {
      loading.value = false
    }
  }

  const clearError = () => {
    error.value = null
  }

  return {
    // State
    movies,
    currentMovie,
    actors,
    directors,
    genres,
    loading,
    error,
    // Getters
    moviesCount,
    uniqueReleaseYears,
    // Actions
    fetchMovies,
    fetchMovie,
    fetchActors,
    fetchActor,
    fetchDirectors,
    fetchDirector,
    fetchGenres,
    clearError
  }
}) 